# AI Starter Kit

Opinionated, tool-agnostic instructions for coding agents, plus the prompts and review
checks that make them useful. Clone it, run one command, and any agent — Claude Code,
Cursor, Copilot, Codex, Windsurf, Aider — works from the same rules.

No framework, no dependencies, no runtime. Plain Markdown and one POSIX shell script.

## Quick start

```bash
git clone https://github.com/dereknguyen269/AI-Starter-Kit.git
cd AI-Starter-Kit
sh install.sh --target ~/code/my-project          # all tools
```

Pick one tool instead:

```bash
sh install.sh --target . --tool claude     # AGENTS.md + CLAUDE.md
sh install.sh --target . --tool cursor     # AGENTS.md + .cursor/rules/ai-kit.mdc
sh install.sh --target . --tool copilot    # AGENTS.md + .github/copilot-instructions.md
```

Existing files are skipped unless you pass `--force`.

Follow the [step-by-step usage guide](docs/USAGE.md) after installation.

Then open `AGENTS.md` in the target repo and fill in **Project** and **Commands**;
adjust **Stop and ask** for project-specific risks. Tool-specific files are snapshots,
not live references: copy your edited rules into those files too. `--force` overwrites
customizations with the generic template; it does not synchronize edits. See the
[worked example](docs/EXAMPLE.md).

## What you get

| File in your repo | Purpose |
| --- | --- |
| `AGENTS.md` | Single source of truth: project facts, commands, working rules, definition of done |
| `CLAUDE.md` / `.cursor/rules/ai-kit.mdc` / `.github/copilot-instructions.md` | Initial copies at each tool's expected path; update manually after customizing |
| `docs/ai/prompts.md` | Spec, plan, implement, test-first, review, debug, commit, refactor prompts |
| `docs/ai/checklist.md` | Pre-merge review: correctness, trust boundaries, deps, hygiene, rollback |

Why one source: every tool reads a different filename. Generating them from
`templates/AGENTS.md` means a rule change lands everywhere and never rots in one file.

## Verify

```bash
python3 -m unittest discover -s tests -v
```

The kit's only executable surface is `install.sh`; `tests/test_install.sh` checks it
installs the right files per tool, is idempotent, and refuses to clobber without
`--force`.

## Reference

- [docs/GUIDE.md](docs/GUIDE.md) — the long-form guide: prompting, context engineering,
  tool comparison (40+), 2026 workflows, security guidelines.
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to propose changes.
- [PR_CHECKLIST.md](PR_CHECKLIST.md) — checklist for changes to this repo.

The tool landscape moves fast. Pricing and model claims in the guide are dated; the
templates are not.

## License

MIT. See [LICENSE](LICENSE).
