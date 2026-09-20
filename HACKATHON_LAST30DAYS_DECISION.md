# Hackathon decision after recent-community research

September 20 follow-up: the user's broader-audience requirement and the fresh 48-submission repository audit produced a new recommendation, [BackToCard](BACKTOCARD_PROJECT_DECISION.md). This file preserves the earlier student-focused option.

Research completed September 20, 2026. Requested window: August 21 through September 20, 2026. This updates the earlier BidPatch recommendation in HACKATHON_PROJECT_STRATEGY.md. No app was built and no students, schools, parents, suppliers, or organisers were contacted.

## Recommendation

**Build TransferPacket: a student web app that finds, requests, and tracks the missing course documents needed for a transfer-credit review.** Start with one institution's documented process, such as Baruch's ELEC1111 syllabus submission route.

Pitch: “Your course needs a review. TransferPacket gets the evidence ready and follows up on what's missing.”

The outcome is **packet ready; academic review pending**. Institutions decide whether to award or apply credit. The app cannot guarantee credit, restore nonexistent documents, or infer equivalence from a similar course title.

This is my strongest solo-builder hackathon hypothesis, not established product demand or a prediction of winning. BidPatch remains competitive if an estimator can provide a realistic case and feedback immediately.

## Why this recommendation changed

The earlier construction research established a technically credible workflow using archival bid addenda. The new search found more direct recent accounts for student document collection. It also found an official email route. These findings reduce the need to invent an email step merely to use a sponsor.

The last30days engine ran twice, with saved query plans and a strict recent research target. Search metadata and retrieved page content were reviewed separately. Raw result totals contain substantial noise and do not measure support for any concept. Older videos, irrelevant GitHub issues and HN stories, generic SEO articles, and a 2023 article labelled 2026 were excluded from demand claims. X was unavailable; Instagram/TikTok and the broad run's YouTube requests failed. The focused run returned YouTube material, but its older videos were not used as recent evidence.

## Evidence and its limits

