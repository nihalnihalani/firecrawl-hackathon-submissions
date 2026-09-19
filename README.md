# AllGas Hackathon: Complete Scraped Submissions Dataset & Analysis

This repository contains the complete, verified, and structured dataset of all **40 project submissions** for the **AllGas Hackathon** (hosted on [Vibe Apps](https://vibeapps.dev/tag/allgashackathon)). 

The entire dataset was compiled autonomously using **Firecrawl** (for deep JS-rendered browser scraping) and **Python** (for rate-limit-aware batch execution and structured schema extraction).

---

## 📂 Repository Structure

```
├── README.md                          # Interactive overview, grid of submissions, and replication guide
├── hackathon_submissions_report.md    # In-depth, individual report of all 40 projects with full summaries
├── hackathon_submissions.json         # Raw, structured JSON dataset of all metadata
└── .firecrawl/
    ├── actions.json                   # Firecrawl browser interaction script (clicks 'Load More' on index page)
    ├── scrape_batches.py              # Main batch scraping script (concurrency limit handling)
    ├── scrape_missing.py              # Self-healing rate-limit-aware scraper for remaining pages
    └── extract_details.py             # Schema parser to compile raw MD into structured JSON & Report
```

---

## 📊 AllGas Hackathon Cohort Analysis

### Sponsor Stack Adoption
This hackathon was sponsored by a powerful stack of full-stack AI development tools. Across all 40 submissions, there was 100% integration and verification of the primary sponsor layers:
*   **Convex:** Live reactive state-sync backend & real-time client queries.
*   **OpenAI:** Structured text processing and cognitive analysis.
*   **Firecrawl:** Real-time web search, browser scraping, and active site monitoring.
*   **AgentMail:** Seamless, inbox-first email communication and webhooks.

### Domain Distribution
The 40 submissions fall into six distinct high-impact functional domains:
1.  **Finance, Quoting & Auditing (10 Apps):** Standardizing complex quotes, tracking hidden subscription charges, and verifying receipts line-by-line.
2.  **Local Gov & Real Estate / Tenancy (6 Apps):** Bridging public records, city compliance data, and direct communication to empower tenants and residents.
3.  **Legal & Consumer Rights Advocacy (4 Apps):** Leveling the playing field against corporate legal/policy structures.
4.  **Invisible UI & Email Logistics (3 Apps):** Removing traditional graphical frontends entirely in favor of zero-friction email-first communication.
5.  **Productivity, Education & Healthcare (3 Apps):** Automatically indexing dynamic lists like medication supply, school newsletters, and transcriptions.
6.  **Collaborative & Niche Tools (14 Apps):** Ranging from multi-agent zero-disclosure contract negotiations (*Overlap*) to browser-based collaborative mystery games (*OFFSCRIPT*).

---

## 📋 The Complete Submissions Grid (40 Projects)

| # | Project Name | Creator | GitHub Repository | Video Demo | Live Application | Sponsor Stack |
|---|---|---|---|---|---|---|
| **01** | Jamanyo | Eugene Tulu | [GitHub](https://github.com/eugene-tulu/convexallgas) | [Demo Video](https://youtu.be/pIHbwgOvZwg) | [Live Link](https://fine-fish-527.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **02** | ClaimHero | Dinh Phuc Thinh | [GitHub](https://github.com/zaikaman/ClaimHero) | [Demo Video](https://www.youtube.com/watch?v=M04LMuJRilg) | [Live Link](https://kindhearted-elephant-992.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **03** | Carter | Ben Anderson | [GitHub](https://github.com/andersjbe/carter-ai) | [Demo Video](https://www.youtube.com/watch?v=zgS6NWyqzFE) | [Live Link](https://ardent-bandicoot-155.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **04** | Compari | David Buss | [GitHub](https://github.com/kotarCreative/compari) | [Demo Video](https://www.loom.com/share/6c39274f0ff84618b1da8e60d2f60327) | [Live Link](https://enduring-husky-65.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **05** | Faultline | N DIVIJ | [GitHub](https://github.com/N-45div/faultline) | [Demo Video](https://youtu.be/oZGHuZrlAnQ) | [Live Link](https://clear-dogfish-72.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **06** | Duebell | Kevin Alexander Soto Burgos | [GitHub](https://github.com/kasbsquall/duebell) | [Demo Video](https://youtu.be/dViTfHukVrc) | [Live Link](https://sleek-grouse-640.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **07** | MP3ToText | ethan | N/A | [Demo Video](https://www.youtube.com/watch?v=axAFqWB9vkw) | [Live Link](https://mp3totext.io/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **08** | SafePlate | Nelson | [GitHub](https://github.com/chinesepowered/safeplate) | [Demo Video](https://www.youtube.com/watch?v=nzArirVettI) | [Live Link](https://valiant-fox-223.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **09** | Exorcist | Nelson | [GitHub](https://github.com/chinesepowered/exorcist) | [Demo Video](https://www.youtube.com/watch?v=An1iPgCm6CU) | [Live Link](https://adventurous-caribou-217.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **10** | Quote Arena | Nelson | [GitHub](https://github.com/chinesepowered/quote-arena) | [Demo Video](https://www.youtube.com/watch?v=dixtNz7GDkU) | [Live Link](https://polished-dragon-158.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **11** | After | Nelson | [GitHub](https://github.com/chinesepowered/after) | [Demo Video](https://www.youtube.com/watch?v=eZ8eIKz-_tc) | [Live Link](https://kindred-guanaco-234.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **12** | Ombuds | Shyam Raghuwanshi | [GitHub](https://github.com/Shyam-Raghuwanshi/Ombuds) | [Demo Video](https://youtu.be/VErPwL-xLYw) | [Live Link](https://flexible-reindeer-206.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **13** | Opportunity Scout | Himanshu Jha | [GitHub](https://github.com/himanshu748/opportunity-scout-convex) | [Demo Video](https://www.youtube.com/watch?v=vnmZcJOoM6o) | [Live Link](https://graceful-spoonbill-850.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **14** | bipolar | Mulugeta Zeferu | [GitHub](https://github.com/mooler-z/bipolar) | [Demo Video](https://drive.google.com/file/d/1xZU_HiHnRfIeF6y7vDF-WBJeRvqJAGDQ/view?usp=sharing) | [Live Link](https://vivid-greyhound-473.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **15** | Datehaja | Hyo Jang | [GitHub](https://github.com/hyochan/Datehaja) | [Demo Video](https://youtu.be/K35t6VaF0iI) | [Live Link](https://merry-bass-190.convex.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **16** | Perkdrop.click | Sanath R | [GitHub](https://github.com/sansynx/perkdrop-click) | N/A | [Live Link](https://perkdrop.click/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **17** | Backpack | Elias | [GitHub](https://github.com/Elioz404/Backpack) | N/A | [Live Link](https://backpack.school/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **18** | Fillable | Aditya Singh | [GitHub](https://github.com/compiler-aditya/fillable-all-gas) | N/A | [Live Link](https://fillable.co/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **19** | TenantShield | memeshe | [GitHub](https://github.com/memeshee/tenantshield) | N/A | [Live Link](https://tenantshield.site/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **20** | Overlap | Aditya Singh | [GitHub](https://github.com/compiler-aditya/convex-all-gas) | N/A | [Live Link](https://overlap.ai/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **21** | Zabuton | Nick Sawinyh | [GitHub](https://github.com/sneg55/zabuton) | N/A | [Live Link](https://zabuton.city/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **22** | ThesisLine | Himanshu Kumar | [GitHub](https://github.com/himanshu748/thesisline) | N/A | [Live Link](https://thesisline.in/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **23** | Attestor | Bamidele Olamide | [GitHub](https://github.com/Bholdguy/attestor) | N/A | [Live Link](https://attestor.net/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **24** | RegVista | Raj Gopalakrishnan | [GitHub](https://github.com/rajgopalakrish/RegVista_CVH) | N/A | [Live Link](https://regvista.io/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **25** | PixelShop — The AI Shopping Network | 胡洪伟 | [GitHub](https://github.com/hhwjsw711/pixelshop) | N/A | [Live Link](https://pixelshop.club/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **26** | OFFSCRIPT | Himanshu Kumar | [GitHub](https://github.com/himanshu748/offscript) | N/A | [Live Link](https://offscript.live/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **27** | Beacon | Nelson | [GitHub](https://github.com/chinesepowered/beacon) | N/A | [Live Link](https://beacon.pet/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **28** | One Table | Himanshu Kumar | [GitHub](https://github.com/himanshu748/one-table) | N/A | [Live Link](https://onetable.club/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **29** | Might | 劉恩言 / Ranopha | [GitHub](https://github.com/Ranopha/might) | N/A | [Live Link](https://might.dev/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **30** | Claim Check | Taylor Heller | [GitHub](https://github.com/snowphamtom/ceilinggate) | N/A | [Live Link](https://claimcheck.io/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **31** | CeilingGate | Taylor Heller | N/A | N/A | [Live Link](https://ceilinggate.net/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **32** | still-true | Randall LaPoint, Jr | [GitHub](https://github.com/Lokie-ree/still-true) | N/A | [Live Link](https://stilltrue.org/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **33** | RentPilot | Himanshu Kumar | [GitHub](https://github.com/himanshu748/rentpilot) | N/A | [Live Link](https://rentpilot.io/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **34** | Block | Shwetas Dhake | [GitHub](https://github.com/shwetd19/Convex-All-Gas/) | N/A | [Live Link](https://blockleads.ai/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **35** | NoticeProof | Tang Vu | [GitHub](https://github.com/tang-vu/noticeproof) | N/A | [Live Link](https://noticeproof.io/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **36** | Get It in Writing | Joe Simo | [GitHub](https://github.com/Joe-Simo/get-it-in-writing) | N/A | [Live Link](https://getitinwriting.net/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **37** | Attest | Yao Tsakpo | [GitHub](https://github.com/yaotsakpo/attest) | N/A | [Live Link](https://attestinbox.com/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **38** | Red Flag | Melanie Cruz | [GitHub](https://github.com/DarkKingpro10/Red-Flag) | N/A | [Live Link](https://redflag.work/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **39** | Recourse | Afolabi Emmanuel | [GitHub](https://github.com/Spagero763/recourse) | N/A | [Live Link](https://recourseclaim.com/) | `convex`, `openai`, `firecrawl`, `agentmail` |
| **40** | TableForAll | Amaan Ahmad | [GitHub](https://github.com/iamaanahmad/TableForAll) | [Demo Video](https://youtu.be/bdyDmLJKL0w) | [Live Link](https://aware-shark-108.convex.site) | `convex`, `openai`, `firecrawl`, `agentmail` |

*(Note: For comprehensive, individual textual breakdowns including Problem Solved, Tech Stack, Key Metrics, and Engineering Challenges for every app, see **[hackathon_submissions_report.md](hackathon_submissions_report.md)**).*

---

## 🚀 How to Reproduce / Re-run the Scraper

If you want to fetch fresh submissions, run live updates, or expand details, you can execute the pipeline yourself.

### 1. Prerequisites
Ensure you have the Firecrawl CLI installed globally and authenticated:
```bash
npm install -g firecrawl-cli
firecrawl auth
```

### 2. Scraping the Index (Load More interaction)
Run the main index scraper with the custom scroll and click actions:
```bash
firecrawl scrape "https://vibeapps.dev/tag/allgashackathon" --actions-file .firecrawl/actions.json -o .firecrawl/all_apps_raw.md
```

### 3. Fetching App Details (Concurrency-Safe Execution)
To fetch the individual detail pages without hitting credit usage bottlenecks or triggering 429 Rate Limits, execute our batching script:
```bash
python3 .firecrawl/scrape_batches.py
```
If any transient errors occur, run the rate-limit-aware self-healing script:
```bash
python3 .firecrawl/scrape_missing.py
```

### 4. Extracting Structured Metadata & Reports
Compile the raw markdown downloads into the clean structured report and JSON format:
```bash
python3 .firecrawl/extract_details.py
```
This compiles all files in `.firecrawl/` and automatically updates `hackathon_submissions.json` and `hackathon_submissions_report.md`.

---

## 📜 Licenses & Disclaimers
*   **Original Data source:** [Vibe Apps](https://vibeapps.dev)
*   **Scraping Tooling:** Powered by [Firecrawl](https://firecrawl.dev)
*   The code and dataset compiled in this repository are published for educational and analytical purposes. All copyrights of individual submissions belong to their respective creators.
