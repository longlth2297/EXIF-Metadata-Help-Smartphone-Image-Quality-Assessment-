# DECISIONS — append only

## D-0001 — 2026-11-08 — Separate documentary and execution evidence

- **Decision:** Use the statuses `PAPER_REPORTED`, `DOCUMENT_VERIFIED`, `EXECUTION_VERIFIED`, `ESTIMATED`, `UNVERIFIED`, and `FAILED` for claims.
- **Reason:** The handoff contains proposals and literature results but no executed project data or training.
- **Alternatives rejected:** Treating paper values or archive listings as local results.
- **Evidence:** `AGENTS.md`; `research_sources/CODEX_MASTER_PROMPT.md`.

## D-0002 — 2026-11-08 — Create a new isolated repository

- **Decision:** Initialize `spaq-exif-robustness/` rather than modifying the handoff package.
- **Reason:** The workspace had no existing Git repository, and the controlling prompt explicitly prefers an isolated project folder.
- **Evidence:** environment preflight and Git initialization output.

## D-0003 — 2026-11-08 — Keep the study scope locked

- **Decision:** Core sequence is E0/E1, then E3 for minimum viable research, followed by E2/E4 when gates and measured budget allow. PrISM pseudo-labels are excluded from the core scope.
- **Reason:** Preserves causal contrasts and avoids an unverified label dependency.
- **Evidence:** research reports and acceptance criteria.

