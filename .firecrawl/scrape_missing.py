import subprocess
import sys
import time
import os

missing_slugs = [
    'carter', 'faultline', 'safeplate', 'attestor', 'regvista', 
    'pixelshop-the-ai-shopping-network', 'offscript', 'beacon', 
    'one-table', 'might', 'claim-check', 'ceilinggate', 'still-true', 
    'rentpilot', 'block', 'noticeproof', 'get-it-in-writing', 
    'attest', 'red-flag', 'recourse', 'tableforall'
]

urls = [f"https://vibeapps.dev/s/{slug}" for slug in missing_slugs]

batch_size = 5
for i in range(0, len(urls), batch_size):
    batch = urls[i:i+batch_size]
    print(f"Scraping batch {i//batch_size + 1}/{(len(urls)-1)//batch_size + 1}: {len(batch)} URLs...")
    cmd = ["firecrawl", "scrape"] + batch
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error in batch {i//batch_size + 1}:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        # If we failed, let's sleep a bit longer
        time.sleep(10)
    
    if i + batch_size < len(urls):
        print("Sleeping for 35 seconds to respect rate limits...")
        time.sleep(35)

print("Scraping completed!")
