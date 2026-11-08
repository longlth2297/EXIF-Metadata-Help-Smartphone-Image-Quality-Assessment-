# PROJECT STATUS

**Updated UTC:** 2026-11-08T19:58:25Z  
**Phase:** Phase 1 — data acquisition and verified data contract (G1)  
**Last successful gate:** G0  
**Git commit / remote:** `2297c0539e14056182f40dbbada4054b79bbb5ea` / NONE  
**Kaggle kernel/version/status:** NONE / Kaggle CLI 2.2.5 installed, authentication absent

## Current objective

Verify SPAQ images and original annotations, establish a trustworthy row-level contract, and freeze a leakage-audited split before model work.

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

## Current task

- G1-002: verify the author-recommended 34.8 GB archive and cross-check its original annotation workbooks against the flattened metadata CSV.

## Actual blockers

- Kaggle execution requires user OAuth outside tracked files; the CLI reports `Authentication required`.
- GitHub remote creation currently requires installing/authenticating `gh` or configuring another safe authenticated route.
- Q-Align images are re-encoded JPEGs without embedded EXIF. Original workbooks are being recovered to validate the flattened metadata provenance.

## Observed results

DATA CONTRACT IS PROVISIONALLY MATCHED BUT G1 IS NOT YET CLOSED. NO TRAINING OR MODEL EVALUATION HAS OCCURRED.

## Next actions

1. Complete, hash, and list `chaofengc/IQA-PyTorch-Datasets/spaq.tgz` without extraction.
2. Verify original annotation schemas/rows against the flattened CSV and resolve the exposure-time outlier.
3. Freeze a 70/10/20 project split only after duplicate and group-risk audit.

## Relevant evidence and file paths

- `evidence/q_align_spaq_archive.json`
- `evidence/spaq_qalign_join_audit.json`
- `docs/DATASET_RECOVERY.md`
- `docs/SOURCE_AUDIT.md`
- `EVIDENCE_LOG.md`

