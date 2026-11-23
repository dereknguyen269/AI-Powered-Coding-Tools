# Review checklist

Apply to AI-generated code before merge. Every unchecked box is a question for the author,
not a suggestion.

## Correctness

- [ ] The diff does exactly what the request asked — no extra features, no drive-by refactors
- [ ] Error paths handled: what happens on timeout, empty input, 4xx/5xx, missing file
- [ ] Async/concurrency: no unawaited promises, no shared mutable state without a guard
- [ ] Off-by-one and boundary cases covered by a test or a runnable check
- [ ] Behavior verified by running it — not inferred from reading the code

## Trust boundaries

- [ ] All external input validated (body, query, headers, filenames, URLs)
- [ ] No secret, token, key, or credential in the diff, logs, or fixtures
- [ ] No `eval`, shell interpolation of user data, or unbounded path joins
- [ ] Auth/authorization checked server-side, not in the UI
- [ ] Destructive operations require explicit intent and are reversible or backed up

## Dependencies and surface

- [ ] No new dependency without a stated reason and a check that stdlib can't do it
- [ ] No new file, config key, or abstraction with a single use
- [ ] Public API/response shape unchanged, or the change is called out and versioned

## Repo hygiene

- [ ] Tests pass locally; CI green (or the failure is explained, not hidden)
- [ ] No debug prints, commented-out code, TODOs, or "for later" scaffolding
- [ ] Unrelated files untouched; no reformatting noise in the diff
- [ ] Commit message explains why; PR body lists what was verified and how

## Rollback

- [ ] Migration/backfill has a down path
- [ ] Feature can be disabled without a redeploy, or the revert is a single commit
