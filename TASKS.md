# TASKS

Legend: `TODO`, `IN_PROGRESS`, `DONE`, `FAILED`, `BLOCKED`, `NOT_APPLICABLE`. Every completed task cites real evidence.

## Phase 0 — repository and source audit

- [x] **G0-001 DONE** Read controlling documents and audit primary papers/repositories/data endpoints. Evidence: `docs/SOURCE_AUDIT.md`, pinned SHAs in `EVIDENCE_LOG.md`.
- [ ] **G0-002 IN_PROGRESS** Create repository, durable state ledger, test runner skeleton, and initial clean commit. Evidence target: Git commit.
- [x] **G0-003 DONE** Probe Python/Git/GPU/GitHub/Kaggle without exposing secrets. Evidence: `EVIDENCE_LOG.md`; Kaggle CLI 2.2.5 installed, auth absent.

## Phase 1 — data and provenance

- [ ] **G1-001 IN_PROGRESS** Retrieve SPAQ images and authentic annotations. Q-Align images and IQA-PyTorch flattened metadata obtained; author-recommended original archive download active. Evidence: `docs/DATASET_RECOVERY.md`.
- [ ] **G1-002 IN_PROGRESS** Hash assets; audit schemas, joins, EXIF provenance, duplicates, and terms. Current: 11,125/11,125 join, no nulls/collisions; raw workbook cross-check pending. Evidence: `evidence/q_align_spaq_archive.json`, `evidence/spaq_qalign_join_audit.json`.
- [ ] **G1-003 TODO** Freeze leakage-audited splits and validate loader. Depends on G1-002.

## Phase 2 — vertical slice and compute smoke

- [ ] **G2-001 TODO** Run real-image forward/backward/checkpoint/reload/evaluation vertical slice and required unit tests. Depends on G1.
- [ ] **G2-002 BLOCKED** Run Kaggle smoke with GPU, 300-sample timing, 20 train steps, VRAM, checkpoint resume, output retrieval, and runtime projection. Blocker: CLI/auth not yet established. Runnable preparation proceeds offline.

## Phase 3 — matched baselines

- [ ] **G3-001 TODO** Execute E0 image-only training and persist predictions/checkpoint/logs.
- [ ] **G3-002 TODO** Execute matched E1 additive EXIF training and persist artifacts.

## Phase 4 — controlled extensions

- [ ] **G4-001 TODO** Execute E3 additive plus metadata dropout (MVR priority).
- [ ] **G4-002 TODO** Execute E2 gated fusion matched ablation.
- [ ] **G4-003 TODO** Execute E4 gated plus dropout matched ablation.

## Phase 5 — analysis

- [ ] **G5-001 TODO** Missingness curves, justified capture-condition groups, paired bootstrap, error analysis, and figures.

## Phase 6 — deliverable

- [ ] **G6-001 TODO** Clean reproduction commands, report, acceptance audit, artifact hashes, safe remote push, and final handoff.

