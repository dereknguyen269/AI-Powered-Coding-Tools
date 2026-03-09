#!/usr/bin/env python3
"""
Markdown Link Formatter
Fixes common markdown link formatting issues, particularly URLs with
extra closing parentheses or other punctuation.
"""

import re
import sys

def fix_markdown_links(content):
    """
    Fix markdown links with formatting issues.
    
    Common issues:
    1. URLs with closing parentheses: [text](https://example.com/path))
    2. URLs with other trailing punctuation
    3. Missing spaces between links
    """
    
    # Pattern to find markdown links
    # This captures [text](url) where url might have trailing punctuation
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    def fix_url(match):
        text = match.group(1)
        url = match.group(2)
        
        # Remove trailing punctuation that shouldn't be part of URL
        # Common issues: ), ., ,, ;, :, !, ?
        original_url = url
        
        # Check if URL ends with common punctuation
        # But be careful not to remove valid URL characters
        # We'll only remove punctuation that's likely formatting errors
        
        # Case 1: URL ends with closing parenthesis (common markdown error)
        if url.endswith(')') and url.count('(') == 0:
            # This is likely a formatting error
            url = url.rstrip(')')
            print(f"  Fixed: Removed trailing ')' from URL")
            print(f"    Original: {original_url}")
            print(f"    Fixed:    {url}")
        
        # Case 2: URL ends with period, comma, semicolon, etc.
        # But only if it looks like it might be punctuation, not part of URL
        punctuation = '.,;:!?'
        if url.endswith(tuple(punctuation)):
            # Check if this looks like a valid URL ending
            # Valid URL endings: .com, .org, .io, etc.
            valid_endings = ['.com', '.org', '.net', '.io', '.dev', '.ai', '.co', '.uk', '.edu', '.gov']
            if not any(url.endswith(ending) for ending in valid_endings):
                # Might be punctuation, but be conservative
                # Only fix if URL already has a valid TLD
                if '.' in url[:-1]:  # Has a dot before the last character
                    last_part = url.split('.')[-1]
                    if len(last_part) <= 1:  # Very short last part (like ".)")
                        url = url.rstrip(punctuation)
                        print(f"  Fixed: Removed trailing punctuation from URL")
                        print(f"    Original: {original_url}")
                        print(f"    Fixed:    {url}")
        
        return f'[{text}]({url})'
    
    # Fix all links
    fixed_content = re.sub(link_pattern, fix_url, content)
    
    return fixed_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_markdown_links.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Processing: {input_file}")
        print("=" * 50)
        
        fixed_content = fix_markdown_links(content)
        
        if fixed_content != content:
            # Create backup
            backup_file = input_file + '.backup'
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\nBackup saved to: {backup_file}")
            
            # Write fixed content
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed file saved to: {input_file}")
            
            # Show changes
            print("\nSummary of changes:")
            original_lines = content.split('\n')
            fixed_lines = fixed_content.split('\n')
            
            for i, (orig, fixed) in enumerate(zip(original_lines, fixed_lines)):
                if orig != fixed:
                    print(f"\nLine {i+1}:")
                    print(f"  Original: {orig}")
                    print(f"  Fixed:    {fixed}")
        else:
            print("No formatting issues found.")
            
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()