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

