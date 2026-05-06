# SDD-Core: Draft Design

I'll help you write the **design** artifact describing *how* the change will be implemented.

Answer the following questions:

1. **Change ID** – What is the `change_id`?
   *(confirm with `sdd-core phase <change_id>` that you are in DESIGN)*

2. **Approach** – Which design approach are you taking?
   If you evaluated alternatives, briefly note why you rejected them.

3. **Components and data flow** – Walk through the key components:
   what each does, how they interact, and how data flows between them.

4. **New or changed interfaces** – List any new/modified public interfaces,
   CLI flags, config keys, event types, or data schemas.

5. **Edge cases** – What edge cases or failure modes need special handling?

6. **Rollback plan** – If this change needs to be reverted, what is the rollback procedure?

---

Once you answer, I will write `.sdd/changes/<change_id>/design.md` with `status: draft`.

When the design is reviewed and ready, set `status: ready` and run:

```bash
sdd-core transition <change_id> task
```
