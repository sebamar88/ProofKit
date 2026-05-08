Break the active ProofKit change into tasks.

1. Run `proofkit status` to find the `change_id`, then read `design.md`.
2. Derive an ordered task list from the design — each task small and independently testable. No explanations, just the list.
3. Write `.proofkit/changes/<change_id>/tasks.md` with `- [ ]` checkboxes and `status: draft`.
4. Implement the tasks one by one, checking each off (`- [x]`) as you complete it.
5. When all tasks are checked, run `proofkit ready <change_id>` to mark the task list ready and advance to VERIFY.
