# ProofKit Demo Repo Design

## Summary

Create a small standalone repository at `C:\Users\sebam\Desktop\Development\proofkit-demo` that demonstrates the core ProofKit value proposition in under 60 seconds:

1. An AI or human claims a fix is done.
2. The code is still broken.
3. ProofKit blocks fake completion because verification evidence fails.
4. A one-line fix is applied.
5. ProofKit accepts the change only after real execution passes.

The demo is a conversion asset, not a full product tutorial. It should optimize for immediate comprehension, minimal setup, and believable output.

## Goals

- Show a real failing test on intentionally broken code.
- Show ProofKit blocking progress when verification evidence fails.
- Show the smallest possible fix that makes the test pass.
- Show ProofKit accepting the verification only after the passing command runs.
- Keep the full story understandable from the README alone.

## Non-Goals

- Demonstrate the full ProofKit lifecycle in depth.
- Teach the internal architecture of ProofKit.
- Showcase multiple bug classes, adapters, or advanced workflows.
- Require complex setup, external services, or custom infrastructure.

## Recommended Approach

Use a `README-first` repository with a tiny broken Node app plus an optional demo runner script.

Why this approach:

- The README becomes the primary conversion surface.
- The broken app gives concrete, reproducible evidence.
- The script helps with video capture and fast reruns without replacing the manual story.
- The repository remains small enough to understand immediately.

## Alternatives Considered

### 1. Full `.sdd/` workflow demo as the main story

Rejected because it adds too much ceremony for a first-contact demo and weakens the main message.

### 2. Script-only demo with no readable walkthrough

Rejected because it hides the narrative and makes the demo feel magical instead of obvious.

### 3. Multi-case demo with several bugs and multiple verification stages

Rejected because it adds noise and slows comprehension.

## Repository Structure

```text
proofkit-demo/
├── README.md
├── broken-app/
│   ├── app.js
│   ├── package.json
│   └── test.js
└── scripts/
    ├── run-demo.ps1
    └── run-demo.sh
```

## Demo Flow

### Step 1: Start broken

The repository ships with a deliberate one-line bug:

```js
function sum(a, b) {
  return a - b;
}
```

The associated test must fail from a clean checkout.

### Step 2: Show reality

The README instructs the user to run the test inside `broken-app/` and see the real failure.

### Step 3: Show ProofKit enforcement

The README then shows ProofKit rejecting verification when the command fails. The exact command used in the repo should be the real one validated during implementation, not placeholder output.

### Step 4: Apply the one-line fix

The README shows the corrected implementation:

```js
function sum(a, b) {
  return a + b;
}
```

### Step 5: Re-run verification

The test passes, then ProofKit records passing execution evidence.

## Content Requirements

### README

The README must:

- lead with the ProofKit value proposition
- show the broken state first
- use short step-by-step sections
- include only the minimum commands needed
- use real command output captured from the implementation environment
- end with the short product promise: ProofKit stops fake completion and only accepts real execution

The README should not:

- explain internal architecture
- describe advanced command surfaces unless they directly support the core story
- include multiple branching paths

### Broken App

The application should:

- use plain Node.js with no extra dependencies
- include exactly one exported function
- include exactly one failing assertion
- stay small enough to inspect in seconds

### Scripts

Provide:

- `scripts/run-demo.sh`
- `scripts/run-demo.ps1`

These scripts should:

- run the broken test
- run the ProofKit verification step
- avoid hiding failures behind excessive formatting

They are helpers, not the primary interface.

## Execution Assumptions

- `node` and `npm` are available.
- `proofkit` is invokable in the local environment, or can be run through a documented alternative such as `npx -y proofkit@latest`.
- The repo should not require installing additional packages beyond the standard Node runtime already present.

## Success Criteria

The demo is successful if:

- a user can read the README and understand the ProofKit value in under 60 seconds
- the initial test run fails reliably
- the ProofKit verification step fails against the broken code
- the one-line fix makes the test pass
- the ProofKit verification step succeeds after the fix

## Implementation Notes

- Prefer Windows-friendly commands in the main README because the target environment here is Windows.
- Keep shell examples copyable.
- If local `proofkit` invocation differs from published install usage, document the exact command that was actually verified.
- Capture real outputs during implementation and use those in the README instead of invented snippets.

## Risks

- If `proofkit verify` requires a specific repository initialization flow, the demo may need a minimal governed setup that stays mostly out of the main narrative.
- If `proofkit` is not globally available in the environment, the README must use a fallback invocation that still feels lightweight.
- If the verification command wording is too abstract, the demo will lose conversion value.

## Deliverable

A standalone demo repository that is intentionally tiny, reproducible, and optimized to answer one question clearly:

“How does ProofKit stop an AI from saying ‘done’ when the code is still broken?”
