---
mode: agent
description: Advance the active RunProof change — auto-execute or draft missing artifacts
---

Run `runproof status --json` and capture the output.

If `can_auto_advance` is true: run `runproof next` and report the new phase in one line.

If `can_auto_advance` is false:
1. Read `next_action` from the JSON output to identify the missing artifact.
2. Read `.runproof/skills/<current_phase>.md` for phase instructions.
3. Read `.runproof/memory/constitution.md` if it exists.
4. Scan the repo for relevant context.
5. Draft and write the artifact to `.runproof/changes/<change_id>/<artifact_file>`.
6. Run `runproof ready <change_id>`.
7. Report in one line: what was written and the new phase.
