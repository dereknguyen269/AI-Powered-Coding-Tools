# Worked example: add a CLI flag

A tiny example of how to fill the kit in a Python repository. Adapt paths and commands to your project; do not paste the example rules into unrelated repos unchanged.

## Project-specific `AGENTS.md` sections

Keep the generic rules installed by the kit. Replace the placeholders with:

~~~markdown
## Project

A CLI that counts lines in a text file for local users.
Stack: Python 3.12, standard library only.
Entry points: `counter.py`; tests in `tests/test_counter.py`.

## Commands

```sh
python3 -m unittest discover -s tests -v
python3 counter.py --help
```

## Stop and ask

Ask before changing the CLI output format, since other scripts parse it.
~~~

If you use Claude Code, Cursor, or Copilot, update the installed tool-specific copy too: `install.sh` copied template text at install time; it does **not** sync later edits to `AGENTS.md`.

## Prompt

Use the [implement prompt](../templates/prompts.md) with these values:

```text
Implement --ignore-empty for counter.py only.
- Files allowed: counter.py, tests/test_counter.py. Do not touch anything else.
- Match the existing CLI style.
- No new dependencies.
- First add a test: a file with three lines, one blank, reports 2 with --ignore-empty and 3 without.
- Run python3 -m unittest discover -s tests -v and paste real output.
```

## Review and verify

Check the diff against [the review checklist](../templates/checklist.md): flag absent preserves old behavior; empty files work; unreadable paths report errors; no unrelated changes. Run the command yourself. Record the actual pass/fail result in the PR, not an agent's prediction.
