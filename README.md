# When Does EXIF Help Smartphone Image Quality Assessment?

This repository is an executed, resource-adapted study of EXIF fusion and metadata missingness on SPAQ. It compares five matched MOS regressors on a repeated-content-safe 70/10/20 split of 11,125 real images. The controlled result is modest: additive EXIF (E1) improves the image-only baseline (E0) under paired test-image resampling, but a larger gated fusion model (E2) does not reliably improve E1, and metadata dropout (E3/E4) does not help.

This is not a claim of reproducing the original SPAQ training numbers. The study uses one frozen ImageNet-V2 ResNet-50 feature cache so all variants can be executed and controlled within available compute. The original SPAQ and TOPIQ paper values remain literature references only.

## Verified results

All rows use seed `20261109`, split SHA-256 `91a8d1...a108`, manifest SHA-256 `abff8b...5800d`, and frozen feature cache SHA-256 `b639bb...975ed`.

| Experiment | Change from control | Test SRCC | Test PLCC | Test MAE |
|---|---|---:|---:|---:|
| E0 | Image-only head | 0.83048 | 0.83063 | 9.3489 |
| E1 | E0 + 16-parameter additive EXIF offset | **0.83613** | 0.83572 | 9.1942 |
| E2 | E1 fusion replaced by 8,704-parameter gate | 0.83602 | **0.83779** | **9.1179** |
| E3 | E1 + 50% record-level metadata dropout | 0.83450 | 0.83452 | 9.2534 |
| E4 | E2 + 50% record-level metadata dropout | 0.83208 | 0.83337 | 9.3265 |

The prespecified E1-E0 paired difference is +0.00565 SRCC with 95% bootstrap interval [0.00132, 0.01013]. E2-E1 is -0.00012 [-0.00516, 0.00484], so the gated mechanism has no reliable SRCC advantage here. These intervals measure test-image sampling uncertainty, not training-seed uncertainty.

![Paired bootstrap confidence intervals](docs/figures/paired_bootstrap_cis.png)

At 100% missing test EXIF, SRCC is 0.83579/0.83290/0.83432/0.82813 for E1/E2/E3/E4. Training-time metadata dropout did not improve either fusion family.

![Metadata missingness](docs/figures/missingness_srcc.png)

## Data provenance and license caution

The original SPAQ Drive link is broken. The recovery chain is:

- Compact image variant: `q-future/q-align-datasets`, revision `3da8831b...e376`, `spaq.tar`, 2,626,897,920 bytes, SHA-256 `d312242f...2194`.
- Author-recommended originals and workbooks: `chaofengc/IQA-PyTorch-Datasets`, revision `f97c4f5d...1bef`, `spaq.tgz`, 34,841,101,349 bytes, SHA-256 `54e0cb49...7418f7`.
- Exact case-sensitive filename join: 11,125/11,125 with no orphan or collision.

The compact archive has no annotations and no embedded EXIF. The larger archive contains 11,125 original JPEGs and three authentic workbooks. Embedded EXIF was inspected in every original: scene brightness is observed in 8,546 rows and author-estimated in 2,579. No EXIF or MOS value is fabricated. `03461.jpg` has invalid raw exposure and remains explicitly invalid; the separate author APEX value is retained with provenance.

The mirror card's license does not prove that all underlying SPAQ photographs are relicensed. Raw images/workbooks remain Git-ignored and are not redistributed. See [dataset recovery](docs/DATASET_RECOVERY.md) and [provenance](data/provenance.json).

## Leakage protection

The compact images contain 322 byte-identical pairs, 321 with different MOS. A dHash radius-four audit adds 747 non-exact repeated-content candidates. All 1,069 candidate edges are grouped before splitting, yielding 7,786 train, 1,111 validation, and 2,228 test rows with zero candidate-edge crossings. The inherited Q-Align split was rejected because it separates 103 exact pairs.

## Environment and setup

The executed environment used Python 3.12.10, PyTorch 2.14.1+cu130, torchvision 0.29.1+cu130, and an RTX 4050 Laptop GPU.

