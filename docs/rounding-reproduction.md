# Reproduce the half-cent defect

Synthetic display defect, not a live account incident. ClickUp: CU-868mnhw8a / FMR-WRK-232.

## Inputs and expected behavior

Advisory fee `12.345`, fund expense `3.335`, transaction fee `0.00`. Half-up displayed lines are `12.35`, `3.34`, and `0.00`; expected total is `15.69`.

The staged broken version rounds the raw total, yielding `15.68`. It is deliberately committed before the fix so the regression can be observed. Decimal is used even in the staged version to make the one-cent mismatch reproducible, rather than relying on platform-sensitive float examples.

```sh
python3 -m unittest discover -s tests -p test_fee_breakdown.py -v
python3 -m src.fee_breakdown --case half-cent
```

## Correct fix

Keep shared `round_cents` with `ROUND_HALF_UP`; sum the rounded display amounts for the total. The named regression is `test_half_cent_boundary_total_matches_lines`.

## Evidence to retain

Use GitHub Actions run links for the broken and fixed commits. Check that the red run failed specifically on the 15.68/15.69 assertion. A queued run, inaccessible log, syntax error, or missing runner is not evidence of this defect. Do not revert the fix just to make the demo red again; inspect the earlier commit/run.
