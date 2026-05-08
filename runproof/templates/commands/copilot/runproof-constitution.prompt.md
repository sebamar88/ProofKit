---
mode: agent
description: Create or update the RunProof constitution for this project
---

If the user provided directives, use them. Otherwise scan the repo: package.json, pyproject.toml, linting configs, CI files, CLAUDE.md, recent commits.

Write `.runproof/memory/constitution.md` with sections: Tech Stack, Testing Standards, Code Quality, AI Agent Guidelines.

If the file already exists, show a diff and ask for confirmation before overwriting.

Run `runproof memory show --key constitution` to confirm success.
