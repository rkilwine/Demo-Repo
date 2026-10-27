## Synthetic demo change

- ClickUp story: CU-868mnhw6a (FMR-WRK-231)
- Rounding defect: CU-868mnhw8a (FMR-WRK-232)
- Scope and business outcome:

## Acceptance and evidence

- AC1 short wording: unit check only; actual approval pending.
- AC2 consistent half-up totals: regression and fixture results.
- AC3 accessibility: not implemented in this CLI; manual frontend testing pending.
- AC4 configuration: external JSON reload test; hosted distribution not included.
- Latest head SHA:
- Actual test run link/result:
- Earlier failing regression run:
- Independent reviewer decision: pending (author notes are not approval).

## Risk and rollback

Synthetic data only. Hide explanations with the CLI flag; do not treat that as a monetary-logic rollback. See `docs/rollout-runbook.md`.

## Human decision

No deployment or merge implied. Keep release approval separate from CI and code review.
