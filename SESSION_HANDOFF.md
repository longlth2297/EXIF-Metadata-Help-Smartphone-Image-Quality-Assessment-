# SESSION HANDOFF

**Updated UTC:** 2026-11-08T20:35:43Z
**Repo path/commit:** `D:\HCMUS\Year2\Scientific Method\SC\spaq-exif-robustness` / `a07407879426af1ece25bcfb68ffea5669b6b66d`
**Most advanced completed gate:** G1
**Active Kaggle kernel/version/status:** NONE / BLOCKED_ON_USER_AUTH  
**Last valid checkpoint:** NONE

## Verified completed tasks

- Read all controlling local documents and both research reports.
- Verified the handoff package hashes against its manifest.
- Initialized the project repository and durable progress ledger; committed the G0/recovery milestone.
- Installed Kaggle CLI 2.2.5; account probe proves auth is absent.
- Downloaded and verified Q-Align `spaq.tar`: 11,125 readable JPEGs, no annotations or embedded EXIF.
- Retrieved pinned IQA-PyTorch metadata and matched all 11,125 rows to archive filenames with no orphans/collisions.
- Hashed every Q-Align image and identified 322 exact duplicate pairs. All pairs conflict on at least one subjective field, 321 conflict on MOS, all agree on EXIF, and 103 cross the Q-Align train/test boundary.
- Downloaded and hash-verified the 34.8 GB author-recommended archive; streamed it without full extraction and recovered the original workbooks.
- Proved exact 11,125-row workbook/mirror equality and audited embedded EXIF for every original JPEG.
- Froze the repeated-content-grouped split and built `data/manifest.parquet` with observed/estimated masks.
- Installed `.venv312`; local RTX 4050 CUDA operation and 10 tests pass.

## Last operation, command and result

- Last operation: built canonical manifest SHA-256 `abff8b1a5f7d2e74d0c8874655fbe40d5e75de75bf61e65753c7085cee15800d` and passed 10 tests.

## Failed/blocked steps

- `python --version` resolves to a nonfunctional Windows Store alias; use `py`.
- `gh` is absent. Kaggle auth is absent; user OAuth is required before remote smoke execution.
- Source row `03461.jpg` contains exposure `1,000,000`, while embedded exposure is invalid/non-finite. Never invent a replacement; retain the author's distinct APEX shutter value with provenance.

## Data provenance and frozen split references

- Q-Align archive SHA-256: `d312242f10af983d5ceaac433c76b7c2b3473e2a2f87782f9db8ee1537dc2194`.
- Flattened metadata SHA-256: `17d4eaedeff3c2724b8f6fee9f9dbfef65ac8824bd31b774760d86b53a719e8f`.
- Canonical manifest exact join: 11,125/11,125; SHA-256 `abff8b1a...5800d`.
- Frozen split SHA-256 `91a8d1b2...a108`; train/val/test 7,786/1,111/2,228.

## Exact next commands

1. Extract `data/raw/q_align/spaq.tar` to ignored local storage.
2. Run the 16-image model vertical slice using `.venv312`.
3. Persist checkpoint/reload proof, predictions, metrics, timing, GPU peak memory, and hashes.
4. Package Kaggle smoke runner; authentication remains `BLOCKED_ON_USER_AUTH`.

## Warnings

- Do not report paper metrics as project results.
- Do not accept the Hugging Face archive license as proof of underlying SPAQ image rights.
- Do not use `topiq_nr-spaq` as an unseen SPAQ comparator.

