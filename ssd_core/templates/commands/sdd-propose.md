# SDD-Core: Draft Proposal

I'll help you write the **proposal** artifact for the current SDD-Core change.
Before I start, answer the following questions:

1. **Change ID** – What is the `change_id`?
   *(run `sdd-core status` if you need to check active changes)*

2. **Intent** – In one sentence, what problem does this change solve?

3. **Scope** – What is explicitly *in scope* and what is explicitly *out of scope*?

4. **Success definition** – How will you know the change succeeded?
   *(tests, metrics, user-visible behavior, acceptance criteria)*

5. **Key risks** – What could go wrong? Any blockers or dependencies?

---

Once you answer the questions above I will write
`.sdd/changes/<change_id>/proposal.md` with `status: draft`.

When the proposal is complete and reviewed, set `status: ready` and run:

```bash
sdd-core transition <change_id> specify
```
