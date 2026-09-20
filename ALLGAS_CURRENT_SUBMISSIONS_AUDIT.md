# All Gas Hackathon: current submission and public repository audit

Snapshot: September 20, 2026. Listing: [allgashackathon](https://vibeapps.dev/tag/allgashackathon). This covers every entry visible after exhausting Load More, not an independent eligibility check.

## Coverage

- Firecrawl expanded the listing from 20 to 40 to 48 entries, then retrieved all 48 individual detail pages. Every detail request completed successfully.
- The detail pages list 44 GitHub repositories, one GitLab repository, and three entries without a repository link.
- Public GitHub API inspection retrieved 43 repository trees and 41 root READMEs. Jamanyo and Compari have accessible trees but their root README endpoints returned 404. Red Flag's linked repository returned 404.
- Firecrawl also retrieved Faultline's current GitLab root tree and rendered README. That makes 44 accessible repositories and 42 retrieved READMEs across both hosts; GitLab coverage does not include a recursive source-file audit.
- Across the 43 accessible GitHub repositories, 181 selected source/configuration/hackathon-log files were downloaded. One additional ClaimHero hackathon log was skipped because of size. Selection covered available schemas, Convex component configuration, package manifests and hackathon logs, plus targeted workflow files for the nearest competitors.
- This is a static review. No downloaded repository code was executed and no claim is made that all deployed apps or sponsor integrations were tested.
- Votes are a snapshot of the listing, not unique-user validation, eligibility, adoption or judges' scores.

## Decision

**BackToCard** is the preferred project hypothesis: reconcile each returned item against actual confirmed refunds and later recharges. Its strongest competing entry is Recourse. A policy lookup, generated complaint and reminder alone would be insufficient differentiation. See [the complete decision, evidence and build scope](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/BACKTOCARD_PROJECT_DECISION.md).

## All 48 entries

| # | Project | Category | Listed repository | Static review | Votes |
|---|---|---|---|---|---|
| 1 | [Found](https://vibeapps.dev/s/found) | Housing and accommodation | [GitHub](https://github.com/AdamAmr05/found) | README + tree + selected files | 1 |
| 2 | [workshop](https://vibeapps.dev/s/workshop) | Learning and simulation | [GitHub](https://github.com/Joystonm/workshop) | README + tree + selected files | 2 |
| 3 | [Bidzy](https://vibeapps.dev/s/bidzy) | Quotes and procurement | [GitHub](https://github.com/Kingnanaweb3/bidzy) | README + tree + selected files | 2 |
| 4 | [OurSpaces](https://vibeapps.dev/s/ourspaces) | Shared group coordination | [GitHub](https://github.com/thomasnguyen/ourspaces-app) | README + tree + selected files | 4 |
| 5 | [Subzero](https://vibeapps.dev/s/subzero) | Subscriptions and cancellation | [GitHub](https://github.com/DammyCodes-all/subzero) | README + tree + selected files | 2 |
| 6 | [RecallReady](https://vibeapps.dev/s/recallready) | Product recalls | [GitHub](https://github.com/demonchant/recallready) | README + tree + selected files | 1 |
| 7 | [Iris - Your iMessage Thought Partner](https://vibeapps.dev/s/iris-your-imessage-thought-partner) | Personal companion | Not listed | No repository listed | 1 |
| 8 | [Pigeon](https://vibeapps.dev/s/pigeon) | Page and document monitoring | [GitHub](https://github.com/ref-dev22/pigeon) | README + tree + selected files | 2 |
| 9 | [Jamanyo](https://vibeapps.dev/s/jamanyo) | Shopping and discovery | [GitHub](https://github.com/eugene-tulu/convexallgas) | Tree + selected files; no root README | 1 |
| 10 | [ClaimHero](https://vibeapps.dev/s/claimhero) | Claims and disputes | [GitHub](https://github.com/zaikaman/ClaimHero) | README + tree + selected files | 2 |
| 11 | [Carter](https://vibeapps.dev/s/carter) | Shopping and discovery | [GitHub](https://github.com/andersjbe/carter-ai) | README + tree + selected files | 2 |
| 12 | [Compari](https://vibeapps.dev/s/compari) | Quotes and procurement | [GitHub](https://github.com/kotarCreative/compari) | Tree + selected files; no root README | 1 |
| 13 | [Faultline](https://vibeapps.dev/s/faultline) | Housing and accommodation | [GitLab](https://gitlab.com/ndivij2004/faultline) | Rendered README + root tree | 2 |
| 14 | [Duebell](https://vibeapps.dev/s/duebell) | Claims and disputes | [GitHub](https://github.com/kasbsquall/duebell) | README + tree + selected files | 1 |
| 15 | [MP3ToText](https://vibeapps.dev/s/mp3totext) | Transcription | Not listed | No repository listed | 2 |
| 16 | [SafePlate](https://vibeapps.dev/s/safeplate) | Food and dining | [GitHub](https://github.com/chinesepowered/safeplate) | README + tree + selected files | 1 |
| 17 | [Exorcist](https://vibeapps.dev/s/exorcist) | Subscriptions and cancellation | [GitHub](https://github.com/chinesepowered/exorcist) | README + tree + selected files | 1 |
| 18 | [Quote Arena](https://vibeapps.dev/s/quote-arena) | Quotes and procurement | [GitHub](https://github.com/chinesepowered/quote-arena) | README + tree + selected files | 1 |
| 19 | [After](https://vibeapps.dev/s/after) | Life administration | [GitHub](https://github.com/chinesepowered/after) | README + tree + selected files | 1 |
| 20 | [Ombuds](https://vibeapps.dev/s/ombuds) | Care and healthcare | [GitHub](https://github.com/Shyam-Raghuwanshi/Ombuds) | README + tree + selected files | 2 |
| 21 | [Opportunity Scout](https://vibeapps.dev/s/opportunity-scout) | Opportunity discovery | [GitHub](https://github.com/himanshu748/opportunity-scout-convex) | README + tree + selected files | 4 |
| 22 | [bipolar](https://vibeapps.dev/s/bipolar) | Social and entertainment | [GitHub](https://github.com/mooler-z/bipolar) | README + tree + selected files | 17 |
| 23 | [Datehaja](https://vibeapps.dev/s/datehaja) | Social and entertainment | [GitHub](https://github.com/hyochan/Datehaja) | README + tree + selected files | 1 |
| 24 | [Perkdrop.click](https://vibeapps.dev/s/perkdropclick) | Opportunity discovery | [GitHub](https://github.com/sansynx/perkdrop-click) | README + tree + selected files | 2 |
| 25 | [Backpack](https://vibeapps.dev/s/backpack) | Shared group coordination | [GitHub](https://github.com/Elioz404/Backpack) | README + tree + selected files | 2 |
| 26 | [Fillable](https://vibeapps.dev/s/fillable) | Care and healthcare | [GitHub](https://github.com/compiler-aditya/fillable-all-gas) | README + tree + selected files | 1 |
| 27 | [TenantShield](https://vibeapps.dev/s/tenantshield) | Claims and disputes | [GitHub](https://github.com/memeshee/tenantshield) | README + tree + selected files | 2 |
| 28 | [Overlap](https://vibeapps.dev/s/overlap) | Negotiation | [GitHub](https://github.com/compiler-aditya/convex-all-gas) | README + tree + selected files | 2 |
| 29 | [Zabuton](https://vibeapps.dev/s/zabuton) | Civic administration | [GitHub](https://github.com/sneg55/zabuton) | README + tree + selected files | 2 |
| 30 | [ThesisLine](https://vibeapps.dev/s/thesisline) | Research and compliance | [GitHub](https://github.com/himanshu748/thesisline) | README + tree + selected files | 3 |
| 31 | [Attestor](https://vibeapps.dev/s/attestor) | Research and compliance | [GitHub](https://github.com/Bholdguy/attestor) | README + tree + selected files | 1 |
| 32 | [RegVista](https://vibeapps.dev/s/regvista) | Research and compliance | [GitHub](https://github.com/rajgopalakrish/RegVista_CVH) | README + tree + selected files | 1 |
| 33 | [PixelShop — The AI Shopping Network](https://vibeapps.dev/s/pixelshop-the-ai-shopping-network) | Shopping and discovery | [GitHub](https://github.com/hhwjsw711/pixelshop) | README + tree + selected files | 4 |
| 34 | [OFFSCRIPT](https://vibeapps.dev/s/offscript) | Social and entertainment | [GitHub](https://github.com/himanshu748/offscript) | README + tree + selected files | 3 |
| 35 | [Beacon](https://vibeapps.dev/s/beacon) | Lost-pet search | [GitHub](https://github.com/chinesepowered/beacon) | README + tree + selected files | 2 |
| 36 | [One Table](https://vibeapps.dev/s/one-table) | Quotes and procurement | [GitHub](https://github.com/himanshu748/one-table) | README + tree + selected files | 3 |
| 37 | [Might](https://vibeapps.dev/s/might) | Personal companion | [GitHub](https://github.com/Ranopha/might) | README + tree + selected files | 1 |
| 38 | [Claim Check](https://vibeapps.dev/s/claim-check) | Evidence verification | [GitHub](https://github.com/snowphamtom/ceilinggate) | README + tree + selected files | 1 |
| 39 | [CeilingGate](https://vibeapps.dev/s/ceilinggate) | Evidence verification | Not listed | No repository listed | 1 |
| 40 | [still-true](https://vibeapps.dev/s/still-true) | Page and document monitoring | [GitHub](https://github.com/Lokie-ree/still-true) | README + tree + selected files | 3 |
| 41 | [RentPilot](https://vibeapps.dev/s/rentpilot) | Housing and accommodation | [GitHub](https://github.com/himanshu748/rentpilot) | README + tree + selected files | 3 |
| 42 | [Block](https://vibeapps.dev/s/block) | Business outreach | [GitHub](https://github.com/shwetd19/Convex-All-Gas/) | README + tree + selected files | 10 |
| 43 | [NoticeProof](https://vibeapps.dev/s/noticeproof) | Product recalls | [GitHub](https://github.com/tang-vu/noticeproof) | README + tree + selected files | 3 |
| 44 | [Get It in Writing](https://vibeapps.dev/s/get-it-in-writing) | Evidence verification | [GitHub](https://github.com/Joe-Simo/get-it-in-writing) | README + tree + selected files | 1 |
| 45 | [Attest](https://vibeapps.dev/s/attest) | Evidence verification | [GitHub](https://github.com/yaotsakpo/attest) | README + tree + selected files | 2 |
| 46 | [Red Flag](https://vibeapps.dev/s/red-flag) | Workplace information | [GitHub](https://github.com/DarkKingpro10/Red-Flag) | Linked repo returned 404 | 2 |
| 47 | [Recourse](https://vibeapps.dev/s/recourse) | Claims and disputes | [GitHub](https://github.com/Spagero763/recourse) | README + tree + selected files | 4 |
| 48 | [TableForAll](https://vibeapps.dev/s/tableforall) | Food and dining | [GitHub](https://github.com/iamaanahmad/TableForAll) | README + tree + selected files | 3 |

## Competitive implications

| Direction | Existing entries | Implication |
|---|---|---|
| Refund or complaint assistant | Recourse, Duebell, ClaimHero, TenantShield | Source-backed demands and follow-up are already represented. |
| Subscription cancellation | Exorcist, Subzero | Receipt ingestion, renewal tracking and cancellation email are already represented. |
| Quote chasing | Bidzy, Compari, Quote Arena, One Table | Do not claim scope changes or true-cost comparison as an untouched gap. |
| Recall assistance | RecallReady, NoticeProof | Product inventory and verified recall action already exist. |
| Shared household administration | Backpack, OurSpaces, RecallReady | Shared live data alone is not a new product premise. |
| Written evidence and change detection | Get It in Writing, still-true, Pigeon | Citations, requirement checks and meaningful-change emails are baseline competition. |

Recourse source evidence: [reply handling at the inspected commit](https://github.com/Spagero763/recourse/blob/207eca795c756f9c17d959fb4f89465be5db3277/convex/replies.ts). It maps an accepted reply to resolved and clears nudges, while separate manual reopening is available. BackToCard must show item/parcel/payment reconciliation, including partial credits and later reversals, to justify being a distinct app.

## Individual records

Taglines below are author descriptions, not independently verified performance claims. Full extracted descriptions are preserved in the JSON and CSV.

### Found

An accommodation search that helps you research places, find them on the map, and contact them.

- Category: Housing and accommodation.
- [Submission](https://vibeapps.dev/s/found).
- [Listed repository](https://github.com/AdamAmr05/found).
- [Listed live app](https://mellow-hamster-66.convex.site/).
- [Listed video](https://youtu.be/ApUeWdys44Q).
- Static coverage: 509 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/AdamAmr05/found/blob/main/hackathon.md), [convex/schema.ts](https://github.com/AdamAmr05/found/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/AdamAmr05/found/blob/main/convex/convex.config.ts).

### workshop

Stop memorizing how the world works. Start experimenting, breaking things, and learning why they work.

- Category: Learning and simulation.
- [Submission](https://vibeapps.dev/s/workshop).
- [Listed repository](https://github.com/Joystonm/workshop).
- [Listed live app](https://fastidious-elephant-84.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=5KeJykYDkyk).
- Static coverage: 16856 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Joystonm/workshop/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Joystonm/workshop/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Joystonm/workshop/blob/main/convex/convex.config.ts).

### Bidzy

An agent that helps homeowners email contractors for quotes, reads what comes back, and finds the real cheapest price.

- Category: Quotes and procurement.
- [Submission](https://vibeapps.dev/s/bidzy).
- [Listed repository](https://github.com/Kingnanaweb3/bidzy).
- [Listed live app](https://hushed-seahorse-768.convex.site/).
- [Listed video](https://youtu.be/tHs9rsslHYk).
- Static coverage: 199 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Kingnanaweb3/bidzy/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Kingnanaweb3/bidzy/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Kingnanaweb3/bidzy/blob/main/convex/convex.config.ts).
- Review note: The README describes Recyv, while the current submission, schema and hackathon log describe Bidzy. The latter include scope-change and stale-quote handling; README-only review would miss this.

### OurSpaces

One page your whole group can mess with. Everyone's on it at the same time, and it has its own email address.

- Category: Shared group coordination.
- [Submission](https://vibeapps.dev/s/ourspaces).
- [Listed repository](https://github.com/thomasnguyen/ourspaces-app).
- [Listed live app](https://necessary-cobra-892.convex.site/).
- [Listed video](https://youtu.be/0VVFWbfX1QQ).
- Static coverage: 454 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/thomasnguyen/ourspaces-app/blob/main/hackathon.md), [convex/schema.ts](https://github.com/thomasnguyen/ourspaces-app/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/thomasnguyen/ourspaces-app/blob/main/convex/convex.config.ts).

### Subzero

Know what’s renewing. Know how to stop it.

- Category: Subscriptions and cancellation.
- [Submission](https://vibeapps.dev/s/subzero).
- [Listed repository](https://github.com/DammyCodes-all/subzero).
- [Listed live app](https://elated-oriole-157.convex.site/).
- [Listed video](https://youtu.be/xTY-RJFeHZA).
- Static coverage: 293 repository tree entries; 6 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/DammyCodes-all/subzero/blob/master/hackathon.md), [convex/schema.ts](https://github.com/DammyCodes-all/subzero/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/DammyCodes-all/subzero/blob/master/convex/convex.config.ts).
- Review note: Already models subscription evidence, cancellation actions, notifications and Gmail ingestion attempts. Ingestion and reminder reliability alone are not distinctive.

### RecallReady

Forward a receipt. RecallReady identifies the product, watches official recalls, and guides your household to safety.

- Category: Product recalls.
- [Submission](https://vibeapps.dev/s/recallready).
- [Listed repository](https://github.com/demonchant/recallready).
- [Listed live app](https://whimsical-rat-205.convex.site/).
- [Listed video](https://youtu.be/nM_DBjL4IK0).
- Static coverage: 55 repository tree entries; 6 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/demonchant/recallready/blob/main/hackathon.md), [convex/schema.ts](https://github.com/demonchant/recallready/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/demonchant/recallready/blob/main/convex/convex.config.ts).
- Review note: Already models households, products, official recall matches, events and inbound emails. Shared household inventory alone is not distinctive.

### Iris - Your iMessage Thought Partner

Iris is the AI thought partner that lives in iMessage and RCS.

- Category: Personal companion.
- [Submission](https://vibeapps.dev/s/iris-your-imessage-thought-partner).
- [Listed live app](https://chatwithiris.com/).
- No repository link on the retrieved detail page.

### Pigeon

A newsletter for pages that don't have one. Watch any web page, get a plain-language email when it really changes.

- Category: Page and document monitoring.
- [Submission](https://vibeapps.dev/s/pigeon).
- [Listed repository](https://github.com/ref-dev22/pigeon).
- [Listed live app](https://marvelous-dinosaur-465.convex.site/).
- [Listed video](https://youtu.be/M9quyQCpe1Q?si=9defF7qotysTGj0E).
- Static coverage: 55 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/ref-dev22/pigeon/blob/main/hackathon.md), [convex/schema.ts](https://github.com/ref-dev22/pigeon/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/ref-dev22/pigeon/blob/main/convex/convex.config.ts).

### Jamanyo

Jamanyo is an AI car scout that only calls a listing a lead when the evidence backs it up, with email delivery built on AgentMail.

- Category: Shopping and discovery.
- [Submission](https://vibeapps.dev/s/jamanyo).
- [Listed repository](https://github.com/eugene-tulu/convexallgas).
- [Listed live app](https://fine-fish-527.convex.site/).
- [Listed video](https://youtu.be/pIHbwgOvZwg).
- Static coverage: 150 repository tree entries; 4 selected files retrieved; root README unavailable.
- Inspected artifacts: [hackathon.md](https://github.com/eugene-tulu/convexallgas/blob/main/hackathon.md), [convex/schema.ts](https://github.com/eugene-tulu/convexallgas/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/eugene-tulu/convexallgas/blob/main/convex/convex.config.ts).
- Review note: The root README endpoint returned 404, but the public file tree, schema, package and hackathon log were retrieved. The description discloses a model-provider fallback and controlled email testing; sponsor tags are not runtime proof.

### ClaimHero

ClaimHero turns insurance denials into cited appeals with policy research, missing-proof detection, and human-approved delivery.

- Category: Claims and disputes.
- [Submission](https://vibeapps.dev/s/claimhero).
- [Listed repository](https://github.com/zaikaman/ClaimHero).
- [Listed live app](https://kindhearted-elephant-992.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=M04LMuJRilg).
- Static coverage: 635 repository tree entries; 3 selected files retrieved; root README retrieved.
- Inspected artifacts: [convex/schema.ts](https://github.com/zaikaman/ClaimHero/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/zaikaman/ClaimHero/blob/main/convex/convex.config.ts).

### Carter

Curious about what you want. Relentless about finding it.

- Category: Shopping and discovery.
- [Submission](https://vibeapps.dev/s/carter).
- [Listed repository](https://github.com/andersjbe/carter-ai).
- [Listed live app](https://ardent-bandicoot-155.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=zgS6NWyqzFE).
- Static coverage: 335 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/andersjbe/carter-ai/blob/main/hackathon.md), [convex/schema.ts](https://github.com/andersjbe/carter-ai/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/andersjbe/carter-ai/blob/main/convex/convex.config.ts).

### Compari

Price quoting made easy

- Category: Quotes and procurement.
- [Submission](https://vibeapps.dev/s/compari).
- [Listed repository](https://github.com/kotarCreative/compari).
- [Listed live app](https://enduring-husky-65.convex.site/).
- [Listed video](https://www.loom.com/share/6c39274f0ff84618b1da8e60d2f60327).
- Static coverage: 241 repository tree entries; 4 selected files retrieved; root README unavailable.
- Inspected artifacts: [hackathon.md](https://github.com/kotarCreative/compari/blob/main/hackathon.md), [convex/schema.ts](https://github.com/kotarCreative/compari/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/kotarCreative/compari/blob/main/convex/convex.config.ts).
- Review note: The root README endpoint returned 404, but the public file tree and selected source were retrieved. The author describes difficulty obtaining real vendor replies.

### Faultline

Your landlord told the city it's fixed. Is it? Say so in your own words; we keep it dated and tell you if the city agrees.

- Category: Housing and accommodation.
- [Submission](https://vibeapps.dev/s/faultline).
- [Listed repository](https://gitlab.com/ndivij2004/faultline).
- [Listed live app](https://clear-dogfish-72.convex.site/).
- [Listed video](https://youtu.be/Xa8uKOZP-Y4).
- Static coverage: rendered GitLab README and visible root tree; no recursive source-file audit. The README describes a tenant repair-evidence and city-certification response loop. Implementation and deployment claims were not executed.
- [Retrieved README](https://gitlab.com/ndivij2004/faultline/-/blob/main/README.md); observed commit `60f1352da8e6e99c7ccfccf0099dd5ee14ca9e84`.

### Duebell

Peru gives companies 15 business days to answer a consumer complaint. Duebell keeps the clock, reads the reply and drafts your filing.

- Category: Claims and disputes.
- [Submission](https://vibeapps.dev/s/duebell).
- [Listed repository](https://github.com/kasbsquall/duebell).
- [Listed live app](https://sleek-grouse-640.convex.site/).
- [Listed video](https://youtu.be/dViTfHukVrc).
- Static coverage: 183 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/kasbsquall/duebell/blob/main/hackathon.md), [convex/schema.ts](https://github.com/kasbsquall/duebell/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/kasbsquall/duebell/blob/main/convex/convex.config.ts).

### MP3ToText

Online MP3 to text—upload audio and export in multiple formats.

- Category: Transcription.
- [Submission](https://vibeapps.dev/s/mp3totext).
- [Listed live app](https://mp3totext.io/).
- [Listed video](https://www.youtube.com/watch?v=axAFqWB9vkw).
- No repository link on the retrieved detail page.

### SafePlate

Eating out with a serious food allergy — it reads the real menu and asks the kitchen what the menu cannot answer.

- Category: Food and dining.
- [Submission](https://vibeapps.dev/s/safeplate).
- [Listed repository](https://github.com/chinesepowered/safeplate).
- [Listed live app](https://valiant-fox-223.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=nzArirVettI).
- Static coverage: 112 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/chinesepowered/safeplate/blob/master/hackathon.md), [convex/schema.ts](https://github.com/chinesepowered/safeplate/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/chinesepowered/safeplate/blob/master/convex/convex.config.ts).
- Review note: The current detail description is only a short tagline; repository material supplements it.

### Exorcist

Find what is haunting your card. Forward your receipts and it cancels what you forgot about.

- Category: Subscriptions and cancellation.
- [Submission](https://vibeapps.dev/s/exorcist).
- [Listed repository](https://github.com/chinesepowered/exorcist).
- [Listed live app](https://adventurous-caribou-217.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=An1iPgCm6CU).
- Static coverage: 114 repository tree entries; 6 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/chinesepowered/exorcist/blob/master/hackathon.md), [convex/schema.ts](https://github.com/chinesepowered/exorcist/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/chinesepowered/exorcist/blob/master/convex/convex.config.ts).
- Review note: Already provides a forwarded-receipt ledger, merchant research, approved correspondence and cancellation classification.

### Quote Arena

Post a home repair job once. It finds contractors, emails them all, and ranks what comes back.

- Category: Quotes and procurement.
- [Submission](https://vibeapps.dev/s/quote-arena).
- [Listed repository](https://github.com/chinesepowered/quote-arena).
- [Listed live app](https://polished-dragon-158.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=dixtNz7GDkU).
- Static coverage: 125 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/chinesepowered/quote-arena/blob/master/hackathon.md), [convex/schema.ts](https://github.com/chinesepowered/quote-arena/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/chinesepowered/quote-arena/blob/master/convex/convex.config.ts).

### After

When someone dies there are forty companies to tell. After finds each process, writes the letters, and tracks them.

- Category: Life administration.
- [Submission](https://vibeapps.dev/s/after).
- [Listed repository](https://github.com/chinesepowered/after).
- [Listed live app](https://kindred-guanaco-234.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=eZ8eIKz-_tc).
- Static coverage: 127 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/chinesepowered/after/blob/master/hackathon.md), [convex/schema.ts](https://github.com/chinesepowered/after/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/chinesepowered/after/blob/master/convex/convex.config.ts).

### Ombuds

Public records tell you if a care home is safe. Only email tells you if it's available. Ombuds does both, and takes nothing from facilities.

- Category: Care and healthcare.
- [Submission](https://vibeapps.dev/s/ombuds).
- [Listed repository](https://github.com/Shyam-Raghuwanshi/Ombuds).
- [Listed live app](https://flexible-reindeer-206.convex.site/).
- [Listed video](https://youtu.be/VErPwL-xLYw).
- Static coverage: 73 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Shyam-Raghuwanshi/Ombuds/blob/master/hackathon.md), [convex/schema.ts](https://github.com/Shyam-Raghuwanshi/Ombuds/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/Shyam-Raghuwanshi/Ombuds/blob/master/convex/convex.config.ts).

### Opportunity Scout

Choose a hackathon worth your time, with source evidence, honest unknowns and a personal shortlist.

- Category: Opportunity discovery.
- [Submission](https://vibeapps.dev/s/opportunity-scout).
- [Listed repository](https://github.com/himanshu748/opportunity-scout-convex).
- [Listed live app](https://graceful-spoonbill-850.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=vnmZcJOoM6o).
- Static coverage: 105 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/himanshu748/opportunity-scout-convex/blob/main/hackathon.md), [convex/schema.ts](https://github.com/himanshu748/opportunity-scout-convex/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/himanshu748/opportunity-scout-convex/blob/main/convex/convex.config.ts).

### bipolar

Vote love or hate on polarizing topics, then see how the rest of the world voted — country by country.

- Category: Social and entertainment.
- [Submission](https://vibeapps.dev/s/bipolar).
- [Listed repository](https://github.com/mooler-z/bipolar).
- [Listed live app](https://vivid-greyhound-473.convex.site/).
- [Listed video](https://drive.google.com/file/d/1xZU_HiHnRfIeF6y7vDF-WBJeRvqJAGDQ/view?usp=sharing).
- Static coverage: 389 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/mooler-z/bipolar/blob/main/hackathon.md), [convex/schema.ts](https://github.com/mooler-z/bipolar/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/mooler-z/bipolar/blob/main/convex/convex.config.ts).

### Datehaja

My second self dates for me, remembers my corrections, and returns with an honest read. Contact opens only after two human yeses.

- Category: Social and entertainment.
- [Submission](https://vibeapps.dev/s/datehaja).
- [Listed repository](https://github.com/hyochan/Datehaja).
- [Listed live app](https://merry-bass-190.convex.site/).
- [Listed video](https://youtu.be/qu1VWBXuIz8).
- Static coverage: 555 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/hyochan/Datehaja/blob/main/hackathon.md), [convex/schema.ts](https://github.com/hyochan/Datehaja/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/hyochan/Datehaja/blob/main/convex/convex.config.ts).

### Perkdrop.click

A moderated catalog of free credits and programs, with the original provider claim page

- Category: Opportunity discovery.
- [Submission](https://vibeapps.dev/s/perkdropclick).
- [Listed repository](https://github.com/sansynx/perkdrop-click).
- [Listed live app](https://perkdrop-click.sanathr106.chatgpt.site/).
- [Listed video](https://youtu.be/DCb3a0kDiXo).
- Static coverage: 85 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/sansynx/perkdrop-click/blob/master/hackathon.md), [convex/schema.ts](https://github.com/sansynx/perkdrop-click/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/sansynx/perkdrop-click/blob/master/convex/convex.config.ts).

### Backpack

Everything your school sends — the site, the newsletters, the mail — as one shared list of what your family actually has to do.

- Category: Shared group coordination.
- [Submission](https://vibeapps.dev/s/backpack).
- [Listed repository](https://github.com/Elioz404/Backpack).
- [Listed live app](https://resilient-mastiff-559.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=Mu_FvHAuK9E).
- Static coverage: 79 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Elioz404/Backpack/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Elioz404/Backpack/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Elioz404/Backpack/blob/main/convex/convex.config.ts).

### Fillable

Know your exact medication’s reported supply, follow changes, and bring clearer questions to your pharmacist.

- Category: Care and healthcare.
- [Submission](https://vibeapps.dev/s/fillable).
- [Listed repository](https://github.com/compiler-aditya/fillable-all-gas).
- [Listed live app](https://wandering-hawk-899.convex.site/).
- [Listed video](https://youtu.be/x4KFO5PQ6Vw).
- Static coverage: 152 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/compiler-aditya/fillable-all-gas/blob/main/hackathon.md), [convex/schema.ts](https://github.com/compiler-aditya/fillable-all-gas/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/compiler-aditya/fillable-all-gas/blob/main/convex/convex.config.ts).

### TenantShield

Demand letters that cite the right clause by number, then chase the landlord until they answer.

- Category: Claims and disputes.
- [Submission](https://vibeapps.dev/s/tenantshield).
- [Listed repository](https://github.com/memeshee/tenantshield).
- [Listed live app](https://confident-bass-919.convex.site/).
- [Listed video](https://youtu.be/s_9u-okSGu4).
- Static coverage: 38 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/memeshee/tenantshield/blob/main/hackathon.md), [convex/schema.ts](https://github.com/memeshee/tenantshield/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/memeshee/tenantshield/blob/main/convex/convex.config.ts).

### Overlap

Two agents. Two private limits. A deal neither side had to reveal.

- Category: Negotiation.
- [Submission](https://vibeapps.dev/s/overlap).
- [Listed repository](https://github.com/compiler-aditya/convex-all-gas).
- [Listed live app](https://expert-wolverine-992.convex.site/).
- [Listed video](https://youtu.be/v7oj3IR8W8g).
- Static coverage: 106 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/compiler-aditya/convex-all-gas/blob/main/hackathon.md), [convex/schema.ts](https://github.com/compiler-aditya/convex-all-gas/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/compiler-aditya/convex-all-gas/blob/main/convex/convex.config.ts).

### Zabuton

Point it at a city’s website. It reads every board, commission and term, then keeps the roster current.

- Category: Civic administration.
- [Submission](https://vibeapps.dev/s/zabuton).
- [Listed repository](https://github.com/sneg55/zabuton).
- [Listed live app](https://original-spoonbill-489.convex.site/).
- [Listed video](https://youtu.be/wl5ynsKpY8k).
- Static coverage: 123 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/sneg55/zabuton/blob/main/hackathon.md), [convex/schema.ts](https://github.com/sneg55/zabuton/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/sneg55/zabuton/blob/main/convex/convex.config.ts).

### ThesisLine

Follow Indian-stock research questions through official disclosures, quoted evidence and verified alerts.

- Category: Research and compliance.
- [Submission](https://vibeapps.dev/s/thesisline).
- [Listed repository](https://github.com/himanshu748/thesisline).
- [Listed live app](https://resolute-akita-616.convex.site/).
- [Listed video](https://drive.google.com/file/d/1dUeHLHe0Lagy2sREmg5PRBxu3pppB1tw/view).
- Static coverage: 61 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/himanshu748/thesisline/blob/main/hackathon.md), [convex/schema.ts](https://github.com/himanshu748/thesisline/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/himanshu748/thesisline/blob/main/convex/convex.config.ts).

### Attestor

A license-trust supervisor that catches stale, misidentified, or invalid healthcare licenses before a staffing decision relies on them.

- Category: Research and compliance.
- [Submission](https://vibeapps.dev/s/attestor).
- [Listed repository](https://github.com/Bholdguy/attestor).
- [Listed live app](https://brazen-snail-826.convex.site/).
- [Listed video](https://x.com/bholdguy/status/2098441580772303076).
- Static coverage: 132 repository tree entries; 3 selected files retrieved; root README retrieved.
- Inspected artifacts: [convex/schema.ts](https://github.com/Bholdguy/attestor/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Bholdguy/attestor/blob/main/convex/convex.config.ts).

### RegVista

Regulatory intelligence that maps a company's exposure, connects regimes to source-backed findings, and tracks developments

- Category: Research and compliance.
- [Submission](https://vibeapps.dev/s/regvista).
- [Listed repository](https://github.com/rajgopalakrish/RegVista_CVH).
- [Listed live app](https://brilliant-roadrunner-68.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=dDjU7qFdHY8).
- Static coverage: 35 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/rajgopalakrish/RegVista_CVH/blob/claude/regvista-convex-hackathon-jh2g5y/hackathon.md), [convex/schema.ts](https://github.com/rajgopalakrish/RegVista_CVH/blob/claude/regvista-convex-hackathon-jh2g5y/convex/schema.ts), [convex/convex.config.ts](https://github.com/rajgopalakrish/RegVista_CVH/blob/claude/regvista-convex-hackathon-jh2g5y/convex/convex.config.ts).

### PixelShop — The AI Shopping Network

Any product on the internet, turned into a live shopping channel — written, produced, and aired by AI while you watch.

- Category: Shopping and discovery.
- [Submission](https://vibeapps.dev/s/pixelshop-the-ai-shopping-network).
- [Listed repository](https://github.com/hhwjsw711/pixelshop).
- [Listed live app](https://fearless-otter-334.convex.site/).
- [Listed video](https://youtu.be/dBYvrjQv2sg).
- Static coverage: 27 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/hhwjsw711/pixelshop/blob/master/hackathon.md), [convex/schema.ts](https://github.com/hhwjsw711/pixelshop/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/hhwjsw711/pixelshop/blob/master/convex/convex.config.ts).

### OFFSCRIPT

A two-player browser mystery. You have half the story; your friend has the rest.

- Category: Social and entertainment.
- [Submission](https://vibeapps.dev/s/offscript).
- [Listed repository](https://github.com/himanshu748/offscript).
- [Listed live app](https://flexible-kiwi-480.convex.site/).
- [Listed video](https://drive.google.com/file/d/1oCSR-ZezcXE7-KGd8ocpVDYaNc-yos20/view).
- Static coverage: 73 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/himanshu748/offscript/blob/main/hackathon.md), [convex/schema.ts](https://github.com/himanshu748/offscript/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/himanshu748/offscript/blob/main/convex/convex.config.ts).

### Beacon

A lost pet report becomes a search that never sleeps — crawling shelters, matching, and emailing.

- Category: Lost-pet search.
- [Submission](https://vibeapps.dev/s/beacon).
- [Listed repository](https://github.com/chinesepowered/beacon).
- [Listed live app](https://moonlit-ferret-277.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=MMXR0BWSom4).
- Static coverage: 124 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/chinesepowered/beacon/blob/master/hackathon.md), [convex/schema.ts](https://github.com/chinesepowered/beacon/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/chinesepowered/beacon/blob/master/convex/convex.config.ts).

### One Table

Compare venue quotes with minimums, taxes and missing costs in view.

- Category: Quotes and procurement.
- [Submission](https://vibeapps.dev/s/one-table).
- [Listed repository](https://github.com/himanshu748/one-table).
- [Listed live app](https://wooden-dogfish-387.convex.site/).
- [Listed video](https://drive.google.com/file/d/1qAw_Xku8fSNFyYdR0S0IB-yiSE2-aiKD/view).
- Static coverage: 102 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/himanshu748/one-table/blob/main/hackathon.md), [convex/schema.ts](https://github.com/himanshu748/one-table/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/himanshu748/one-table/blob/main/convex/convex.config.ts).

### Might

You have more to offer than you know. Might finds where it matters.

- Category: Personal companion.
- [Submission](https://vibeapps.dev/s/might).
- [Listed repository](https://github.com/Ranopha/might).
- [Listed live app](https://hushed-stork-401.convex.site/).
- [Listed video](https://youtu.be/VjZp9nPWEEU).
- Static coverage: 208 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Ranopha/might/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Ranopha/might/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Ranopha/might/blob/main/convex/convex.config.ts).

### Claim Check

Claim Check — claimed ≤ receipt (C ≤ S) → GRANT or REFUSE, line by line.

- Category: Evidence verification.
- [Submission](https://vibeapps.dev/s/claim-check).
- [Listed repository](https://github.com/snowphamtom/ceilinggate).
- [Listed live app](https://snowphamtom.github.io/ceilinggate/).
- [Listed video](https://www.youtube.com/watch?v=hDnY3_iszX4).
- Static coverage: 320 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/snowphamtom/ceilinggate/blob/master/hackathon.md), [convex/schema.ts](https://github.com/snowphamtom/ceilinggate/blob/master/convex/schema.ts), [convex/convex.config.ts](https://github.com/snowphamtom/ceilinggate/blob/master/convex/convex.config.ts).
- Review note: This entry explicitly links snowphamtom/ceilinggate. The separately listed CeilingGate entry has no repository link; this audit does not copy the link across entries.

### CeilingGate

Email a public receipt. Get GRANT or the line that is over.

- Category: Evidence verification.
- [Submission](https://vibeapps.dev/s/ceilinggate).
- [Listed live app](https://quirky-rhinoceros-204.convex.site/).
- No repository link on the retrieved detail page.
- Review note: No repository listed on this detail page. Similar naming or a shared author is not treated as a repository link.

### still-true

Forward a document. It tells you what it never says — and how many lines it read before saying so.

- Category: Page and document monitoring.
- [Submission](https://vibeapps.dev/s/still-true).
- [Listed repository](https://github.com/Lokie-ree/still-true).
- [Listed live app](https://impressive-marten-163.convex.site/).
- [Listed video](https://youtu.be/HofqXKI8KJs).
- Static coverage: 83 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Lokie-ree/still-true/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Lokie-ree/still-true/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Lokie-ree/still-true/blob/main/convex/convex.config.ts).
- Review note: Already watches source documents and checks changes to cited clauses, in addition to extracting obligations and document silence.

### RentPilot

Find room leads by area, budget and must-haves, then track listing evidence, approved inquiries and replies.

- Category: Housing and accommodation.
- [Submission](https://vibeapps.dev/s/rentpilot).
- [Listed repository](https://github.com/himanshu748/rentpilot).
- [Listed live app](https://ceaseless-pigeon-981.convex.site/).
- [Listed video](https://youtu.be/TjNKa9jboJo).
- Static coverage: 84 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/himanshu748/rentpilot/blob/main/hackathon.md), [convex/schema.ts](https://github.com/himanshu748/rentpilot/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/himanshu748/rentpilot/blob/main/convex/convex.config.ts).

### Block

Drop your business link — an AI agent maps your competitors and customers, drafts outreach, and works every lead for you.

- Category: Business outreach.
- [Submission](https://vibeapps.dev/s/block).
- [Listed repository](https://github.com/shwetd19/Convex-All-Gas/).
- [Listed live app](https://flippant-stork-696.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=kHp2UfkJ9G8).
- Static coverage: 187 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/shwetd19/Convex-All-Gas/blob/main/hackathon.md), [convex/schema.ts](https://github.com/shwetd19/Convex-All-Gas/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/shwetd19/Convex-All-Gas/blob/main/convex/convex.config.ts).

### NoticeProof

Forward a recall notice. NoticeProof verifies every claim and switches you to an independently trusted contact - before you click.

- Category: Product recalls.
- [Submission](https://vibeapps.dev/s/noticeproof).
- [Listed repository](https://github.com/tang-vu/noticeproof).
- [Listed live app](https://lovely-eel-809.convex.site/).
- [Listed video](https://youtu.be/KX4xkUp6Qm8).
- Static coverage: 189 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/tang-vu/noticeproof/blob/main/hackathon.md), [convex/schema.ts](https://github.com/tang-vu/noticeproof/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/tang-vu/noticeproof/blob/main/convex/convex.config.ts).

### Get It in Writing

Don't rely on "probably." See what an official page actually promises — and get the gap confirmed in writing.

- Category: Evidence verification.
- [Submission](https://vibeapps.dev/s/get-it-in-writing).
- [Listed repository](https://github.com/Joe-Simo/get-it-in-writing).
- [Listed live app](https://resilient-salamander-937.convex.site/).
- [Listed video](https://youtu.be/aXTCeEUKq5Q).
- Static coverage: 101 repository tree entries; 6 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Joe-Simo/get-it-in-writing/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Joe-Simo/get-it-in-writing/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Joe-Simo/get-it-in-writing/blob/main/convex/convex.config.ts).
- Review note: Already models individual requirements, proof items and reply outcomes. Granular evidence checking alone is not a new distinction.

### Attest

An assistant on your inbox that says yes to the verified recruiter and the small invoice, and no to the SSN scam and the unverified wire.

- Category: Evidence verification.
- [Submission](https://vibeapps.dev/s/attest).
- [Listed repository](https://github.com/yaotsakpo/attest).
- [Listed live app](https://dynamic-egret-864.convex.site/).
- [Listed video](https://www.loom.com/share/9c1e3c56fbea4d22948c41fac86392b3).
- Static coverage: 134 repository tree entries; 4 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/yaotsakpo/attest/blob/main/hackathon.md), [convex/schema.ts](https://github.com/yaotsakpo/attest/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/yaotsakpo/attest/blob/main/convex/convex.config.ts).

### Red Flag

Una plataforma donde los trabajadores exponen anonimamente el ambiente real de empresas y sucursales para orientar a quienes buscan empleo

- Category: Workplace information.
- [Submission](https://vibeapps.dev/s/red-flag).
- [Listed repository](https://github.com/DarkKingpro10/Red-Flag).
- [Listed live app](https://red-flag-btuq.vercel.app/).
- [Listed video](https://drive.google.com/file/d/1I9gE-QXpfXmv7z3ttUA5mtBh-Zxw7qxJ/view?usp=drivesdk).
- Review note: The linked GitHub repository returned 404 to this audit. Its public availability is unverified; the reason is unknown.

### Recourse

Pursue what you're owed, citing the clause that entitles you to it.

- Category: Claims and disputes.
- [Submission](https://vibeapps.dev/s/recourse).
- [Listed repository](https://github.com/Spagero763/recourse).
- [Listed live app](https://hearty-lobster-443.convex.site/).
- [Listed video](https://www.youtube.com/watch?v=slCpqIoOOrg).
- Static coverage: 141 repository tree entries; 9 selected files retrieved; root README retrieved.
- Inspected artifacts: [hackathon.md](https://github.com/Spagero763/recourse/blob/main/hackathon.md), [convex/schema.ts](https://github.com/Spagero763/recourse/blob/main/convex/schema.ts), [convex/convex.config.ts](https://github.com/Spagero763/recourse/blob/main/convex/convex.config.ts).
- Review note: Closest competitor. At the inspected commit, an accepted reply resolves the case and clears nudges. Manual reopening exists. The inspected schema has no separate purchase-item, parcel or payment-event records.

### TableForAll

Email replies become a cited dinner shortlist. Guests install nothing.

- Category: Food and dining.
- [Submission](https://vibeapps.dev/s/tableforall).
- [Listed repository](https://github.com/iamaanahmad/TableForAll).
- [Listed live app](https://aware-shark-108.convex.site/).
- [Listed video](https://youtu.be/bdyDmLJKL0w).
- Static coverage: 30 repository tree entries; 2 selected files retrieved; root README retrieved.
- Inspected artifacts: [convex/schema.ts](https://github.com/iamaanahmad/TableForAll/blob/main/convex/schema.ts).
- Review note: The inspected README describes a preview mode. Source code presence does not prove the public deployment executes every integration.

## Retrieval and reproducibility

- Raw listing, all detail responses, repository audit and selected source downloads: `.firecrawl/audit-2026-09-20/`.
- `current_submissions.json` preserves detail retrieval timestamps, source files and Firecrawl scrape IDs where returned.
- `repository_audit.json` records GitHub metadata/tree/README availability; `source_audit.json` records file paths, blob SHAs and fetch outcomes.
- The public JSON and CSV preserve all 48 descriptions and submitted links. They do not replace absent repository links with guesses.
- No inference is made about why a GitHub request returned 404.
