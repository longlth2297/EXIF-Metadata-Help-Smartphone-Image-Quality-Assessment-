"""Validate the persisted release evidence without retraining models."""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    checks: dict[str, object] = {}
    manifest_path = ROOT / "data" / "manifest.parquet"
    manifest = pd.read_parquet(manifest_path)
    checks["manifest_sha256"] = sha256(manifest_path)
    checks["manifest_rows"] = len(manifest)
    checks["split_counts"] = manifest["split"].value_counts().sort_index().to_dict()
    checks["unique_image_names"] = int(manifest["image_name"].nunique())
    group_partitions = manifest.groupby("group_id")["split"].nunique()
    checks["groups_crossing_splits"] = int((group_partitions > 1).sum())

    expected_manifest = "abff8b1a5f7d2e74d0c8874655fbe40d5e75de75bf61e65753c7085cee15800d"
    if checks["manifest_sha256"] != expected_manifest:
        raise AssertionError("Canonical manifest hash differs from frozen contract")
    if checks["manifest_rows"] != 11125 or checks["unique_image_names"] != 11125:
        raise AssertionError("Canonical manifest row/key count changed")
    if checks["split_counts"] != {"test": 2228, "train": 7786, "val": 1111}:
        raise AssertionError("Frozen split counts changed")
    if checks["groups_crossing_splits"] != 0:
        raise AssertionError("A content group crosses partitions")

    evidence_names = [
        "e0_frozen_r50_s20261109.json", "e1_frozen_r50_s20261109.json",
        "e2_frozen_r50_s20261109.json", "e3_frozen_r50_s20261109.json",
        "e4_frozen_r50_s20261109.json", "missingness_all_s20261109.json",
        "analysis_summary_s20261109.json", "kaggle_smoke_v2.json",
    ]
    checks["evidence_status"] = {}
    for name in evidence_names:
        payload = json.loads((ROOT / "evidence" / name).read_text(encoding="utf-8"))
        status = payload.get("status")
        if status not in {"SUCCESS", "EXECUTION_VERIFIED"}:
            raise AssertionError(f"{name}: unexpected status {status!r}")
        checks["evidence_status"][name] = status

    analysis = json.loads((ROOT / "evidence" / "analysis_summary_s20261109.json").read_text())
    verified_outputs = {}
    for relative, expected in analysis["output_sha256"].items():
        path = ROOT / relative.replace("\\", "/")
        observed = sha256(path)
        if observed != expected:
            raise AssertionError(f"Analysis output hash mismatch: {relative}")
        verified_outputs[relative] = observed
    checks["verified_analysis_outputs"] = len(verified_outputs)

    kaggle = json.loads((ROOT / "evidence" / "kaggle_smoke_v2.json").read_text())
    kaggle_output_root = ROOT / "artifacts" / "kaggle_download" / "v2"
    verified_kaggle_outputs = {}
    for name, expected in kaggle["downloaded_artifacts"].items():
        path = kaggle_output_root / name
        observed = sha256(path)
        if observed != expected:
            raise AssertionError(f"Kaggle output hash mismatch: {name}")
        verified_kaggle_outputs[name] = observed
    checks["verified_kaggle_outputs"] = verified_kaggle_outputs

    ignored_targets = [
        "data/raw/q_align/spaq.tar",
        "data/raw/iqa_pytorch_datasets/spaq.tgz",
        "artifacts/features/spaq_resnet50_imagenet_v2_abff8b1a.npz",
        "artifacts/runs/e1_frozen_r50_s20261109/best.pt",
        "kaggle/kernel/kernel-metadata.json",
    ]
    ignored_input = ("\n".join(ignored_targets) + "\n").encode("utf-8")
    ignored = subprocess.run(
        ["git", "check-ignore", "--stdin"], cwd=ROOT, input=ignored_input,
        capture_output=True, check=False,
    ).stdout.decode("utf-8").splitlines()
    checks["ignored_sensitive_targets"] = sorted(ignored)
    if sorted(ignored) != sorted(ignored_targets):
        raise AssertionError("One or more raw/credential/artifact targets are not ignored")

    required_docs = [
        "README.md", "docs/EXPERIMENT_REPORT.md", "docs/ACCEPTANCE_AUDIT.md",
        "docs/KAGGLE_RUNBOOK.md", "PROJECT_STATUS.md", "STATE.json", "SESSION_HANDOFF.md",
    ]
    missing_docs = [name for name in required_docs if not (ROOT / name).is_file()]
    checks["missing_required_docs"] = missing_docs
    if missing_docs:
        raise AssertionError(f"Missing release documents: {missing_docs}")

    result = {
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "status": "SUCCESS",
        "checks": checks,
    }
    output = ROOT / "evidence" / "release_validation.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
