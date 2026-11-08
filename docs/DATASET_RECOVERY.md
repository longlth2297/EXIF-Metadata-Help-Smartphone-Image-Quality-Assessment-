# SPAQ dataset recovery

## Author-confirmed source change

The original Google Drive folder returns HTTP 404. In `h4nwei/SPAQ` issue #38, opened 2026-01-16, repository owner `h4nwei` responded on 2026-03-11 with the replacement `chaofengc/IQA-PyTorch-Datasets/spaq.tgz` archive on Hugging Face. The broken Drive link will not be retried.

## Candidate A — Q-Align `spaq.tar`

- Repository: `q-future/q-align-datasets`
- Revision observed in response header: `3da8831b98d683a024b1216720df0cc8a832e376`
- URL: `https://huggingface.co/datasets/q-future/q-align-datasets/resolve/main/spaq.tar`
- Advertised/object bytes: `2,626,897,920`
- Hugging Face linked ETag: `d312242f10af983d5ceaac433c76b7c2b3473e2a2f87782f9db8ee1537dc2194`
- Downloaded SHA-256: `d312242f10af983d5ceaac433c76b7c2b3473e2a2f87782f9db8ee1537dc2194`
- Members: one directory plus 11,125 unique `.jpg` files; no tables or other files.
- Status: archive integrity and member count verified; full image readability/dimension/embedded-EXIF audit in progress.
- License warning: the repository card says MIT, but this does not establish that underlying SPAQ images or annotations are MIT-licensed.

## Candidate B — author-recommended `spaq.tgz`

- Repository: `chaofengc/IQA-PyTorch-Datasets`
- Revision observed in response header: `f97c4f5dbdbdea7039bc9b80db808313347b1bef`
- URL: `https://huggingface.co/datasets/chaofengc/IQA-PyTorch-Datasets/resolve/main/spaq.tgz`
- Advertised/object bytes: `34,841,101,349` (32.45 GiB)
- Hugging Face linked ETag: `54e0cb49dc8359f9293e746d452d8b12ec653056c9b12a4f97798a984c7418f7`
- Repository card license: CC-BY-SA-4.0; applicability to every underlying SPAQ asset still requires caution.
- Local D: drive free before download: 227,981,836,288 bytes. The archive will be listed without extraction first. It is not suitable for Kaggle's documented 20 GB saved working directory as a monolithic uploaded/extracted asset.

## Gate rule

The EXIF data gate remains open until real images, MOS, and usable EXIF rows are matched using observed identifiers with coverage and collision checks. Missing annotation types will not be synthesized.

## Duplicate and leakage audit

Every JPEG payload in the Q-Align archive was SHA-256 hashed. There are 322 exact duplicate groups, each containing two filenames. These are not duplicate annotation rows: 321 pairs have different MOS values and all 322 differ in at least one subjective quality or scene field. Conversely, all eight EXIF-derived columns are identical within every exact pair. The Q-Align train/test field separates 103 exact pairs, and the ten legacy 80/20 fields separate 86--120 pairs each. Those inherited splits are therefore rejected for this study. The project split must treat each exact pair as a single group.

The 64-bit dHash audit also produced 747 non-exact candidate pairs within Hamming distance four. dHash collisions can be visually unrelated, so these candidates are not automatically declared duplicates; representative visual review and/or a stronger feature audit is required before adding them to grouping constraints.

Evidence: `evidence/q_align_duplicate_audit.json` and `evidence/q_align_duplicate_label_audit.json`.

