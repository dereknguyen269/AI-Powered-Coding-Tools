#!/bin/bash

# Script to push main branch with new 2026 content
echo "🚀 Pushing new 2026 AI development content to GitHub..."

# Check if we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "❌ Error: Not on main branch. Current branch: $CURRENT_BRANCH"
    echo "Please checkout main branch first: git checkout main"
    exit 1
fi

# Show what will be pushed
echo "📊 Changes to be pushed:"
git log --oneline -5

echo ""
echo "📁 New files added:"
git diff --name-only HEAD~1 HEAD

echo ""
echo "🔍 Running pre-push checks..."

# Check if there are any changes
if git diff --quiet HEAD~1 HEAD; then
    echo "❌ No changes to push"
    exit 1
fi

echo ""
echo "✅ Ready to push. Press Enter to continue or Ctrl+C to cancel..."
read

# Push to GitHub
echo "🔄 Pushing to origin/main..."
git push origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Successfully pushed new 2026 content!"
    echo ""
    echo "📋 Summary of new content:"
    echo "1. AI-CODING-WORKFLOWS-2026.md - Modern development methodologies"
    echo "2. AI-TOOLS-COMPARISON-2026.md - Comprehensive tool analysis"
    echo "3. AI-SECURITY-GUIDELINES-2026.md - Security best practices"
    echo "4. SETUP-GUIDE-2026.md - Production-ready environment setup"
    echo "5. GitHub Actions workflow - Automated maintenance"
    echo "6. Updated README.md - Added 2026 resources section"
    echo ""
    echo "🌐 View repository: https://github.com/dereknguyen269/AI-Powered-Coding-Tools"
else
    echo "❌ Failed to push. Please check your credentials and try again."
    echo "You can push manually with: git push origin main"
fi