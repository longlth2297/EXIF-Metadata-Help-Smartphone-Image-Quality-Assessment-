# SESSION HANDOFF

**Updated UTC:** 2026-11-09T07:28:45Z
**Repo path/commit:** `D:\HCMUS\Year2\Scientific Method\SC\spaq-exif-robustness` / `57b3ee3dc5a352fea19a9441332a6e78d2db896e`
**Most advanced completed gate:** G6
**Active Kaggle kernel/version/status:** `longltrnhong/spaq-exif-robustness-smoke` / v2 / COMPLETE
**Last valid checkpoint:** `artifacts/runs/e2_frozen_r50_s20261109/best.pt`

## Verified completed tasks

- Read all controlling local documents and both research reports.
- Verified the handoff package hashes against its manifest.
- Initialized the project repository and durable progress ledger; committed the G0/recovery milestone.
- Installed Kaggle CLI 2.2.5 and established OAuth for `longltrnhong`.
- Downloaded and verified Q-Align `spaq.tar`: 11,125 readable JPEGs, no annotations or embedded EXIF.
- Retrieved pinned IQA-PyTorch metadata and matched all 11,125 rows to archive filenames with no orphans/collisions.
- Hashed every Q-Align image and identified 322 exact duplicate pairs. All pairs conflict on at least one subjective field, 321 conflict on MOS, all agree on EXIF, and 103 cross the Q-Align train/test boundary.
- Downloaded and hash-verified the 34.8 GB author-recommended archive; streamed it without full extraction and recovered the original workbooks.
- Proved exact 11,125-row workbook/mirror equality and audited embedded EXIF for every original JPEG.
- Froze the repeated-content-grouped split and built `data/manifest.parquet` with observed/estimated masks.
- Installed `.venv312`; local RTX 4050 CUDA operation and 10 tests pass.
- Extracted all 11,125 compact images and ran the 16-image/20-step ResNet-50 vertical slice with atomic checkpoint, bit-exact reload, optimizer resume, and 1.20 GB peak allocation.
- Four-image overfit sanity reduced L1 from 54.29 to 1.49 (minimum 0.17) in 200 steps; 12 tests pass.
- Packaged and executed the standalone Kaggle smoke runner against a private verified dataset.
- Extracted one verified 11,125x2,048 frozen ResNet-50 cache and ran E0/E1/E3 with identical split, seed, visual features, budget, and validation-only checkpoint selection.
- E1 improves test SRCC by 0.00565 and MAE by 0.1547 over E0 in this one seed. E3 is below E1 at full metadata.
- Evaluated 0/25/50/100% record-level metadata missingness with five fixed stochastic masks at 25/50%; E3 dropout gives no measured robustness advantage.
- Completed matched E2 gated and E4 gated-plus-dropout runs. E2 test SRCC/PLCC/MAE is 0.83602/0.83779/9.1179; E4 is 0.83208/0.83337/9.3265.
- Extended missingness evaluation to all metadata models; E2 falls to 0.83290 SRCC and E4 to 0.82813 at zero available EXIF.
- Completed 10,000-resample paired inference: E1-E0 SRCC delta 0.00565 [0.00132, 0.01013]; all E2-E1 metric intervals cross zero.
- Completed train-defined high-ISO (n=235), long-exposure (n=316), and night-scene (n=191) analysis, deterministic top-error audit, and seven hashed figures.
- Completed README, experiment report, Kaggle runbook, acceptance audit, and automated release validation. Sixteen tests and dependency checks pass.
- Established Kaggle OAuth and uploaded the verified compact dataset privately. Kaggle expanded the tar into 11,125 images; v2 verifies the deterministic tree hash of the exact 300-image smoke sample.
- Kaggle v1 timed out during the overly broad full-tree integrity scan. Controlled v2 verified the exact 300-image smoke sample, completed on Tesla T4, and produced downloaded/hash-verified checkpoint, summary, and log artifacts.

## Last operation, command and result

- Last operation: downloaded Kaggle v2 outputs to `artifacts/kaggle_download/v2`; checkpoint SHA-256 `a7c69a6e...b487f` matches the remote summary.

## Failed/blocked steps

- `python --version` resolves to a nonfunctional Windows Store alias; use `py`.
- `gh` is absent and no Git remote exists; publication is optional.
- Source row `03461.jpg` contains exposure `1,000,000`, while embedded exposure is invalid/non-finite. Never invent a replacement; retain the author's distinct APEX shutter value with provenance.

## Data provenance and frozen split references

- Q-Align archive SHA-256: `d312242f10af983d5ceaac433c76b7c2b3473e2a2f87782f9db8ee1537dc2194`.
- Flattened metadata SHA-256: `17d4eaedeff3c2724b8f6fee9f9dbfef65ac8824bd31b774760d86b53a719e8f`.
- Canonical manifest exact join: 11,125/11,125; SHA-256 `abff8b1a...5800d`.
- Frozen split SHA-256 `91a8d1b2...a108`; train/val/test 7,786/1,111/2,228.

## Exact next commands

1. No required research work remains.
2. If desired, install/authenticate `gh` and create a private remote.
3. Keep Kaggle dataset/kernel private unless visibility change is explicitly requested.

## Warnings

- Do not report paper metrics as project results.
- Do not accept the Hugging Face archive license as proof of underlying SPAQ image rights.
- Do not use `topiq_nr-spaq` as an unseen SPAQ comparator.

