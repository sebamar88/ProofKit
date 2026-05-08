---
mode: agent
description: Show the active RunProof change status in one line
---

Run `runproof status --json` and report in this format:
<change_id> | <phase> | missing: <missing_artifacts or "none"> | next: /runproof-next

If no active changes: "No active changes — use /runproof-new to start one."
