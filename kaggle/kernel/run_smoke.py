"""Standalone Kaggle GPU/data/checkpoint smoke test for SPAQ."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import tarfile
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import torch
import torchvision
from PIL import Image
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torchvision.models import resnet18
from torchvision.transforms import v2


WORKING = Path("/kaggle/working")
INPUT = Path("/kaggle/input")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class Images(Dataset):
    def __init__(self, frame: pd.DataFrame, root: Path) -> None:
        self.frame = frame.reset_index(drop=True)
        self.root = root
        self.transform = v2.Compose(
            [v2.Resize((224, 224)), v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]
        )

    def __len__(self) -> int:
        return len(self.frame)

    def __getitem__(self, index: int):
        row = self.frame.iloc[index]
        with Image.open(self.root / row.image_name) as image:
            tensor = self.transform(image.convert("RGB"))
        return tensor, torch.tensor(float(row.MOS), dtype=torch.float32)


def locate_one(pattern: str) -> Path:
    matches = sorted(INPUT.glob(pattern))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {pattern} under /kaggle/input, found {len(matches)}")
    return matches[0]


def main() -> None:
    torch.manual_seed(20261109)
    archive_path = locate_one("**/spaq.tar")
    manifest_path = locate_one("**/manifest.parquet")
    manifest = pd.read_parquet(manifest_path)
    sample = manifest.loc[manifest.split == "train"].sort_values("image_name").head(300)
    image_root = WORKING / "smoke_images"
    image_root.mkdir(exist_ok=True)
    extract_started = time.perf_counter()
    with tarfile.open(archive_path, "r:") as archive:
        for image_name in sample.image_name:
            target = image_root / image_name
            if target.is_file():
                continue
            source = archive.extractfile(f"spaq/{image_name}")
            if source is None:
                raise RuntimeError(f"Missing archive member {image_name}")
            temporary = target.with_suffix(".tmp")
            temporary.write_bytes(source.read())
            os.replace(temporary, target)
    extract_seconds = time.perf_counter() - extract_started

    dataset = Images(sample, image_root)
    loader = DataLoader(dataset, batch_size=16, shuffle=False, num_workers=2, pin_memory=True)
    if not torch.cuda.is_available():
        raise RuntimeError("Kaggle smoke requires a CUDA accelerator")
    device = torch.device("cuda")
    model = resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 1)
    model.to(device)
    torch.cuda.reset_peak_memory_stats()

    inference_started = time.perf_counter()
    model.eval()
    with torch.inference_mode():
        for images, _ in loader:
            model(images.to(device, non_blocking=True))
    torch.cuda.synchronize()
    inference_seconds = time.perf_counter() - inference_started

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    criterion = nn.L1Loss()
    train_loader = DataLoader(dataset, batch_size=8, shuffle=True, num_workers=2)
    iterator = iter(train_loader)
    train_started = time.perf_counter()
    model.train()
    losses = []
    for _ in range(20):
        try:
            images, targets = next(iterator)
        except StopIteration:
            iterator = iter(train_loader)
            images, targets = next(iterator)
        optimizer.zero_grad(set_to_none=True)
        predictions = model(images.to(device)).squeeze(1)
        loss = criterion(predictions, targets.to(device))
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach().cpu()))
    torch.cuda.synchronize()
    train_seconds = time.perf_counter() - train_started

    checkpoint = WORKING / "smoke_checkpoint.pt"
    temporary = checkpoint.with_suffix(".tmp")
    torch.save({"model": model.state_dict(), "optimizer": optimizer.state_dict(), "step": 20}, temporary)
    os.replace(temporary, checkpoint)
    reloaded = resnet18(weights=None)
    reloaded.fc = nn.Linear(reloaded.fc.in_features, 1)
    payload = torch.load(checkpoint, map_location="cpu", weights_only=False)
    reloaded.load_state_dict(payload["model"])

    disk = shutil.disk_usage(WORKING)
    summary = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "status": "EXECUTION_VERIFIED",
        "python": platform.python_version(),
        "torch": torch.__version__,
        "torchvision": torchvision.__version__,
        "gpu": torch.cuda.get_device_name(0),
        "gpu_total_bytes": torch.cuda.get_device_properties(0).total_memory,
        "gpu_peak_allocated_bytes": torch.cuda.max_memory_allocated(),
        "working_disk_total_bytes": disk.total,
        "working_disk_free_bytes": disk.free,
        "archive_path": str(archive_path),
        "archive_bytes": archive_path.stat().st_size,
        "manifest_sha256": sha256(manifest_path),
        "sample_count": 300,
        "extract_seconds": extract_seconds,
        "inference_300_seconds": inference_seconds,
        "train_20_steps_seconds": train_seconds,
        "train_loss_first": losses[0],
        "train_loss_last": losses[-1],
        "checkpoint_sha256": sha256(checkpoint),
        "checkpoint_reload_succeeded": True,
    }
    (WORKING / "smoke_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
