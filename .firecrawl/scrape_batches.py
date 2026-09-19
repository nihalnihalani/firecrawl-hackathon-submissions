import subprocess
import sys
import time

urls = [
    "https://vibeapps.dev/s/carter",
    "https://vibeapps.dev/s/compari",
    "https://vibeapps.dev/s/faultline",
    "https://vibeapps.dev/s/duebell",
    "https://vibeapps.dev/s/mp3totext",
    "https://vibeapps.dev/s/safeplate",
    "https://vibeapps.dev/s/exorcist",
    "https://vibeapps.dev/s/quote-arena",
    "https://vibeapps.dev/s/after",
    "https://vibeapps.dev/s/ombuds",
    "https://vibeapps.dev/s/opportunity-scout",
    "https://vibeapps.dev/s/bipolar",
    "https://vibeapps.dev/s/datehaja",
    "https://vibeapps.dev/s/perkdropclick",
    "https://vibeapps.dev/s/backpack",
    "https://vibeapps.dev/s/fillable",
    "https://vibeapps.dev/s/tenantshield",
    "https://vibeapps.dev/s/overlap",
    "https://vibeapps.dev/s/zabuton",
    "https://vibeapps.dev/s/thesisline",
    "https://vibeapps.dev/s/attestor",
    "https://vibeapps.dev/s/regvista",
    "https://vibeapps.dev/s/pixelshop-the-ai-shopping-network",
    "https://vibeapps.dev/s/offscript",
    "https://vibeapps.dev/s/beacon",
    "https://vibeapps.dev/s/one-table",
    "https://vibeapps.dev/s/might",
    "https://vibeapps.dev/s/claim-check",
    "https://vibeapps.dev/s/ceilinggate",
    "https://vibeapps.dev/s/still-true",
    "https://vibeapps.dev/s/rentpilot",
    "https://vibeapps.dev/s/block",
    "https://vibeapps.dev/s/noticeproof",
    "https://vibeapps.dev/s/get-it-in-writing",
    "https://vibeapps.dev/s/attest",
    "https://vibeapps.dev/s/red-flag",
    "https://vibeapps.dev/s/recourse",
    "https://vibeapps.dev/s/tableforall"
]

batch_size = 10
for i in range(0, len(urls), batch_size):
    batch = urls[i:i+batch_size]
    print(f"Scraping batch {i//batch_size + 1}/{len(urls)//batch_size + 1}: {len(batch)} URLs...")
    cmd = ["firecrawl", "scrape"] + batch
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error in batch {i//batch_size + 1}:", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
    
    # Pause slightly between batches to avoid hammering the API
    time.sleep(2)

print("Batch scraping completed!")
