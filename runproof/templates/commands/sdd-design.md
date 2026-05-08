Write the design for the active ProofKit change.

1. Run `proofkit status` to find the `change_id`, then read `proposal.md` and `delta-spec.md`.
2. Derive the implementation approach from the spec — chosen approach, key components and data flow, edge cases. Note rejected alternatives only if the choice is non-obvious.
3. Write `.proofkit/changes/<change_id>/design.md`. Be precise and brief.
4. Run `proofkit ready <change_id>` to mark the design ready and advance to TASK.
