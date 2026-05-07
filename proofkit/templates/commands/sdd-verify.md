# SDD-Core: Verification Readiness Check

I'll help you confirm the change meets its acceptance criteria before recording the
VERIFY phase.

Answer the following questions:

1. **Change ID** – What is the `change_id`?
   *(confirm with `sdd-core phase <change_id>` that you are in TASK or ready to verify)*

2. **Test command** – What command runs your full test suite?
   *(e.g. `pytest`, `npm test`, `cargo test --all`)*

3. **All green?** – Confirm every test passes.
   If not: which are failing and what is blocking them?

4. **Acceptance criteria** – Go through the delta-spec acceptance criteria one by one
   and confirm each is met with evidence.

5. **Edge cases** – Were the design edge cases exercised by the tests?

6. **No regressions** – Has anything outside the scope of this change broken?

---

Once everything is confirmed, run:

```bash
sdd-core verify <change_id> --command "<your-test-command>"
```

SDD-Core will execute the command, capture cryptographic evidence, and advance
the phase to VERIFY automatically.
