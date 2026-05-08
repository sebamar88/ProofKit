Write the delta-spec for the active ProofKit change.

1. Run `proofkit status` to find the `change_id`, then read `proposal.md`.
2. Derive the spec directly from the proposal — what components change, what the behavior is before and after, and 3–5 verifiable acceptance criteria. Ask the user only if something critical is missing.
3. Write `.proofkit/changes/<change_id>/delta-spec.md`. Document *only what changes*, not the entire system.
4. Run `proofkit ready <change_id>` to mark the spec ready and advance to DESIGN.
