---
mode: agent
description: Create a new RunProof governed change with a drafted proposal
---

Convert the user's intent to a kebab-case change_id.
Run `runproof new <change_id>`.
Read `.runproof/memory/constitution.md` if it exists.
Scan the repo for context relevant to the intent.
Write a tight proposal.md: one-sentence intent, explicit scope, success criteria.
Set `status: ready` in the frontmatter.
Run `runproof ready <change_id>`.
Report in one line: change_id created and current phase.
