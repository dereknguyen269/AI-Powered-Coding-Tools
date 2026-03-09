#!/usr/bin/env python3
"""
Link checker for AI-Powered-Coding-Tools repository
Checks all external links in README.md for validity
"""

import re
import requests
import concurrent.futures
from urllib.parse import urlparse
import time
from datetime import datetime

def extract_links_from_markdown(markdown_content):
    """Extract all HTTP/HTTPS links from markdown content"""
    # Pattern for markdown links: [text](url)
    markdown_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    # Pattern for plain URLs (not in markdown format)
    url_pattern = r'(https?://[^\s<>"\']+)'
    
    links = []
    
    # Find markdown links
    for match in re.finditer(markdown_link_pattern, markdown_content):
        url = match.group(2)
        if url.startswith('http'):
            links.append({
                'url': url,
                'context': match.group(1),
                'type': 'markdown'
            })
    
    # Find plain URLs
    for match in re.finditer(url_pattern, markdown_content):
        url = match.group(1)
        # Skip if already captured as markdown link
        if not any(link['url'] == url for link in links):
            # Get some context around the URL
            start = max(0, match.start() - 50)
            end = min(len(markdown_content), match.end() + 50)
            context = markdown_content[start:end].replace('\n', ' ')
            links.append({
                'url': url,
                'context': context,
                'type': 'plain'
            })
    
    return links

def check_link(link_info):
    """Check if a link is accessible"""
    url = link_info['url']
    
    # Skip GitHub API URLs
    if 'api.github.com' in url:
        return {
            **link_info,
            'status': 'skipped',
            'reason': 'GitHub API URL'
        }
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; AI-Powered-Coding-Tools-Link-Checker/1.0)'
        }
        
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        
        return {
            **link_info,
            'status_code': response.status_code,
            'final_url': response.url,
            'status': 'working' if response.status_code < 400 else 'broken'
        }
        
    except requests.exceptions.Timeout:
        return {
            **link_info,
            'status': 'timeout',
            'reason': 'Request timed out'
        }
    except requests.exceptions.ConnectionError:
        return {
            **link_info,
            'status': 'connection_error',
            'reason': 'Connection failed'
        }
    except requests.exceptions.TooManyRedirects:
        return {
            **link_info,
            'status': 'redirect_error',
            'reason': 'Too many redirects'
        }
    except Exception as e:
        return {
            **link_info,
            'status': 'error',
            'reason': str(e)
        }

def main():
    print("🔍 AI-Powered-Coding-Tools Link Checker")
    print("=" * 50)
    
    # Read the README.md content from the web
    readme_url = "https://raw.githubusercontent.com/dereknguyen269/AI-Powered-Coding-Tools/main/README.md"
    
    try:
        response = requests.get(readme_url)
        response.raise_for_status()
        markdown_content = response.text
        
        print(f"📄 README loaded: {len(markdown_content)} characters")
        
        # Extract links
        links = extract_links_from_markdown(markdown_content)
        print(f"🔗 Found {len(links)} links to check")
        
        # Check links in parallel
        print("⏳ Checking links...")
        start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(check_link, links))
        
        elapsed_time = time.time() - start_time
        
        # Analyze results
        working = [r for r in results if r.get('status') == 'working']
        broken = [r for r in results if r.get('status') in ['broken', 'error', 'timeout', 'connection_error']]
        skipped = [r for r in results if r.get('status') == 'skipped']
        
        print(f"\n📊 Results ({elapsed_time:.1f}s):")
        print(f"✅ Working: {len(working)}")
        print(f"❌ Broken: {len(broken)}")
        print(f"⏭️  Skipped: {len(skipped)}")
        
        # Print broken links
        if broken:
            print(f"\n🔴 Broken Links ({len(broken)}):")
            print("-" * 80)
            for result in broken:
                print(f"URL: {result['url']}")
                print(f"Context: {result['context'][:100]}...")
                if 'status_code' in result:
                    print(f"Status: {result['status_code']}")
                if 'reason' in result:
                    print(f"Reason: {result['reason']}")
                print(f"Type: {result['type']}")
                print()
        
        # Generate report
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"""# Link Check Report
Generated: {timestamp}
Repository: https://github.com/dereknguyen269/AI-Powered-Coding-Tools

## Summary
- Total Links: {len(links)}
- Working: {len(working)}
- Broken: {len(broken)}
- Skipped: {len(skipped)}

## Broken Links Details
"""
        
        for result in broken:
            report += f"\n### {result['url']}\n"
            report += f"- Context: {result['context'][:150]}...\n"
            if 'status_code' in result:
                report += f"- Status Code: {result['status_code']}\n"
            if 'reason' in result:
                report += f"- Reason: {result['reason']}\n"
            report += f"- Type: {result['type']}\n"
        
        # Save report
        with open('link-check-report.md', 'w') as f:
            f.write(report)
        
        print(f"\n📝 Report saved to: link-check-report.md")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()