# Use the AI Starter Kit

This kit adds **project instructions and reusable prompts** to an existing codebase. It does not install an AI tool, create an application, configure an account, or manage API keys. You need Git, a POSIX shell, and an AI coding tool of your choice.

## 1. Install into your project

From a separate directory, clone the kit and point `--target` at your **existing** project:

```sh
git clone https://github.com/dereknguyen269/AI-Starter-Kit.git
cd AI-Starter-Kit
sh install.sh --target /absolute/path/to/my-project --tool all
```

`all` installs `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/ai-kit.mdc`, `.github/copilot-instructions.md`, `docs/ai/prompts.md`, and `docs/ai/checklist.md`. For fewer files choose `--tool agents`, `claude`, `cursor`, or `copilot`. All choices include `AGENTS.md`, prompts, and checklist. The default is `all`; the default target is `.` (the current directory), so **set `--target` explicitly** unless you deliberately want to install into the kit itself.

The installer skips existing files. Read its `skip (exists)` messages; **do not use `--force` on a project with customized instructions** unless you want those files overwritten. It never installs software or secrets.

## 2. Make the instructions specific

Open `/absolute/path/to/my-project/AGENTS.md`. Replace the placeholders under **Project** and **Commands** with facts you have verified. For example:

~~~md
## Project

A Python CLI for counting lines in local text files.
Stack: Python 3.12; standard library only.
Entry points: `counter.py`; tests: `tests/test_counter.py`.

## Commands

```sh
python3 -m unittest discover -s tests -v
python3 counter.py --help
```
~~~

Run each command first. Remove placeholder commands your project does not have; add project-specific risks under **Stop and ask**. Keep instructions short, concrete, and about this repository. Do not put credentials, personal data, or unverified commands in instruction files.

**Copies are not synchronized.** If you installed `CLAUDE.md` or `.github/copilot-instructions.md`, copy your customized `AGENTS.md` content into each installed copy. For Cursor, keep the `.mdc` frontmatter (`---` through `---`) and replace **only the body** beneath it. Alternatively, start with `--tool agents` when your tool supports `AGENTS.md` directly; see the compatibility notes below. Running `--force` restores the original *generic* template, not your edits.

## 3. Give the agent a first task

Open your AI coding tool **in the target project**, not in the kit directory. Start with a small, reversible change. The installed `docs/ai/prompts.md` has templates for specifying, planning, implementing, testing, reviewing, and debugging. For example:

```text
Read AGENTS.md and the affected code. Fix the reported bug in <file> only.
Write a test that fails before the fix. Keep the diff minimal.
Run the test command from AGENTS.md and report the actual output.
Ask before changing the public API or touching unrelated files.
```

Treat instructions as context, not a security boundary or a guarantee of compliance. Review changes yourself. Run the tests yourself. Use `docs/ai/checklist.md` before merging, particularly for external input, authentication, migrations, and secrets. See the [worked example](EXAMPLE.md) for a filled-in instruction section and a concrete prompt.

## 4. Update safely

1. Commit your customized instructions in **your project** so the team can review them.
2. When project facts or commands change, edit `AGENTS.md` and refresh any tool-specific copies you chose to install. Preserve the Cursor frontmatter.
3. When the kit itself changes, inspect its template and prompts before manually merging improvements. Do not rerun `--force` over customized files.
4. To remove the kit, delete only the installed files you still own; the installer has no uninstall state and cannot distinguish its files from later edits.

## Tool compatibility (checked November 2026)

- **Claude Code:** Current versions can read `AGENTS.md` directly when there is no project `CLAUDE.md` or `CLAUDE.local.md` in the working directory or above it. If either exists, Claude reads those instead; for older versions or deliberate coexistence, `CLAUDE.md` can import `@AGENTS.md`. Check [Claude Code memory docs](https://code.claude.com/docs/en/memory#agents-md) and verify loaded files with `/context all`.
- **Cursor:** Root `AGENTS.md` is supported as a simple alternative to `.cursor/rules`. An `.mdc` project rule with `alwaysApply: true` applies in Agent chats; rules do not affect Cursor Tab. Avoid divergent copies. See [Cursor rules](https://cursor.com/docs/rules).
- **GitHub Copilot:** `.github/copilot-instructions.md` gives repository-wide instructions on supported surfaces; `AGENTS.md` is also supported for agents, but support varies by Copilot surface. Avoid conflicting copies and check the [support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support) and [repository instructions guide](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

Vendor behavior changes. Check the linked official documentation for your installed version before relying on automatic loading.

## Troubleshooting

- **No instructions applied?** Confirm you opened the *target project*, installed the right file, and launched a new agent session after editing. For Claude Code, inspect `/context all`. For Cursor, check that the `.mdc` extension and frontmatter remain intact.
- **`skip (exists)`?** Existing files were preserved. Merge the template manually; avoid `--force` unless you have reviewed the diff or made a backup.
- **Conflicting instructions?** Keep only the files your tools need, or make their content consistent. `AGENTS.md` is the editing source in this kit, but generated copies do not point to it automatically.
- **Wrong target?** The installer does not create the target directory. Pass an existing absolute path with `--target`.
