# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A curated documentation repository of AI-powered coding tools, best practices, and learning resources. The primary content lives in `README.md`. There is no application code to build or deploy.

## Maintenance Scripts

```bash
# Validate links in a markdown file
python scripts/check_links.py README.md

# Fix markdown formatting issues
python scripts/fix_markdown_links.py <input.md> <output.md>

# Script dependencies
pip install requests beautifulsoup4
```

## Automated Maintenance

`.github/workflows/maintenance-2026.yml` runs weekly (Mondays 9 AM UTC) and performs:
- Link validation
- Content freshness checks (year/version references)
- Security scanning
- Documentation health checks
- Spell checking (cspell)

Link checker config: `.github/markdown-link-check.json`

## Content Structure

`README.md` is organized as:
1. Universal best practices (prompting, context management, verification)
2. Tool comparisons — 40+ tools across categories (autonomous agents, IDE-integrated, CLI)
3. 2026 AI development trends
4. AI coding workflows (SDD, context engineering, multi-agent)
5. Security guidelines
6. Performance benchmarks
7. Setup guides

## Contributing

When adding or updating content:
- Follow the PR checklist in `PR_CHECKLIST.md`
- Verify all external links work before committing
- Keep tool comparisons consistent with existing table formats
- See `CONTRIBUTING.md` for full guidelines
