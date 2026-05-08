Verify the active RunProof change.

1. Run `runproof status --json` to get the `change_id`.
2. Run `runproof verify <change_id> --discover` — this auto-detects the test runner, executes it, captures cryptographic evidence, and advances to VERIFY if all tests pass.
3. If `--discover` doesn't find the right command, run `runproof verify <change_id> --command "<test_command>"` instead. Infer the test command from the project stack (package.json scripts, pytest.ini, Makefile).
4. If tests fail: show the failure output and suggest the fix. Do not advance the phase.
5. If tests pass: report in one line — phase advanced + evidence checksum (first 12 chars).
