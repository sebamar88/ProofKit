# SDD-Core: Draft Task Breakdown

I'll help you write the **tasks** artifact — the ordered implementation checklist
that guides the agent through execution.

Answer the following questions:

1. **Change ID** – What is the `change_id`?
   *(confirm with `sdd-core phase <change_id>` that you are in TASK)*

2. **Ordered steps** – List the implementation steps in execution order.
   Each step should be small and independently testable.

3. **Dependencies** – Does any step depend on another?
   Any external resource to fetch or provision first?

4. **Verification gate per step** – What test or check confirms each step is done?

5. **Risky steps** – Which steps are uncertain or could take longer than expected?

---

Once you answer, I will write `.sdd/changes/<change_id>/tasks.md` with unchecked
checkbox items (`- [ ]`) and `status: draft`.

Complete all tasks (check every `- [x]`), then set `status: ready` and run:

```bash
sdd-core verify <change_id> --command "<your-test-command>"
```
