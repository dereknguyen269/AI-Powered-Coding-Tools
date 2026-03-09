#!/bin/bash

# Script to commit and push the script reorganization
echo "Committing script reorganization..."

cd /Users/quan/.picoclaw/workspace/AI-Powered-Coding-Tools

# Commit the changes
git commit -m "refactor: organize Python scripts into scripts/ folder

- Moved all Python scripts to scripts/ directory for better organization
- Added scripts/README.md with documentation for each script
- Moved push_branch.sh to scripts/ folder
- Updated references in maintenance documentation
- Updated GIT_WORKFLOW.md with new file paths

This improves repository structure and makes maintenance tools more discoverable."

if [ $? -eq 0 ]; then
    echo "✅ Changes committed successfully!"
    echo ""
    echo "📋 Next: Pushing to GitHub..."
    git push origin maintenance/link-check-fix-2026-03-09
else
    echo "❌ Failed to commit changes. Please check git status."
fi