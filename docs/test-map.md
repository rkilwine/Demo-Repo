# Acceptance criteria and evidence map

Story CU-868mnhw6a / FMR-WRK-231; defect CU-868mnhw8a / FMR-WRK-232.

| Criterion | Automated check | What it does not prove |
| --- | --- | --- |
| AC1: short, approved fee explanations | `test_all_supported_types_have_short_explanations` | Word count and presence only. Actual wording approval remains open. |
| AC2: displayed totals match half-up rounded lines | `test_half_cent_boundary_total_matches_lines`, fixture test, shared-helper test | No money movement, reconciliation, or production validation. |
| AC3: keyboard and screen-reader access | None | No frontend in this package. Manual accessibility testing remains required. |
| AC4: wording changes without code release | `test_external_configuration_changes_without_code_change` | External file loading only; no hosted configuration rollout or approval enforcement. |
| Input safety | `ValidationTests` | Not an application-security assessment. |
| Feature rollback | `test_feature_flag_hides_explanations` | Hides text only; not a deployed feature-flag system. |

## Evidence procedure

In GitHub Actions, open a run, record its head commit and result, and inspect the actual test log. Compare earlier failing regression evidence with the fixed commit. Never treat a URL alone or an older successful run as proof for newer code. A red workflow caused by infrastructure or syntax is not a valid rounding-regression demonstration.
