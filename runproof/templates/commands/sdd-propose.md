Draft a proposal for the active ProofKit change.

1. Run `proofkit status` to find the active `change_id`.
2. Ask the user: **"What are you trying to change and why?"** — skip if the intent is already clear from context.
3. Write `.proofkit/changes/<change_id>/proposal.md`. Keep it tight: one-sentence intent, explicit scope, and how success is measured. No fluff.
4. Run `proofkit ready <change_id>` to mark the proposal ready and advance to SPECIFY.
