Create a new RunProof governed change.

1. Convert the user's intent to a kebab-case `change_id` (e.g., "add dark mode" → "add-dark-mode").
2. Run `runproof new <change_id>`.
3. Read `.runproof/memory/constitution.md` if it exists.
4. Scan the repo for context relevant to the intent (stack, related files, recent changes).
5. Write a tight `proposal.md` in `.runproof/changes/<change_id>/proposal.md`:
   - One-sentence intent
   - Explicit scope (what's in, what's out)
   - How success is measured
   Set `status: ready` in the frontmatter.
6. Run `runproof ready <change_id>`.
7. Report in one line: change_id created and current phase.
