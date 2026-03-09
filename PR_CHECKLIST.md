# PR Checklist for Repository Maintenance

## Before Creating PR
- [ ] All maintenance files are in the repository
- [ ] Git status shows only the intended files
- [ ] Commit message follows conventional commits format
- [ ] Branch name is descriptive (e.g., `maintenance/link-check-fix-2026-03-09`)

## Files to Include
### Required:
- [ ] `corrected-link-report.md` - Link validation results
- [ ] `maintenance-report.md` - Comprehensive summary
- [ ] `maintenance-plan.md` - Updated plan
- [ ] `link_checker.py` - Improved tool
- [ ] `check_links.py` - Markdown-aware checker

### Recommended:
- [ ] `fix_markdown_links.py` - Link formatter
- [ ] `CONTRIBUTING.md` - Contributor guidelines
- [ ] `CODE_OF_CONDUCT.md` - Community standards
- [ ] `README-link-check.md` - Documentation

## PR Description Checklist
- [ ] Clear title starting with "fix: " or "feat: "
- [ ] Summary of what was fixed (all links working)
- [ ] List of files added/changed
- [ ] Explanation of false positive issue
- [ ] Repository health assessment
- [ ] Next steps/recommendations

## Testing (if applicable)
- [ ] Link checker runs without errors
- [ ] All scripts execute properly
- [ ] Markdown files render correctly
- [ ] No broken links in new documentation

## Final Verification
- [ ] PR targets correct base branch (usually `main` or `master`)
- [ ] PR description is complete and professional
- [ ] All checkboxes in this list are checked
- [ ] Ready for review!

## Common PR Titles
- `fix: Repository maintenance and link validation`
- `feat: Add maintenance tools and documentation`
- `docs: Add link validation report and maintenance plan`
- `chore: Update repository maintenance infrastructure`

## PR Labels (if available)
- `documentation`
- `maintenance`
- `tools`
- `bug-fix` (for the false positive issue)
- `enhancement`