```powershell
py -3.12 -m venv .venv312
.\.venv312\Scripts\python.exe -m pip install --upgrade pip
.\.venv312\Scripts\python.exe -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu130
.\.venv312\Scripts\python.exe -m pip install -e ".[dev,analysis]"
.\.venv312\Scripts\python.exe -m pytest -q
```

Dataset acquisition is intentionally not hidden behind an unverified downloader. Download the two pinned objects above, verify their exact byte counts/SHA-256, and use the audit/build scripts documented in [dataset recovery](docs/DATASET_RECOVERY.md). The tracked `data/manifest.parquet` is the frozen row contract; raw files are ignored.

## Reproduce the resource-adapted experiments

Assuming compact images are extracted under `data/raw/q_align/extracted/spaq`:

```powershell
$py = ".\.venv312\Scripts\python.exe"
& $py scripts\extract_features.py --manifest data\manifest.parquet --image-root data\raw\q_align\extracted\spaq --output artifacts\features\spaq_resnet50_imagenet_v2_abff8b1a.npz --evidence-output evidence\feature_cache_resnet50.json
$commit = git rev-parse HEAD
foreach ($e in "E0","E1","E2","E3","E4") {
  $id = $e.ToLower()
  & $py scripts\train_cached_head.py --experiment $e --manifest data\manifest.parquet --features artifacts\features\spaq_resnet50_imagenet_v2_abff8b1a.npz --output-dir "artifacts\runs\${id}_frozen_r50_s20261109" --evidence-output "evidence\${id}_frozen_r50_s20261109.json" --source-commit $commit --seed 20261109
}
& $py scripts\evaluate_missingness.py --manifest data\manifest.parquet --features artifacts\features\spaq_resnet50_imagenet_v2_abff8b1a.npz --e1-checkpoint artifacts\runs\e1_frozen_r50_s20261109\best.pt --e2-checkpoint artifacts\runs\e2_frozen_r50_s20261109\best.pt --e3-checkpoint artifacts\runs\e3_frozen_r50_s20261109\best.pt --e4-checkpoint artifacts\runs\e4_frozen_r50_s20261109\best.pt --predictions-output artifacts\runs\missingness_all_s20261109\predictions.csv --summary-output evidence\missingness_all_s20261109.json
& $py scripts\analyze_results.py --seed 20261109 --bootstrap-resamples 10000
```

E0-E4 use validation SRCC for early stopping and open the test set only for final prediction. Configs, checkpoints, logs, and per-image predictions are retained under ignored `artifacts/runs/`; hashes are in tracked evidence JSON.

## Kaggle status

The standalone smoke kernel is ready but has not run remotely because Kaggle authentication is absent. This is an external blocker, not a successful run. After user OAuth, follow [KAGGLE_RUNBOOK.md](docs/KAGGLE_RUNBOOK.md). Do not commit credentials or claim local RTX evidence as Kaggle evidence.

## Repository map

- [Experiment report](docs/EXPERIMENT_REPORT.md): methods, results, limitations, and citations.
- [Acceptance audit](docs/ACCEPTANCE_AUDIT.md): gate-by-gate evidence and remaining blockers.
- `evidence/`: execution summaries, paired tables, hashes, and environment evidence.
- `scripts/`: data audits, split/manifest construction, training, robustness, and analysis.
- `src/spaq_iqa/`: tested data, EXIF, metric, model, and grouping components.
- `PROJECT_STATUS.md`, `STATE.json`, `TASKS.md`, `SESSION_HANDOFF.md`: persistent resume state.

## Main limitations

- One training seed; bootstrap intervals do not capture optimization variability.
- Frozen, downsampled/re-encoded visual inputs; not a faithful SPAQ end-to-end reproduction.
- No defensible device-OOD claim: raw make/model aliases do not form a clean 66-phone identifier.
- Capture-condition subgroups are exploratory and overlap.
- Kaggle remote smoke is blocked on OAuth; no kernel ID/version exists.
- TOPIQ is a related Q1 reference, not an executed matched comparator because protocol/checkpoint overlap would make the comparison misleading.
