# PROJECT STATUS

**Updated UTC:** 2026-11-08T20:35:43Z
**Phase:** Phase 2 — minimum vertical slice and compute smoke (G2)
**Last successful gate:** G1
**Git commit / remote:** `a07407879426af1ece25bcfb68ffea5669b6b66d` / NONE
**Kaggle kernel/version/status:** NONE / Kaggle CLI 2.2.5 installed, authentication absent

## Current objective

Run the 16-real-image forward/backward/checkpoint/reload/evaluation slice, then package the measured Kaggle smoke runner and execute it when authentication is available.

## Execution-verified achievements

- Handoff package hashes match `PACKAGE_MANIFEST.md` for all eight controlling/source documents checked.
- Local Git 2.50.1 is available and a `main` repository was initialized.
- Python 3.13.5 is available through `py`; the `python` alias is not usable.
- Local NVIDIA RTX 4050 Laptop GPU is visible with 6141 MiB VRAM; this is not Kaggle evidence.
- `gh` is not installed. Kaggle CLI 2.2.5 is installed and its read-only account probe confirmed authentication is absent.
- Q-Align `spaq.tar` downloaded: 2,626,897,920 bytes; SHA-256 matches the Hugging Face linked ETag.
- The archive contains exactly 11,125 unique, readable JPEGs and no annotation files; none contains embedded EXIF.
- IQA-PyTorch's pinned metadata release has 11,125 unique SPAQ rows with MOS, attributes, scene annotations, EXIF-derived columns, and no nulls.
- Exact filename join between that CSV and Q-Align archive is 11,125/11,125 with no orphans or collisions.
- A full byte-hash audit found 322 exact duplicate pairs (644 files). All 322 have conflicting annotation fields; 321 have different MOS, while all eight EXIF-derived fields agree within every pair. The inherited Q-Align split separates 103 pairs, so it is not acceptable for this project.
- Author-recommended `spaq.tgz` is 34,841,101,349 bytes; SHA-256 `54e0cb49...7418f7` matches its LFS object. It contains 11,125 originals and three workbooks.
- All 11,125 workbook IDs and 24 MOS/attribute/scene/source-EXIF values match the flattened mirror exactly.
- Embedded EXIF was audited for all originals: scene brightness is observed for 8,546 rows and author-estimated for 2,579.
- The frozen split groups all 1,069 repeated-content edges: 7,786/1,111/2,228 rows and zero edge crossings.
- Canonical `data/manifest.parquet` has 11,125 rows and SHA-256 `abff8b1a...5800d`.
- Python 3.12.10/PyTorch 2.14.1+cu130 completed a CUDA operation on the RTX 4050; ten tests pass.

## Current task

- G2-001: extract the verified compact image variant and run the real-image vertical slice with checkpoint reload and predictions.

## Actual blockers

- Kaggle execution requires user OAuth outside tracked files; the CLI reports `Authentication required`.
- GitHub remote creation currently requires installing/authenticating `gh` or configuring another safe authenticated route.

## Observed results

G1 IS EXECUTION-VERIFIED AND CLOSED. NO MODEL TRAINING RESULT EXISTS YET; only a CUDA arithmetic smoke has run.

## Next actions

1. Extract the 2.63 GB Q-Align image archive locally and validate the canonical loader against real images.
2. Run 16-image forward/backward/checkpoint/reload/evaluation plus tiny-overfit sanity.
3. Prepare the idempotent Kaggle smoke bundle and retain `BLOCKED_ON_USER_AUTH` until OAuth succeeds.

## Relevant evidence and file paths

- `evidence/q_align_spaq_archive.json`
- `evidence/spaq_qalign_join_audit.json`
- `evidence/q_align_duplicate_audit.json`
- `evidence/q_align_duplicate_label_audit.json`
- `evidence/iqa_pytorch_spaq_archive.json`
- `evidence/spaq_original_workbook_audit.json`
- `evidence/spaq_embedded_exif_audit.json`
- `evidence/spaq_manifest_audit.json`
- `docs/DATASET_RECOVERY.md`
- `docs/SOURCE_AUDIT.md`
- `EVIDENCE_LOG.md`

