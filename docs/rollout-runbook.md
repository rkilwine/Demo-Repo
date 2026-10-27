# Demo rollout and rollback runbook

No deployment is included. These are rehearsal steps, not production instructions.

## Preflight

1. Use only this synthetic repo/branch. Confirm current PR head and observed tests.
2. Confirm glossary is labeled synthetic and actual wording approval is not claimed.
3. Review the open gates in `release-checklist.md`.
4. Keep the PR open and leave `main` unchanged during rehearsal.

## Rehearse locally

```sh
python3 -m unittest discover -s tests -v
python3 -m src.fee_breakdown --case normal
python3 -m src.fee_breakdown --case half-cent
python3 -m src.fee_breakdown --case zero
```

## Roll back explanation display

```sh
python3 -m src.fee_breakdown --case half-cent --hide-explanations
```

Expect explanations to be null, status hidden, and the fixed total still 15.69. This flag changes only the local invocation; no remote system is affected. It is not a substitute for reverting a money defect.

## Runtime wording update

Provide a separately reviewed synthetic JSON file with `--glossary path/to/glossary.json`. Re-run glossary tests and the relevant scenario. The demo proves configuration loading, not an enterprise publishing pipeline.

## Stop conditions

Stop a release-readiness claim on failing latest-head tests, unresolved wording review, missing independent review, or missing accessibility/UAT evidence. Assign the next action in ClickUp through the normal human process. No release approval, status automation, or deployment is performed by this runbook.
