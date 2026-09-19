import os
import re
import json

target_slugs = [
    'jamanyo', 'claimhero', 'carter', 'compari', 'faultline', 'duebell', 'mp3totext', 'safeplate',
    'exorcist', 'quote-arena', 'after', 'ombuds', 'opportunity-scout', 'bipolar', 'datehaja',
    'perkdropclick', 'backpack', 'fillable', 'tenantshield', 'overlap', 'zabuton', 'thesisline',
    'attestor', 'regvista', 'pixelshop-the-ai-shopping-network', 'offscript', 'beacon', 'one-table',
    'might', 'claim-check', 'ceilinggate', 'still-true', 'rentpilot', 'block', 'noticeproof',
    'get-it-in-writing', 'attest', 'red-flag', 'recourse', 'tableforall'
]

results = []

for slug in target_slugs:
    path = f'.firecrawl/vibeapps.dev-s-{slug}.md'
    if not os.path.exists(path):
        continue
        
    with open(path, 'r') as f:
        content = f.read()
        
    # Extract Title
    # Formats: '# [Title](url)' or '# Title'
    title_match = re.search(r'#\s+\[([^\]]+)\]', content)
    if not title_match:
        title_match = re.search(r'#\s+([^\n]+)', content)
    title = title_match.group(1).strip() if title_match else slug.capitalize()
    
    # Extract Creator
    creator_match = re.search(r'\[by\s+([^\]]+)\]', content)
    creator = creator_match.group(1).strip() if creator_match else 'N/A'
    if creator == 'N/A':
        # fallback for by Name without links
        alt_creator = re.search(r'by\s+([^·\n]+)', content)
        if alt_creator:
            creator = alt_creator.group(1).strip()
            
    # Extract Submitted Time
    submitted_match = re.search(r'Originally submitted:\s*([^\n]+)', content, re.IGNORECASE)
    submitted = submitted_match.group(1).strip() if submitted_match else 'N/A'
    
    # Extract Links
    video_match = re.search(r'\[Video Demo\]\(([^) "]+)', content)
    video = video_match.group(1).strip() if video_match else 'N/A'
    
    repo_match = re.search(r'\[GitHub Repository\]\(([^) "]+)', content)
    repo = repo_match.group(1).strip() if repo_match else 'N/A'
    
    # Labeled project link
    # Let's find first link in Project Links & Tags
    tags_section = re.search(r'## Project Links & Tags\s*\n\s*\n\s*\[([^\]]+)\]\(([^)]+)\)', content)
    project_url = 'N/A'
    if tags_section:
        project_url = tags_section.group(2).split()[0].strip()
    else:
        # Fallback to finding the link from the title header '# [Title](url)'
        header_link_match = re.search(r'#\s+\[[^\]]+\]\(([^)]+)\)', content)
        if header_link_match:
            project_url = header_link_match.group(1).split()[0].strip()
            
    # Extract Description / Summary (first few paragraphs after the title)
    # Let's extract from Title down to the first header
    summary_match = re.search(r'#\s+\[?[^\]\n]+\]?\(?[^)\n]*\)?\s*\n\s*\n\s*([^#]+)', content)
    summary = 'N/A'
    if summary_match:
        # Cleanup the summary (remove screenshots or large gaps)
        paragraphs = [p.strip() for p in summary_match.group(1).split('\n\n') if p.strip()]
        cleaned_paragraphs = []
        for p in paragraphs:
            if p.startswith('![') or p.startswith('['):
                continue  # skip image elements and lone links at the start
            cleaned_paragraphs.append(p)
        if cleaned_paragraphs:
            summary = ' '.join(cleaned_paragraphs[:2])  # take up to first two paragraphs
            
    # Labeled Sponsor Tags (usually convex, openai, firecrawl, agentmail etc.)
    sponsor_tags = []
    for tag in ['convex', 'openai', 'firecrawl', 'agentmail', 'codex', 'astra', 'fable']:
        if f'tagged with {tag}' in content or f'tag/{tag}' in content:
            sponsor_tags.append(tag)
            
    results.append({
        'slug': slug,
        'title': title,
        'creator': creator,
        'submitted': submitted,
        'project_url': project_url,
        'video_url': video,
        'repo_url': repo,
        'summary': summary[:300] + '...' if len(summary) > 300 else summary,
        'sponsor_tags': sponsor_tags
    })

# Output JSON
with open('hackathon_submissions.json', 'w') as f:
    json.dump(results, f, indent=2)

# Create a beautifully formatted Markdown report
md_report = f"""# AllGas Hackathon Submissions Report
**Total Submissions:** {len(results)}
**Data Extracted on:** Saturday, September 19, 2026

---

"""

for idx, app in enumerate(results, 1):
    md_report += f"""## {idx:02d}. {app['title']}
- **Creator:** {app['creator']}
- **Submission Date:** {app['submitted']}
- **Live App:** {f"[{app['project_url']}]({app['project_url']})" if app['project_url'] != 'N/A' else 'N/A'}
- **GitHub Repository:** {f"[{app['repo_url']}]({app['repo_url']})" if app['repo_url'] != 'N/A' else 'N/A'}
- **Video Demo:** {f"[{app['video_url']}]({app['video_url']})" if app['video_url'] != 'N/A' else 'N/A'}
- **Sponsor Stack:** {', '.join(f'`{t}`' for t in app['sponsor_tags']) if app['sponsor_tags'] else 'N/A'}

### Summary
{app['summary']}

---

"""

with open('hackathon_submissions_report.md', 'w') as f:
    f.write(md_report)

print(f"Extraction complete! Saved data to hackathon_submissions.json and generated report in hackathon_submissions_report.md")