| Evidence | What it supports | What it does not establish |
|---|---|---|
| [September 1 r/UMPI discussion](https://www.reddit.com/r/UMPI/comments/1w4obc4/verify_everything_prior_to_enrollingcommitting_to/) | Firsthand reports of confusing credit application and the effort of retrieving old syllabi | That every institutional decision was wrong; demand at Baruch |
| [September 13 r/GatechClasses question](https://www.reddit.com/r/GatechClasses/comments/1weswrd/transfer_equivalency_question/) | Uncertainty about a lab-science course marked Must Evaluate | That an AI can decide academic equivalence |
| [September 11 r/WGU advice](https://www.reddit.com/r/WGU/comments/1wdmpyf/pro_tip_save_your_syllabi_both_current_and_future/) | Corroborating advice to retain syllabi for receiving institutions | Product adoption or willingness to pay |
| [Baruch's current official policy](https://enrollmentmanagement.baruch.cuny.edu/undergraduate-admissions/transfer-credit-evaluation/) | ELEC1111 needs a syllabus submitted to the Transfer Center by email | That all colleges use email; that Baruch users have validated this app |
| [Georgia Tech's official portal](https://transfercredit.gatech.edu/) | Actual-course syllabus and weekly topics are required there; review has a formal portal | That those requirements should be copied into Baruch's checklist |
| [UMPI official transfer policy](https://www.umpi.edu/offices/student-records/transfer-credits/) | General-education changes effective September 1, 2026; advisor reevaluation route | An automatic right to a particular result |

Verified quotes from the UMPI discussion:

> “I had to hunt down old syllabi to prove my case to them, and eventually all were matched correctly, but not without effort.” - u/AdamLok13

> “You’re fortunate you could find your old syllabi. Mine do not exist anymore; on the internet or otherwise.” - u/velvetmapleleaf

The full discussion verified author and text. Individual comment permalinks could not be retrieved, so the parent discussion is linked rather than inventing comment IDs. Dates are from retrieval metadata; the cached Reddit rendering displays relative times.

## Debate across candidates

| Rank | Application | Strongest case | Strongest objection | Decision |
|---|---|---|---|---|
| 1 | TransferPacket | Concrete missing documents, current student accounts, sourced requirements, genuine email route | Episodic use; existing transfer tools; college-specific process | Best solo-builder choice, subject to one real student test |
| 2 | WaitlistGuard | Keep childcare applications active and obtain confirmation of renewal | Cannot create childcare capacity; processes differ by provider | Strong alternate if a parent can supply a real case |
| 3 | StallReady | Help makers resolve event requirements and missing application documents | Risks becoming a checklist; many applications belong in portals | Practical but needs a stronger completion moment |
| 4 | BidPatch | Link a written bid change to the supplier quote needing revision | Domain expertise and recent practitioner validation missing in this pass | Promote if an estimator becomes available |

WaitlistGuard is narrower than childcare discovery. A [September 18 Ottawa discussion](https://www.reddit.com/r/ottawa/comments/1wjje8b/daycare_waitlist/) contains contradictory advice about age transitions and contacting providers. Separately, [Burnaby Children's Centre Society](https://www.bccschildren.com/waiting-list) says applications open each September, expire after a year, and can be submitted by email. This is evidence for researching each provider's actual rules, not applying Burnaby rules in Ottawa or promising to jump a queue.

StallReady has [recent craft-fair rejection discussion](https://www.reddit.com/r/CraftFairs/comments/1wiungp/interesting_post_by_a_craft_fair_admin_on_why/) and public requirements such as [Sonoma's insurance documentation](https://valleyofthemoonvintagefestival.org/artisan-application-page/). It should resolve a specific blocker, rather than send questions already answered on the event website.

Generic warranty agents, lead-generation agents, and quote-comparison apps overlap heavily with the local submission descriptions. Those descriptions were reviewed; their implementations were not tested.

## Narrow product workflow

1. **Research:** Student selects the destination institution, source institution, course, and actual term. Firecrawl reads official instructions and looks for public course material. Student can also upload an existing syllabus.
2. **Evidence:** Show the policy passage, source URL and retrieval date beside each requirement. Separate school requirements from information used to confirm that a document belongs to the student's course. A current catalogue description or a different-term syllabus is a candidate, not proof that the requested original document was found.
3. **Email:** Draft one precise request for missing material to a student-confirmed instructor or records contact. User reviews the recipient and content before sending. Use AgentMail for a real email thread.
4. **Follow-up:** Read the reply and attachment, identify what remains missing, and propose a targeted follow-up. A reply alone does not close the task. After the student confirms the correct document, update readiness and cancel the reminder.
5. **Finish:** Export the sourced packet and use the institution's documented submission route. Baruch may support email submission for this case; Georgia Tech requires its portal.

Do not combine school policies. In particular, Georgia Tech's weekly-topic requirement is not established as a Baruch requirement.

## Build scope and sponsor functionality

Use three screens: case dashboard, evidence checklist, and email thread with packet preview. Start with one course per case and one school process. Support readable PDFs/text; flag unreadable files instead of claiming complete extraction.

| Technology | Necessary work |
|---|---|
| Firecrawl | Fetch current official instructions and public source-course material; retain provenance |
| OpenAI | Propose structured requirements, compare document identity, identify missing information, draft precise requests with user review |
| AgentMail | Send approved requests, receive replies and attachments, preserve the thread |
| Convex | Authenticated case ownership, evidence/document versions, queries and mutations, live state updates, email-event deduplication, scheduled follow-ups, cancellation after resolution |

Convex supports persistent scheduled functions and cancellation: [official documentation](https://docs.convex.dev/scheduling/scheduled-functions). Use the Firecrawl/AgentMail components linked from the hackathon where they fit the implementation. Store reminder state and re-check case status before sending so a stale job cannot send after resolution. Show a live update in two browser sessions to make the shared state visible.

Existing [TES and Transferology](https://asr.umn.edu/technology-and-process-resources/applications/tes-and-transferology) already support evaluation workflows and equivalency discovery. Differentiate around student-side missing-document collection. This is a proposed focus, not a verified feature gap across all competitors.

## Demo: 2 minutes 45 seconds

| Time | Product action |
|---|---|
| 0:00-0:20 | Show a sample course awaiting syllabus review and the student's concrete task |
| 0:20-0:45 | Fetch the official policy; display the cited syllabus requirement |
| 0:45-1:05 | Show that the source document is missing; approve and send a request |
| 1:05-1:35 | Receive a controlled test reply with a different-term syllabus; the case remains unresolved |
| 1:35-2:05 | Send the targeted follow-up; receive the correct document |
| 2:05-2:30 | Student confirms the match; live checklist updates and reminder is cancelled |
| 2:30-2:45 | Export the evidence packet; finish on “Packet ready. Academic review pending.” |

Label sample records, controlled recipients, and accelerated timing. Use real integration calls. If the archive has no syllabus, the honest product result is a documented unresolved request, not a generated substitute.

## Validation and submission plan

Before broadening the build, ask one transfer student to walk through a real document request and confirm the chosen institution's intake rules. Aim for three observed tests. Measure time to assemble the packet, whether a missing or wrong document was caught, and whether the next action is clear. These are targets, not completed results. Do not report credits or money saved unless actually established.

Publish a short product clip and a real tester quote with permission on X or LinkedIn, tagging the sponsors. Community complaints establish a possible problem; your own user results and public engagement establish social proof for the submission.

The [official All Gas page](https://www.convex.dev/hackathons/all-gas) requires a public repository, root hackathon.md, accessible convex.site or chatgpt.site URL, and a demo under three minutes. Deadline: September 22, 2026 at noon Pacific, September 23 at 00:30 India time.

Suggested build order: end-to-end email and Convex state first; source extraction and evidence review second; demo polish and user testing third; deployment and submission assets last. Keep the one-institution scope through submission.

## Saved research

- [.firecrawl/last30days-hackathon/unresolved-warranty-claims-supplier-quote-changes-daycare-waitlists-and-craft-fair-applications-raw-hackathon.md](.firecrawl/last30days-hackathon/unresolved-warranty-claims-supplier-quote-changes-daycare-waitlists-and-craft-fair-applications-raw-hackathon.md)
- [.firecrawl/last30days-transferproof/college-transfer-credit-approval-raw.md](.firecrawl/last30days-transferproof/college-transfer-credit-approval-raw.md)

The engine footers preserve raw retrieval totals. They must not be presented as counts of relevant users, verified demand, product traction, or comprehensive platform coverage.
