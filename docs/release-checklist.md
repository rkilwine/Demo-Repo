# Release readiness checklist

Synthetic demo. Every unchecked item remains pending. No automated approval.

- [ ] Inspect the latest PR head SHA and a successful test run for that SHA.
- [ ] Link the failing rounding-regression run and later passing fix run.
- [ ] Obtain independent human review; author notes do not count.
- [ ] Resolve glossary wording approval. Demo states are not real approvals.
- [ ] Implement and validate keyboard and screen-reader behavior in a frontend.
- [ ] Execute staging regression and business UAT, neither included here.
- [ ] Verify ClickUp activity links for CU-868mnhw6a and CU-868mnhw8a.
- [ ] Confirm release owner, rollout scope, monitoring, and rollback decision.
- [ ] Update knowledge and attach observed evidence.
- [ ] Human release decision recorded separately from PR merge.

## Current evidence boundary

Repository code, unit tests, and Actions runs can support code review. They do not establish deployment, production access, regulatory compliance, or business acceptance. Keep the PR open for the demo; do not merge from this checklist.
