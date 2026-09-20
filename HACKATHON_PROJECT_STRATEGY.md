# Hackathon project decision: BidPatch

Update, September 20, 2026: the subsequent recent-community research recommends TransferPacket for a solo builder without an estimator partner. See [the updated decision](HACKATHON_LAST30DAYS_DECISION.md). This earlier report preserves the construction research and conditional BidPatch option.

Research date: September 20, 2026. This is a concept recommendation, not a built app or a prediction of winning. Research used Firecrawl, the supplied submission descriptions, official event criteria, public project documents, and existing product pages. No users or suppliers were contacted.

## Recommendation

Build a narrowly scoped web application for a small contractor or estimator: **BidPatch catches a written bid change, identifies the supplier quote that no longer covers it, and tracks the revision until the user confirms it is resolved.**

Pitch: “The project changed. Your supplier quote didn’t. BidPatch shows the gap and helps you close it before you bid.”

This is the strongest researched fit for research → evidence → email → follow-up. Choose it only after showing one realistic case to an estimator, contractor, or supplier. If that audience is inaccessible, StallReady, described below, is the easier validation alternative. Neither idea has established willingness to pay or proven market originality.

## What the existing submissions teach

The local inventory contains strong concepts, especially specific problems with observable outcomes. Quoting, consumer claims, generic sourcing, and verification of website promises recur frequently. Examples include Compari, Quote Arena, One Table, ClaimHero, TenantShield, Recourse, SafePlate, and Get It in Writing.

These are assessments of descriptions, not implementation reviews. Identical sponsor tags, truncated summaries, and malformed creator fields make the dataset unsuitable as proof of working integrations.

The earlier SlotBack recommendation is weaker for this particular brief: filling a workshop cancellation is useful, but a workshop's own waitlist rarely needs substantial web research. Its Firecrawl use risks being incidental.

## Debate and evidence

| Candidate | Real job | Strongest argument | Reason to downgrade |
|---|---|---|---|
| BidPatch | Update a supplier quote after a bid requirement changes | Each step affects a pending decision; the evidence and unresolved dependency are visible | Requires domain feedback, reliable scope matching, and accessible documents |
| StallReady | Help a maker determine whether a market fits and resolve application blockers | Understandable audience, public requirements, specific organiser questions | Can collapse into a checklist; existing event platforms cover applications and communication |
| CareSlot | Reconcile childcare requirements against websites and provider replies | Meaningful family problem and natural email clarification | Winnie, Kinside, and Upwards already cover substantial discovery/availability workflows; replies may take days |
| PartProof | Resolve uncertain replacement-part compatibility | Tangible mistake prevention and evidence-led supplier inquiry | FixPart already accepts model-plate photos and provides part assistance; common cases are self-service |
| SlotBack | Fill a cancelled workshop seat | Excellent shared-state and double-booking demonstration | Research is rarely necessary to the central job |

This is a qualitative judgment, not the organisers' scoring system or an exhaustive competitor audit.

### BidPatch: primary evidence

