#!/bin/sh
# Smoke test for install.sh. Run: sh tests/test_install.sh
set -eu

repo=$(cd "$(dirname "$0")/.." && pwd)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
fail=0

check() { # check <label> <path>
  if [ -f "$2" ]; then echo "ok   $1"; else echo "FAIL $1 ($2)"; fail=1; fi
}
absent() {
  if [ -f "$2" ]; then echo "FAIL $1 ($2 should not exist)"; fail=1; else echo "ok   $1"; fi
}

for tool in claude cursor copilot agents; do
  mkdir -p "$tmp/$tool"
  sh "$repo/install.sh" --target "$tmp/$tool" --tool "$tool" > /dev/null
  check "$tool: AGENTS.md" "$tmp/$tool/AGENTS.md"
done

check "claude: CLAUDE.md" "$tmp/claude/CLAUDE.md"
absent "claude: no cursor rules" "$tmp/claude/.cursor/rules/ai-kit.mdc"
check "cursor: mdc" "$tmp/cursor/.cursor/rules/ai-kit.mdc"
check "copilot: instructions" "$tmp/copilot/.github/copilot-instructions.md"
check "agents: prompts" "$tmp/agents/docs/ai/prompts.md"
check "agents: checklist" "$tmp/agents/docs/ai/checklist.md"

grep -q '^---$' "$tmp/cursor/.cursor/rules/ai-kit.mdc" || { echo "FAIL cursor: missing frontmatter"; fail=1; }
grep -q 'alwaysApply: true' "$tmp/cursor/.cursor/rules/ai-kit.mdc" || { echo "FAIL cursor: missing alwaysApply"; fail=1; }

# Idempotent: second run must not fail or overwrite
echo "keep me" > "$tmp/claude/AGENTS.md"
sh "$repo/install.sh" --target "$tmp/claude" --tool claude > /dev/null
[ "$(cat "$tmp/claude/AGENTS.md")" = "keep me" ] || { echo "FAIL: overwrote without --force"; fail=1; }

# --force must overwrite
sh "$repo/install.sh" --target "$tmp/claude" --tool claude --force > /dev/null
grep -q 'Instructions for any AI coding agent' "$tmp/claude/AGENTS.md" || { echo "FAIL: --force did not overwrite"; fail=1; }

# Bad tool must exit non-zero
if sh "$repo/install.sh" --target "$tmp" --tool nope > /dev/null 2>&1; then
  echo "FAIL: accepted bad --tool"; fail=1
else
  echo "ok   rejects bad --tool"
fi

[ "$fail" -eq 0 ] && echo "all install tests passed"
exit "$fail"
