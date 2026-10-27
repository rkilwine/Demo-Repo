# Design: fee explanations and consistent totals

Synthetic internal demo. Linked ClickUp story: CU-868mnhw6a. Defect: CU-868mnhw8a.

## Boundary and data flow

Synthetic fixture -> validate decimal strings -> shared half-up rounding per line -> sum displayed lines -> attach runtime glossary text -> emit JSON. No external service, storage, authentication, or UI.

## Decisions

- Decimal strings avoid binary floating-point ambiguity. Reject floats, nonfinite values, negatives, excess precision, more than 100 lines, and amounts above the demo limit.
- `src.money.round_cents` is the shared helper. The fixed total sums displayed rounded lines, not raw inputs.
- Glossary is configuration with a version, short explanation, and explicit synthetic review state. Changing the external JSON file requires no Python source change. Real publishing and approval controls are not implemented.
- The `--hide-explanations` flag demonstrates rollback of explanation display only. It does not roll back monetary logic.
- Use only the three scoped fee types. This is display logic, not a billing or fee-calculation engine.

## Known gaps

AC3 keyboard and screen-reader behavior requires a real frontend and manual assistive-technology testing. AC1 wording approval is open; synthetic word-count tests do not establish compliance approval. AC4 proves file-based runtime configuration only, not an enterprise configuration distribution system. No independent reviewer, UAT, staging, deployment, performance, or security approval is claimed.

## Traceability

Branch/PR/commit references use real ClickUp task IDs CU-868mnhw6a and CU-868mnhw8a. These references must be observed on the ClickUp task before integration sync is claimed. Repo existence alone proves neither sync nor release readiness.
