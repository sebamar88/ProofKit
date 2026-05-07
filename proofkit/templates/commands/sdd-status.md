# SDD-Core: Change Status

I'll help you understand the current state of a change and recommend the next action.

Tell me the **change_id** you want to check, or run:

```bash
# List all active changes and their phases
sdd-core status

# Show the declared phase of a specific change
sdd-core phase <change_id>

# Run the workflow gate (shows what is ready and what is missing)
sdd-core run <change_id>

# Show the recorded command history
sdd-core log <change_id>

# Check if the change is ready to archive
sdd-core check <change_id>

# Full governance report (PR-ready)
sdd-core pr-check <change_id>
```

---

Once you share the `change_id` (and optionally paste `sdd-core run <change_id>` output),
I'll analyze the current state and tell you exactly what needs to happen next.
