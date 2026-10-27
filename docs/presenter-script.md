# Five-minute presenter walkthrough

Synthetic demo only. No production or compliance claims.

## 1. Business request (45 seconds)

Open ClickUp story FMR-WRK-231, task CU-868mnhw6a. Explain that clients need clear fee wording and a total that matches the displayed lines. Show the linked rounding defect CU-868mnhw8a.

## 2. Engineering traceability (45 seconds)

Open this branch's PR. Show the actual task IDs in the branch, commits, and PR body. Only say activity sync works after verifying the event on the correct ClickUp task.

## 3. Defect and regression (90 seconds)

Open the first completed regression run if available. The intended failure is expected 15.69 versus actual 15.68. Then show the fix diff and a successful run for the fixed head. If Actions is unavailable, use local execution and explicitly call it local evidence, not CI.

## 4. Configuration and rollback (45 seconds)

Show `config/fee_glossary.json`. Text is loaded as runtime data; one entry deliberately remains in review. Run `python3 -m src.fee_breakdown --case zero --hide-explanations` to show text can be hidden without altering total computation.

## 5. Readiness decision (75 seconds)

Ask the ClickUp readiness advisor: "Review code-review readiness for CU-868mnhw6a. Cite missing evidence and the next human action." Then ask release readiness. Expect open glossary approval, independent review, accessibility testing, and UAT to prevent a release-ready claim.

## If something fails

Do not refresh repeatedly or invent a result. Use the README and test map, name the missing evidence, and continue with the human decision. PR merge is not deployment. This demo ends with an open PR.
