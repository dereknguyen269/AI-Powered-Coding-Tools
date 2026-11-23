#!/bin/sh
# Install the AI starter kit into an existing repo.
# Usage: sh install.sh --target DIR [--tool claude|cursor|copilot|agents|all] [--force]
set -eu

tool=all
target=.
force=0

while [ $# -gt 0 ]; do
  case $1 in
    --target) target=$2; shift 2 ;;
    --tool) tool=$2; shift 2 ;;
    --force) force=1; shift ;;
    -h|--help) sed -n '2,3p' "$0"; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

src=$(cd "$(dirname "$0")" && pwd)
[ -d "$target" ] || { echo "no such directory: $target" >&2; exit 1; }
target=$(cd "$target" && pwd)
[ -f "$src/templates/AGENTS.md" ] || { echo "missing templates/AGENTS.md" >&2; exit 1; }

copy() { # copy <src> <dest>
  if [ -e "$2" ] && [ "$force" -ne 1 ]; then
    echo "skip (exists): ${2#$target/}   [--force to overwrite]"
    return 0
  fi
  mkdir -p "$(dirname "$2")"
  cp "$1" "$2"
  echo "wrote: ${2#$target/}"
}

case $tool in
  claude|cursor|copilot|agents|all) ;;
  *) echo "bad --tool: $tool" >&2; exit 2 ;;
esac

copy "$src/templates/AGENTS.md" "$target/AGENTS.md"
copy "$src/templates/prompts.md" "$target/docs/ai/prompts.md"
copy "$src/templates/checklist.md" "$target/docs/ai/checklist.md"

if [ "$tool" = claude ] || [ "$tool" = all ]; then
  copy "$src/templates/AGENTS.md" "$target/CLAUDE.md"
fi

if [ "$tool" = copilot ] || [ "$tool" = all ]; then
  copy "$src/templates/AGENTS.md" "$target/.github/copilot-instructions.md"
fi

if [ "$tool" = cursor ] || [ "$tool" = all ]; then
  dest="$target/.cursor/rules/ai-kit.mdc"
  if [ -e "$dest" ] && [ "$force" -ne 1 ]; then
    echo "skip (exists): ${dest#$target/}   [--force to overwrite]"
  else
    mkdir -p "$(dirname "$dest")"
    { printf -- '---\ndescription: Project coding rules\nglobs:\nalwaysApply: true\n---\n\n'
      cat "$src/templates/AGENTS.md"; } > "$dest"
    echo "wrote: ${dest#$target/}"
  fi
fi

echo "done. Edit $target/AGENTS.md to fill in Project, Commands, and Stop and ask."
