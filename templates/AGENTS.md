# AGENTS.md

Instructions for AI coding agents working in this repository. If the installer created
`CLAUDE.md`, `.cursor/rules/ai-kit.mdc`, or `.github/copilot-instructions.md`, those
are independent copies, not live references. Keep their contents consistent after
editing this file; preserve Cursor's `.mdc` frontmatter.

## Project

<!-- One line: what this is, who uses it. -->

Stack: <!-- language / framework / runtime -->
Entry points: <!-- main files or dirs -->

## Commands

```bash
# install deps
# run tests
# lint / typecheck
# build
```

Run the narrowest command that proves your change. Never claim a command passed unless
you ran it and read the output.

## How to work

1. **Read before writing.** Locate the code, the test, and the convention you are
   extending. If you cannot find one of the three, say so instead of guessing.
2. **Plan in one or two sentences** before a multi-file change. No plan needed for a
   one-line fix.
3. **Smallest working diff.** Touch only what the request requires. Do not refactor,
   reformat, or rename adjacent code.
4. **Verify.** Run the test or command that fails before your change and passes after.
   For non-trivial logic, leave one runnable check behind.
5. **Report.** What changed, what you verified, what is left. No process narration.

## Hard rules

- No new dependency for something the stdlib or an installed package already does.
- No abstractions with one implementation, no config for a value that never changes.
- No files, scaffolding, or "for later" placeholders that the request did not ask for.
- Match existing style even if you would do it differently.
- Never delete pre-existing dead code without asking.
- Validate at trust boundaries: user input, network responses, file paths, auth.
- Never log, echo, or commit secrets. Never invent credentials.

## Stop and ask

- The request has two plausible readings and the choice changes the diff.
- The change touches auth, payments, destructive data operations, or migrations.
- You need a credential, a login, or a resource you cannot reach.
- You are about to widen scope beyond the request.

## Definition of done

- [ ] Change is minimal and traced to the request
- [ ] Tests or a runnable check cover the new behavior
- [ ] No unrelated files modified
- [ ] No secrets, debug prints, or dead code added
- [ ] Summary states what was verified and how
