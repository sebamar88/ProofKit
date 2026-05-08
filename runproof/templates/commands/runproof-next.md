Run `runproof status --json` and capture the output.

If `can_auto_advance` is true: run `runproof next` and report the new phase in one line.

If `can_auto_advance` is false:
1. Read `next_action` from the JSON output to identify the missing artifact.
2. Read `.runproof/skills/<current_phase>.md` for phase-specific instructions.
3. Read `.runproof/memory/constitution.md` if it exists for project constraints.
4. Scan the repo for relevant context (recent commits, existing specs, tech stack).
5. Draft the artifact content and write it to `.runproof/changes/<change_id>/<artifact_file>`.
6. Run `runproof ready <change_id>` to mark it ready and advance the phase.
7. Report in one line: what was written and the new phase.
