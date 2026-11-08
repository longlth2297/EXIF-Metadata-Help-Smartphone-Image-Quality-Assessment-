# SESSION HANDOFF

**Updated UTC:** 2026-11-08T19:58:25Z  
**Repo path/commit:** `D:\HCMUS\Year2\Scientific Method\SC\spaq-exif-robustness` / `2297c0539e14056182f40dbbada4054b79bbb5ea`  
**Most advanced completed gate:** G0  
**Active Kaggle kernel/version/status:** NONE / BLOCKED_ON_USER_AUTH  
**Last valid checkpoint:** NONE

## Verified completed tasks

- Read all controlling local documents and both research reports.
- Verified the handoff package hashes against its manifest.
- Initialized the project repository and durable progress ledger; committed the G0/recovery milestone.
- Installed Kaggle CLI 2.2.5; account probe proves auth is absent.
- Downloaded and verified Q-Align `spaq.tar`: 11,125 readable JPEGs, no annotations or embedded EXIF.
- Retrieved pinned IQA-PyTorch metadata and matched all 11,125 rows to archive filenames with no orphans/collisions.

## Last operation, command and result

- Active operation: resumable download of the 34,841,101,349-byte author-recommended `spaq.tgz` into ignored raw storage.

## Failed/blocked steps

- `python --version` resolves to a nonfunctional Windows Store alias; use `py`.
- `gh` is absent. Kaggle auth is absent; user OAuth is required before remote smoke execution.
- Flattened EXIF row `03461.jpg` has exposure time `1,000,000`; do not transform/impute until checked against the original workbook.

## Data provenance and frozen split references

- Q-Align archive SHA-256: `d312242f10af983d5ceaac433c76b7c2b3473e2a2f87782f9db8ee1537dc2194`.
- Flattened metadata SHA-256: `17d4eaedeff3c2724b8f6fee9f9dbfef65ac8824bd31b774760d86b53a719e8f`.
- Provisional filename join: 11,125/11,125. No project split exists yet.

## Exact next commands

1. Poll the active `spaq.tgz` download; resume with `curl -C -` if interrupted.
2. Hash and list the archive without extraction; locate original annotation workbooks.
3. Cross-check workbook schemas/rows and then run duplicate/group-risk audit before freezing splits.

## Warnings

- Do not report paper metrics as project results.
- Do not accept the Hugging Face archive license as proof of underlying SPAQ image rights.
- Do not use `topiq_nr-spaq` as an unseen SPAQ comparator.

