# SDD-Core: Draft Delta-Spec

I'll help you write the **delta-spec** — the contract that documents *only what changes*
in this commit, not the full specification.

Answer the following questions:

1. **Change ID** – What is the `change_id`?
   *(run `sdd-core phase <change_id>` to confirm you are in the SPECIFY phase)*

2. **Components affected** – Which files, modules, APIs, or data models are touched?

3. **Behavior before** – What does the system do today that this change replaces or extends?

4. **Behavior after** – What will the system do once this change lands?

5. **Interface contracts** – Any public API, CLI flags, config keys, or schema changes?
   List each new/changed/removed surface with before → after.

6. **Acceptance criteria** – State 3–5 verifiable, unambiguous acceptance conditions.

---

Once you answer, I will write `.sdd/changes/<change_id>/delta-spec.md` with `status: draft`.

When the spec is reviewed and ready, set `status: ready` and run:

```bash
sdd-core transition <change_id> design
```
