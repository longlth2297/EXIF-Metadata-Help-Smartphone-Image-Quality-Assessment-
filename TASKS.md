# TASKS

Legend: `TODO`, `IN_PROGRESS`, `DONE`, `FAILED`, `BLOCKED`, `NOT_APPLICABLE`. Every completed task cites real evidence.

## Phase 0 — repository and source audit

- [x] **G0-001 DONE** Read controlling documents and audit primary papers/repositories/data endpoints. Evidence: `docs/SOURCE_AUDIT.md`, pinned SHAs in `EVIDENCE_LOG.md`.
- [x] **G0-002 DONE** Create repository, durable state ledger, test runner skeleton, and initial clean commit. Evidence: commit `2297c0539e14056182f40dbbada4054b79bbb5ea`.
- [x] **G0-003 DONE** Probe Python/Git/GPU/GitHub/Kaggle without exposing secrets. Evidence: `EVIDENCE_LOG.md`; Kaggle CLI 2.2.5 installed, auth absent.

## Phase 1 — data and provenance

- [x] **G1-001 DONE** Retrieved both compact and author-recommended archives; verified hashes, 11,125 original images, and three authentic workbooks. Evidence: `evidence/q_align_spaq_archive.json`, `evidence/iqa_pytorch_spaq_archive.json`.
- [x] **G1-002 DONE** Audited schemas, joins, embedded EXIF, per-field provenance, duplicates, terms, and preprocessing differences. Evidence: `evidence/spaq_original_workbook_audit.json`, `evidence/spaq_embedded_exif_audit.json`, `data/provenance.json`.
- [x] **G1-003 DONE** Frozen seed-20261109 group-safe split; 1,069 candidate edges cross zero partitions. Manifest SHA-256 `abff8b1a...5800d`; contract tests pass. Evidence: `data/manifest.parquet`, `evidence/spaq_split_seed20261109_audit.json`.

## Phase 2 — vertical slice and compute smoke

- [x] **G2-001 DONE** Ran 16-image ResNet-50 forward/backward, 20 updates, atomic checkpoint, bit-exact reload evaluation, optimizer resume, and four-image overfit sanity; 12 tests pass. Evidence: `evidence/g2_vertical_slice.json`, `evidence/g2_tiny_overfit.json`.
- [ ] **G2-002 BLOCKED** Run Kaggle smoke with GPU, 300-sample timing, 20 train steps, VRAM, checkpoint resume, output retrieval, and runtime projection. Blocker: CLI/auth not yet established. Runnable preparation proceeds offline.

## Phase 3 — matched baselines

- [ ] **G3-001 IN_PROGRESS** Execute E0 image-only training and persist predictions/checkpoint/logs. Frozen split and local measured CUDA path are ready.
- [ ] **G3-002 TODO** Execute matched E1 additive EXIF training and persist artifacts.

## Phase 4 — controlled extensions

- [ ] **G4-001 TODO** Execute E3 additive plus metadata dropout (MVR priority).
- [ ] **G4-002 TODO** Execute E2 gated fusion matched ablation.
- [ ] **G4-003 TODO** Execute E4 gated plus dropout matched ablation.

## Phase 5 — analysis

- [ ] **G5-001 TODO** Missingness curves, justified capture-condition groups, paired bootstrap, error analysis, and figures.

## Phase 6 — deliverable

- [ ] **G6-001 TODO** Clean reproduction commands, report, acceptance audit, artifact hashes, safe remote push, and final handoff.

