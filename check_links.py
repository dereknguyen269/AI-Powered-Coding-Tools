#!/usr/bin/env python3
"""
Improved Markdown Link Checker
Properly extracts and checks markdown links without formatting issues.
"""

import re
import requests
import sys
from urllib.parse import urlparse
import time

def extract_markdown_links(content):
    """
    Extract markdown links from content.
    Returns list of tuples: (text, url, line_number)
    """
    links = []
    
    # Pattern for markdown links: [text](url)
    # This handles URLs with parentheses inside them
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        matches = re.finditer(pattern, line)
        for match in matches:
            text = match.group(1)
            url = match.group(2)
            links.append((text, url, i))
    
    return links

def check_link(url, timeout=10):
    """
    Check if a link is accessible.
    Returns (status_code, error_message)
    """
    try:
        # Clean the URL - remove trailing punctuation that might be markdown formatting
        cleaned_url = url.strip()
        
        # Common markdown formatting errors
        if cleaned_url.endswith(')') and '(' not in cleaned_url:
            cleaned_url = cleaned_url.rstrip(')')
        
        # Skip if it's not a valid URL
        parsed = urlparse(cleaned_url)
        if not parsed.scheme or not parsed.netloc:
            return None, "Invalid URL format"
        
        # Make the request
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0)'
        }
        
        response = requests.head(
            cleaned_url, 
            headers=headers, 
            timeout=timeout,
            allow_redirects=True
        )
        
        return response.status_code, None
        
    except requests.exceptions.Timeout:
        return None, "Timeout"
    except requests.exceptions.ConnectionError:
        return None, "Connection error"
    except requests.exceptions.TooManyRedirects:
        return None, "Too many redirects"
    except Exception as e:
        return None, str(e)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check_links.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Checking links in: {input_file}")
        print("=" * 80)
        
        links = extract_markdown_links(content)
        
        print(f"Found {len(links)} markdown links")
        print()
        
        working = 0
        broken = 0
        skipped = 0
        
        for text, url, line_num in links:
            print(f"Line {line_num}: [{text}]({url})")
            
            status, error = check_link(url)
            
            if status is None:
                print(f"  ❌ Error: {error}")
                broken += 1
            elif status == 200:
                print(f"  ✅ OK (HTTP {status})")
                working += 1
            elif 300 <= status < 400:
                print(f"  ⚠️  Redirect (HTTP {status})")
                working += 1
            elif status == 404:
                print(f"  ❌ Broken (404 Not Found)")
                broken += 1
            elif status == 403:
                print(f"  ⚠️  Access denied (403 Forbidden)")
                broken += 1
            else:
                print(f"  ⚠️  HTTP {status}")
                broken += 1
            
            print()
            time.sleep(0.5)  # Be nice to servers
        
        print("=" * 80)
        print("Summary:")
        print(f"  Total links: {len(links)}")
        print(f"  Working: {working}")
        print(f"  Broken: {broken}")
        print(f"  Skipped: {skipped}")
        
        # Save report
        report_file = input_file.replace('.md', '-link-check.md')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(f"# Link Check Report\n")
            f.write(f"File: {input_file}\n")
            f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Summary\n")
            f.write(f"- Total Links: {len(links)}\n")
            f.write(f"- Working: {working}\n")
            f.write(f"- Broken: {broken}\n")
            f.write(f"- Skipped: {skipped}\n\n")
            
            if broken > 0:
                f.write(f"## Broken Links\n\n")
                for text, url, line_num in links:
                    status, error = check_link(url)
                    if status is None or status >= 400:
                        f.write(f"### Line {line_num}: [{text}]({url})\n")
                        f.write(f"- URL: {url}\n")
                        if status:
                            f.write(f"- Status: HTTP {status}\n")
                        if error:
                            f.write(f"- Error: {error}\n")
                        f.write("\n")
        
        print(f"\nReport saved to: {report_file}")
            
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()