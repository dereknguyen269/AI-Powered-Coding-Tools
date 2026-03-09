# Maintenance Scripts

This directory contains Python and shell scripts for maintaining the AI-Powered-Coding-Tools repository.

## Scripts

### Python Scripts

#### 1. `link_checker.py`
**Purpose:** Basic link checker that extracts URLs from markdown files
**Usage:** `python link_checker.py README.md`
**Output:** Lists all links found in the file

#### 2. `check_links.py`
**Purpose:** Improved markdown-aware link checker with better parsing
**Usage:** `python check_links.py README.md`
**Output:** Detailed report of working/broken links with better markdown parsing

#### 3. `fix_markdown_links.py`
**Purpose:** Fixes common markdown formatting issues in URLs
**Usage:** `python fix_markdown_links.py input.md output.md`
**Output:** Cleaned markdown file with properly formatted URLs

### Shell Scripts

#### 4. `push_branch.sh`
**Purpose:** Helper script to push maintenance branches to GitHub
**Usage:** `./push_branch.sh`
**Requirements:** Must be run from repository root, git must be configured

## Installation

These scripts require Python 3.6+ with the following packages:
- `requests` (for HTTP requests)
- `beautifulsoup4` (for HTML parsing)

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage Examples

### Check all links in README:
```bash
python scripts/check_links.py README.md
```

### Fix markdown formatting issues:
```bash
python scripts/fix_markdown_links.py README.md README-fixed.md
```

### Push maintenance branch:
```bash
chmod +x scripts/push_branch.sh
./scripts/push_branch.sh
```

## Maintenance Workflow

1. **Check links:** `python scripts/check_links.py README.md`
2. **Fix formatting:** `python scripts/fix_markdown_links.py README.md README-fixed.md`
3. **Create branch:** `git checkout -b maintenance/YYYY-MM-DD`
4. **Commit changes:** `git add . && git commit -m "fix: maintenance update"`
5. **Push branch:** `./scripts/push_branch.sh`

## Notes
- These scripts were created during the March 2026 repository maintenance
- They help prevent false positives from basic link checkers
- Consider setting up GitHub Actions for automated link checking