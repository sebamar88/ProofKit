---
title: ProofKit User Guide in Notion
date: 2026-05-07
status: approved
---

# Goal

Create a bilingual user guide for ProofKit in Notion and link it from the public README.

# Scope

- Create one Notion home page: `ProofKit User Guide`
- Create three guide sections under the home page:
  - `Quick Start for Engineers`
  - `Team Workflow Guide`
  - `Production Rollout Guide`
- Create two language subpages under each guide:
  - `EN`
  - `ES`
- Add a short `User Guide` section to `README.md` pointing to the Notion home page

# Information Architecture

The guide should favor navigation clarity over compactness.

Recommended structure:

1. Root page: `ProofKit User Guide`
2. Child pages:
   - `Quick Start for Engineers`
   - `Team Workflow Guide`
   - `Production Rollout Guide`
3. Grandchild pages:
   - `EN`
   - `ES`

This avoids mixing languages in one page and keeps direct links stable.

# Content Design

## Quick Start for Engineers

Purpose:
- Fast installation
- First governed change
- Core commands
- Common operator mistakes

## Team Workflow Guide

Purpose:
- Shared workflow with agents
- Handoff discipline
- State transitions
- Review and verification routines

## Production Rollout Guide

Purpose:
- Packaging and installation choices
- Hooks and CI integration
- Release and publish workflow
- Operational troubleshooting

# README Change

Add a short `User Guide` section near the install/getting started area with a single canonical link to the Notion home page.

# Risks

- Notion MCP may not support workspace-root creation cleanly in one call.
- Enhanced Markdown resource lookup may not resolve through MCP; keep page formatting conservative.
- The guide URL must be created first before wiring the README link.

# Acceptance Criteria

- A Notion page named `ProofKit User Guide` exists.
- The page contains the three guide sections listed above.
- Each guide section has `EN` and `ES` subpages.
- The README links to the Notion home page.
