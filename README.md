# SPAQ EXIF Robustness

Research repository for **When Does EXIF Metadata Help Smartphone Image Quality Assessment? A Controlled Study of Fusion, Missingness, and Capture-Condition Shift**.

## Status

Phase 0 is in progress. No dataset has yet been accepted, no training has occurred, and no project metric is available. Paper-reported values in the source documents are literature references, not results from this repository.

The primary task is to compare matched SPAQ MOS predictors: E0 image-only, E1 additive EXIF, E2 gated EXIF, E3 additive plus metadata dropout, and E4 gated plus metadata dropout. SRCC is primary; PLCC, MAE, RMSE, paired contrasts, missingness stress, and uncertainty are secondary analyses.

## Integrity rules

- Raw images, credentials, restricted weights, and unverified labels are never committed.
- Dataset joins and EXIF fields must be verified from acquired files.
- Train-only preprocessing and fixed split manifests are mandatory.
- Literature metrics are labeled `PAPER_REPORTED`; executed results are labeled `EXECUTION_VERIFIED`.
- Pretrained TOPIQ inference is an external comparator, not a reproduction of TOPIQ training.

## Persistent state

Start every session with `AGENTS.md`, `PROJECT_STATUS.md`, `STATE.json`, `TASKS.md`, `EXPERIMENTS.csv`, and `SESSION_HANDOFF.md`. Source decisions and execution claims are tracked in `DECISIONS.md` and `EVIDENCE_LOG.md`.

## Current next command

See `STATE.json` and `SESSION_HANDOFF.md`; these are updated after each material action.