[James City County's Old News Road Addendum 2](https://www.jamescitycountyva.gov/DocumentCenter/View/872/IFB-11-4579-Addendum-2-PDF), dated June 21, 2012, explicitly changes a 12-inch concrete-pipe quantity from 96 to 122 linear feet. Its revised table also gives 122 LF. This is an archival example, not a current opportunity. The original bid file was not separately retrieved; the addendum states both values.

[Springfield's Addendum 3](https://springfield-or.gov/wp-content/uploads/2022/08/S3087-Addendum-3.pdf), dated August 5, 2022, explicitly changes a ceiling-texture quantity from 3,200 to 5,000 square feet. Firecrawl successfully extracted all eight pages. This supports the feasibility of extracting explicit changes from real written addenda; it does not establish reliable coverage of arbitrary bid packages.

[Long Beach's amendment history](https://longbeachbuys.buyspeed.com/bso/external/bidDetail.sdo?docId=PW-26-759) illustrates a failure mode: quantity changes can accompany description and unit changes. Matching rows solely by their position can create a false discrepancy. Match scope description, specification and unit; flag ambiguity for review.

Existing competition is substantial. [PlanHub for subcontractors](https://planhub.com/subcontractors/) includes document search, supplier estimate requests, communications, stages and reminders. [PlanHub for general contractors](https://planhub.com/general-contractors/) includes follow-ups and bid coordination. These pages do not establish whether the exact proposed reconciliation workflow is absent. Do not claim exclusivity.

### StallReady: credible alternative

[Retropolitan's vendor FAQ](https://www.retropolitancraft.com/vendors/faqs) explains that electricity is limited, carries an additional fee, and that vehicle/trailer setups need specific email discussion. This gives a legitimate research-to-question workflow.

[Crafty Wonderland's FAQ](https://craftywonderland.com/pages/faq) publishes application dates, product restrictions, fees and closed-application rules. A useful assistant should answer documented questions from the source and honour a closed application period, rather than generate unnecessary outreach.

[Marketspread](https://marketspread.com/manage/events/) already covers extensive vendor records, documents and communication. The proposed distinction is a seller's evidence-backed comparison across independent markets, including unresolved requirements. That distinction remains a hypothesis requiring user validation.

### Why the other candidates lost

[FixPart](https://fixpart.co.uk/vacuum-cleaner-spare-parts) already provides model-specific searching and assistance using a photo of a model plate plus a part description. [Winnie](https://winnie.com/), [Kinside](https://www.kinside.com/), and [Upwards](https://upwards.com/childcare-near-me) advertise substantial childcare discovery, availability or matching services. Their existence validates demand for the broad jobs, but makes a generic recreation a weak differentiation strategy.

## Product scope

Target one estimator or small contractor coordinating an existing supplier relationship. Begin with one trade, one public project page, explicit written addenda, and a supplier quote pasted as text. Automatic drawing interpretation and arbitrary scanned-document support are outside the first version.

Core screens:

1. **Project:** public source URL, selected scope, deadline, supplier quote and current revision.
2. **Evidence:** exact change passage, source document, retrieval time, unit, old/new values, and affected quote passage.
3. **Resolution:** reviewed inquiry, email thread, outstanding facts and status history.

Core workflow:

1. Firecrawl reads the project page and selected linked addenda.
2. OpenAI proposes structured changes and links them to source passages.
3. Deterministic checks validate units and calculate explicit numeric differences; uncertain scope matches remain review items.
4. The user confirms the match and approves an email to their supplier.
5. AgentMail receives the reply; the app extracts each answered field and preserves the message as evidence.
6. A partial reply leaves the case open and produces a specific missing-field follow-up.
7. A complete response is presented to the user for resolution. It does not automatically certify the whole bid.

Suggested states: detected → reviewed → request approved → awaiting reply → incomplete reply → ready for user review → resolved. A new source revision reopens relevant cases.

## Why each sponsor is necessary

| Technology | Product role | Visible demonstration |
|---|---|---|
| Firecrawl | Read public project pages and written changes, preserving source material | Judge opens the passage behind the mismatch |
| OpenAI | Interpret change text and supplier replies into structured proposed facts | A reply with a new price still leaves delivery timing unanswered |
| AgentMail | Send approved inquiries and receive the actual reply thread | Real inbound email updates the case |
| Convex | Maintain revision-linked cases, shared live state, webhook deduplication and scheduled follow-ups | Two views update together; duplicate or stale replies do not incorrectly resolve the case |

Design the data around cases and evidence, not chat messages alone. Suggested entities are projects, source revisions, requirements, quote versions, evidence references, email threads and follow-up jobs.

Tie every inquiry to the requirement revision it asks about. A reply confirming revision 1 must not silently resolve revision 2. Follow-up execution must recheck current case state before sending. These are meaningful correctness behaviours, not decorative backend features.

## Under-three-minute demo

Use an explicitly labelled historical case and sample supplier quote. Use real Firecrawl and email calls with controlled, consented demo inboxes. Identify accelerated timers or previously captured results clearly.

| Time | Action |
|---|---|
| 0:00–0:20 | State the problem and show the sample quote for 96 LF |
| 0:20–0:50 | Read the real archived addendum: requirement is now 122 LF |
| 0:50–1:15 | Show the exact evidence and calculated 26 LF gap; approve the supplier inquiry |
| 1:15–1:45 | Send a test supplier reply confirming revised quantity and price, but omit delivery timing |
| 1:45–2:15 | Show the live case remaining incomplete; review a follow-up asking only about delivery |
| 2:15–2:40 | Receive the missing answer, review it, and resolve the case; show the reminder cancelled |
| 2:40–2:55 | State the supported scope and show actual pilot feedback, if obtained |

Do not imply that an independent supplier replied instantly or that a demonstrated quantity gap equals money saved. If validation has not happened, say so.

## Build and validation plan

The official deadline is September 22 at noon Pacific (September 23 at 00:30 IST), so scope matters more than breadth.

- **First 2 hours:** show the source-and-quote example to a reachable estimator or contractor. Ask how they currently handle revisions, what they would need to trust a flag, and whether supplier email is their actual channel. Confirm that public project documents are accessible.
- **Next 10 hours:** build the smallest real vertical flow: source → reviewed mismatch → approved email → reply → live case update.
- **Next 8 hours:** implement partial-answer handling, source revisions, deduplicated inbound events, follow-up cancellation and human resolution.
- **Next 6 hours:** run three representative cases with the collaborator; correct the most consequential failure rather than adding another feature.
- **Remaining time:** deploy, prepare an accessible sample walkthrough, record the demo, document limitations, complete the build log and submission, and publish a factual build post yourself.

Meaningful verification cases: explicit 96→122 change; unchanged quantity; unit mismatch; reordered rows; ambiguous item match; duplicate webhook; incomplete reply; reply to superseded revision; resolved case with a queued reminder. Report measured outcomes only, such as correct flags on a disclosed test set, actual time for a user to identify the affected quote, and unanswered fields caught.

The validation gate is practical: if a reachable user does not recognise the pain, or the relevant information is trapped in inaccessible portals/drawings, do not spend the remaining build time polishing this concept. Switch to a supported workflow with a reachable user, such as StallReady for a maker comparing real upcoming markets.

## Submission alignment

The [official AllGas page](https://www.convex.dev/hackathons/all-gas) rewards useful everyday apps, creativity, meaningful Convex usage, working sponsor integrations, social engagement and a video under three minutes. It requires a public repository, hackathon.md, an accessible convex.site or chatgpt.site deployment and a submission before the deadline. The app must meet the event's new-build eligibility rules.

For social proof, obtain specific feedback from an actual user, with permission to quote it. A clear before/after clip and one witnessed use case are stronger product evidence than invented traction. The organiser's social-engagement criterion remains a separate submission consideration.

No app, pilot, interview, email campaign, social post or submission has been created by this research task.
