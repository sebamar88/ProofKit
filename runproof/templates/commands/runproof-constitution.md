Create or update the RunProof constitution for this project.

The constitution lives at `.runproof/memory/constitution.md`.

**With arguments** (user provides directives): use them as the basis for each section.

**Without arguments**: infer the constitution by scanning:
- Language and framework (package.json, pyproject.toml, Cargo.toml, go.mod, etc.)
- Test runner and coverage config
- Linting and formatting config (.eslintrc, ruff.toml, .prettierrc, etc.)
- CI configuration (.github/workflows/, .gitlab-ci.yml)
- Existing CLAUDE.md or similar AI guidance files
- Recent commit messages (style and conventions)

Write a constitution with these sections:
- Tech Stack
- Testing Standards
- Code Quality
- AI Agent Guidelines

**If constitution already exists**: show a diff between current and proposed content, then ask the user to confirm before overwriting.

Run `runproof memory show --key constitution` after writing to confirm success.
