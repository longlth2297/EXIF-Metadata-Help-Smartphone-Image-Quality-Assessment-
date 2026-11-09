# Phase 7 experiment report

**Status:** EXECUTION IN PROGRESS  
**Preregistration:** `configs/phase7_experiments.json`  
**Preserved baseline:** tag `baseline-v0.1`

## Planned confirmatory analyses

1. E0/E1/E2 on seeds 20261109, 20261110, and 20261111 with unchanged cache, split, budget, and validation selection.
2. Correct-pair versus fixed-seed EXIF permutation for E1/E2.
3. Per-seed E1-E0 and E2-E1 contrasts on all test images and fixed high-ISO, long-exposure, and night subsets.

## Planned diagnostics

- Optics, exposure, flash, and time feature-group ablations.
- Missingness curves aggregated across training seeds.
- Controlled frozen-backbone versus layer4-fine-tuned ResNet-50 pair on Kaggle.

## Results through G7-005

All values below come from the frozen 2,228-image test partition. Model selection used validation SRCC only. The three training seeds were 20261109, 20261110, and 20261111.

| Preregistered comparison | Mean test delta SRCC | Seedwise result | Decision |
|---|---:|---|---|
| E1 additive EXIF - E0 image only | +0.001878 | +0.005649, -0.003524, +0.003508 | Small and not sign-consistent |
| E2 gated EXIF - E1 additive EXIF | -0.001317 | -0.000115, -0.000004, -0.003833 | H3 not supported |

For H1, mean E1-E0 SRCC was larger in high ISO (+0.009375), long exposure (+0.006292), and night (+0.009734) than over all test images (+0.001878). None was positive in all three seeds, so none met the registered conditional-utility rule. These subgroup associations are not causal effects.

For H2, intact correct-pair metadata exceeded the mean of five whole-record permutations by +0.000351 SRCC for E1 and +0.002593 for E2, with a positive contrast in all three training seeds. This meets the registered rule but the magnitude is small. It shows sensitivity to correct pairing, not that metadata is causally useful or robust outside SPAQ. Inference-only feature-group diagnostics identify exposure as the largest leave-out effect for E2; because models were not retrained, those diagnostics are not causal ablations.

H4, the matched frozen-versus-layer4-fine-tuned image-backbone comparison, remains in progress and will be run on Kaggle GPU. Stronger IQA baselines remain deferred until H4 is verified.

## Evidence index

- `evidence/phase7_multiseed_summary.json`: input prediction hashes, per-seed metrics, contrasts, registered H1/H3 decisions, and output hashes.
- `evidence/phase7_metadata_diagnostics.json`: checkpoint hashes, permutation/missingness seeds, registered H2 decisions, diagnostic limitations, and output hashes.
- `evidence/phase7_multiseed_metrics.csv`, `evidence/phase7_multiseed_contrasts.csv`, `evidence/phase7_metadata_diagnostic_metrics.csv`: machine-readable rows behind the summaries.
- `docs/figures/phase7_*.png`: generated views whose SHA-256 values are recorded in the summary JSON files.
