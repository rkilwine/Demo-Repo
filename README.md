# Advisor Portal Fee Breakdown: Synthetic Delivery Demo

**Demo only. Not a Fidelity application, compliance approval, deployment, or production architecture.** No clients, account IDs, credentials, external APIs, or money movement.

This repository demonstrates a traceable business request, implementation, rounding defect, regression test, and human review. Original repository files are preserved and are not part of the runnable example.

## Start here (no packages to install)

Python 3.10+ is required. Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 -m src.fee_breakdown --case normal
python3 -m src.fee_breakdown --case half-cent
python3 -m src.fee_breakdown --case zero --hide-explanations
```

On Windows, use `py` instead of `python3`. The example prints JSON, not a web page. Use the GitHub Actions tab to inspect actual test execution without installing anything.

## What to show

1. Find ClickUp story CU-868mnhw6a (FMR-WRK-231) and defect CU-868mnhw8a (FMR-WRK-232).
2. Open the task-linked branch and pull request.
3. Show the earlier failing test run and later fixed run, if both are actually available.
4. Show the feature flag hiding explanations without changing totals.
5. Ask the readiness advisor what evidence is still missing.

Never describe an unobserved check as passing. A passing unit suite is not human approval, accessibility validation, UAT, or deployment. The pull request stays open for review.

## Repository map

- `src/fee_breakdown.py`: service and command-line entry point.
- `src/money.py`: shared Decimal parsing and half-up rounding.
- `config/fee_glossary.json`: runtime-loaded synthetic wording and review states.
- `data/accounts.json`: normal, zero, and half-cent fixtures.
- `tests/`: fee totals, glossary/configuration, and input validation.
- `docs/presenter-script.md`: presenter walkthrough.
- `docs/test-map.md`: acceptance criteria and evidence gaps.
- `docs/design.md`: decisions and limitations.
- `docs/rounding-reproduction.md`: reproduce the one-cent mismatch.
- `docs/release-checklist.md`: open human gates.
- `docs/rollout-runbook.md`: demo-only rollout and rollback.
- `.github/`: automated tests and PR template.

## Important limits

The glossary contains illustrative wording, not actual compliance-approved copy. `demo_reviewed` is a fictional demo state, not a real approval. `in_review` is intentionally unresolved. The JSON CLI has no keyboard or screen-reader interface to validate. Configuration can be read from a different file with `--glossary`; no content-distribution service is included. Nothing is deployed and no branch protection is asserted.
