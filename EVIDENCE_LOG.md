# EVIDENCE LOG — append only

| UTC | Claim | Status | Evidence / command | Artifact |
|---|---|---|---|---|
| 2026-11-08T19:46:21Z | Handoff source files are intact | EXECUTION_VERIFIED | `Get-FileHash -Algorithm SHA256 ...`; eight hashes match `PACKAGE_MANIFEST.md` | Source console log; hashes will be retained in `evidence/environment_preflight.txt` |
| 2026-11-08T19:46:21Z | Workspace parent was not a Git repository | EXECUTION_VERIFIED | `git -C .. status --short --branch` returned fatal not-a-repository | `evidence/environment_preflight.txt` |
| 2026-11-08T19:46:21Z | Local Git is 2.50.1 and repository initialized on `main` | EXECUTION_VERIFIED | `git --version`; `git init -b main` | `.git/` |
| 2026-11-08T19:46:21Z | Python 3.13.5 is available via `py`; `python` alias failed | EXECUTION_VERIFIED | `py --version`; `python --version` | `evidence/environment_preflight.txt` |
| 2026-11-08T19:46:21Z | Local RTX 4050 Laptop GPU exposes 6141 MiB VRAM | EXECUTION_VERIFIED | `nvidia-smi` | `evidence/environment_preflight.txt` |
| 2026-11-08T19:46:21Z | GitHub and Kaggle CLIs are absent from PATH | EXECUTION_VERIFIED | `gh --version`; `kaggle --version` | `evidence/environment_preflight.txt` |
| 2026-11-08T19:46:21Z | No project training or evaluation has occurred | EXECUTION_VERIFIED | Empty new repository and run registry | `EXPERIMENTS.csv` |
| 2026-11-08T19:48:22Z | Official upstream revisions pinned | EXECUTION_VERIFIED | `git ls-remote`: SPAQ `03e2b1c752b593079afffc2adb6ffff4c76e376e`; IQA-PyTorch `d47b7ac72ed25388371d0b637076c125cdb95a3c` | `docs/SOURCE_AUDIT.md` |
| 2026-11-08T19:53:29Z | SPAQ owner replaced broken Drive source with `chaofengc/IQA-PyTorch-Datasets/spaq.tgz` | DOCUMENT_VERIFIED | `h4nwei/SPAQ` issue #38, owner comment dated 2026-03-11 | `docs/DATASET_RECOVERY.md` |
| 2026-11-08T19:55:18Z | Q-Align archive integrity and images verified | EXECUTION_VERIFIED | 2,626,897,920 bytes; SHA-256 `d312242f...2194`; 11,125/11,125 JPEGs readable; zero embedded EXIF | `evidence/q_align_spaq_archive.json` |
| 2026-11-08T19:57:22Z | Q-Align images join exactly to IQA-PyTorch SPAQ metadata | EXECUTION_VERIFIED | 11,125 unique keys matched, zero orphans/collisions; metadata SHA-256 `17d4eaed...9e8f` | `evidence/spaq_qalign_join_audit.json` |
| 2026-11-08T19:57:22Z | Flattened metadata includes complete MOS, attributes, scene fields, and EXIF columns | EXECUTION_VERIFIED | Read all 11,125 CSV rows and 35 columns; no nulls | `evidence/spaq_qalign_join_audit.json` |
| 2026-11-08T19:57:22Z | One exposure-time value is a material outlier (`1,000,000`) | EXECUTION_VERIFIED | Row `03461.jpg`; next maximum is `0.5`; raw workbook validation pending | `evidence/spaq_qalign_join_audit.json` plus targeted query |
| 2026-11-08T19:58:25Z | Kaggle remote execution unavailable in current auth state | EXECUTION_VERIFIED | Kaggle CLI 2.2.5 `kernels list -m` returned `Authentication required` | `STATE.json` |
| 2026-11-08T19:58:25Z | G0 repository bootstrap checkpoint committed | EXECUTION_VERIFIED | Git commit `2297c0539e14056182f40dbbada4054b79bbb5ea` | Git history |
| 2026-11-08T20:05:51Z | Q-Align SPAQ contains 322 byte-identical image pairs | EXECUTION_VERIFIED | Full SHA-256 per-image audit: 644 files in 322 size-two groups | `evidence/q_align_duplicate_audit.json` |
| 2026-11-08T20:05:51Z | Exact duplicates have conflicting subjective labels and inherited split leakage | EXECUTION_VERIFIED | 321/322 pairs differ in MOS (mean absolute difference 7.75, maximum 31.66); all pairs agree on all EXIF fields; Q-Align split separates 103 pairs | `evidence/q_align_duplicate_label_audit.json` |
| 2026-11-08T20:27:24Z | Author-recommended SPAQ archive integrity and structure verified | EXECUTION_VERIFIED | 34,841,101,349 bytes; SHA-256 `54e0cb49...7418f7`; 11,125 unique JPEGs; three XLSX files; 35,476,869,087 uncompressed bytes | `evidence/iqa_pytorch_spaq_archive.json` |
| 2026-11-08T20:27:16Z | Original workbooks reproduce flattened annotations exactly | EXECUTION_VERIFIED | 11,125 IDs; zero identifier/value mismatches across 24 columns | `evidence/spaq_original_workbook_audit.json` |
| 2026-11-08T20:33:01Z | Embedded EXIF provenance verified for every original image | EXECUTION_VERIFIED | 11,125 JPEGs; brightness observed 8,546 / author-estimated 2,579; compared exposures all match | `evidence/spaq_embedded_exif_audit.json` |
| 2026-11-08T20:34:45Z | Canonical manifest and group-safe split frozen | EXECUTION_VERIFIED | 11,125 rows; SHA-256 `abff8b1a...5800d`; 7,786/1,111/2,228 split; zero edge crossings; 10 tests pass | `data/manifest.parquet`, `evidence/spaq_manifest_audit.json` |
| 2026-11-08T20:35:43Z | Supported local CUDA environment works | EXECUTION_VERIFIED | Python 3.12.10, torch 2.14.1+cu130, torchvision 0.29.1+cu130; RTX 4050 matrix multiplication completed | `PROJECT_STATUS.md` |
| 2026-11-08T20:42:28Z | Real-image model vertical slice and checkpoint resume succeeded | EXECUTION_VERIFIED | ResNet-50, 16 SPAQ images, 20 updates in 2.98 s; 1.20 GB peak; checkpoint predictions bit-exact after reload; step 21 resumed | `evidence/g2_vertical_slice.json` |
| 2026-11-08T20:43:26Z | Tiny real-image subset can overfit | EXECUTION_VERIFIED | Four images, 200 updates; L1 54.29 to 1.49 (minimum 0.17); SRCC 1.0 is resubstitution sanity only | `evidence/g2_tiny_overfit.json` |
| 2026-11-08T20:45:03Z | Kaggle smoke is packaged but remote execution remains auth-blocked | EXECUTION_VERIFIED | Standalone runner records 300-image IO/inference, 20 steps, GPU/disk/VRAM, checkpoint/reload; CLI still reports authentication required | `kaggle/kernel/run_smoke.py`, `STATE.json` |
| 2026-11-08T20:49:26Z | Frozen ResNet-50 feature cache extracted over every SPAQ row | EXECUTION_VERIFIED | 11,125x2,048 float32; SHA-256 `b639bb6f...975ed`; 119.76 s total; 92.89 images/s; 296 MB peak | `evidence/feature_cache_resnet50.json` |
| 2026-11-08T20:51:45Z | E0 image-only resource-adapted baseline completed | EXECUTION_VERIFIED | Best epoch 52 by validation; test SRCC/PLCC/MAE 0.83048/0.83063/9.3489 | `evidence/e0_frozen_r50_s20261109.json` |
| 2026-11-08T20:52:10Z | E1 additive EXIF matched run completed | EXECUTION_VERIFIED | 16 additional parameters; test SRCC/PLCC/MAE 0.83613/0.83572/9.1942 | `evidence/e1_frozen_r50_s20261109.json` |
| 2026-11-08T20:52:31Z | E3 additive EXIF plus 50% metadata dropout completed | EXECUTION_VERIFIED | Test SRCC/PLCC/MAE 0.83450/0.83452/9.2534 | `evidence/e3_frozen_r50_s20261109.json` |
| 2026-11-08T20:53:54Z | E1/E3 missingness curves executed on identical test IDs | EXECUTION_VERIFIED | Five fixed masks at 25/50%; E1 SRCC 0.83613→0.83579 and E3 0.83450→0.83432 from 0→100% missing; dropout gave no robustness advantage | `evidence/missingness_e1_e3_s20261109.json` |
| 2026-11-09T04:31:47Z | E2 gated EXIF matched run completed | EXECUTION_VERIFIED | 8,704 metadata parameters; best epoch 45; test SRCC/PLCC/MAE 0.83602/0.83779/9.1179 | `evidence/e2_frozen_r50_s20261109.json` |
| 2026-11-09T04:31:47Z | E4 gated EXIF plus 50% metadata dropout completed | EXECUTION_VERIFIED | Best epoch 37; test SRCC/PLCC/MAE 0.83208/0.83337/9.3265 | `evidence/e4_frozen_r50_s20261109.json` |
| 2026-11-09T04:31:47Z | Missingness curves executed for E1/E2/E3/E4 on identical test IDs | EXECUTION_VERIFIED | E2 SRCC 0.83602→0.83290 and E4 0.83208→0.82813 from 0→100% missing; dropout did not improve gated robustness | `evidence/missingness_all_s20261109.json` |

