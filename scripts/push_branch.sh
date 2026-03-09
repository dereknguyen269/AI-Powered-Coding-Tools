#!/bin/bash

# Script to push the maintenance branch to GitHub
echo "Pushing maintenance/link-check-fix-2026-03-09 branch to GitHub..."

cd "$(dirname "$0")"

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch: $CURRENT_BRANCH"

# Push to GitHub
echo "Running: git push --set-upstream origin maintenance/link-check-fix-2026-03-09"
git push --set-upstream origin maintenance/link-check-fix-2026-03-09

if [ $? -eq 0 ]; then
    echo "✅ Branch pushed successfully!"
    echo ""
    echo "📋 Next steps:"
    echo "1. Go to: https://github.com/dereknguyen269/AI-Powered-Coding-Tools"
    echo "2. Create a Pull Request from 'maintenance/link-check-fix-2026-03-09' to 'main'"
    echo "3. Use the PR description template in GIT_WORKFLOW.md"
else
    echo "❌ Failed to push branch. Please check your credentials and try again."
    echo "You can also push manually with:"
    echo "  git push origin maintenance/link-check-fix-2026-03-09"
fi