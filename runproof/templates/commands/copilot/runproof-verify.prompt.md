---
mode: agent
description: Verify the active RunProof change — run tests and capture evidence
---

Run `runproof status --json` to get the change_id.
Run `runproof verify <change_id> --discover`.
If --discover fails to find the test command, infer it from the project stack and run `runproof verify <change_id> --command "<cmd>"`.
If tests fail: report the failure and suggest the fix.
If tests pass: report in one line — phase advanced + evidence checksum (first 12 chars).
