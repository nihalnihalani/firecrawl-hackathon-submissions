# BackToCard: project decision after the live submission and repository audit

September 20 deeper-research update: [BACKTOCARD_DEEP_RESEARCH.md](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/BACKTOCARD_DEEP_RESEARCH.md) supersedes the broad tracker positioning below. Refundly already advertises automatic tracking and bank-credit matching. The revised recommendation is a focused audit of a confusing refund, with policy-aware amounts and precise support evidence. See the [revised demo](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/BACKTOCARD_DEMO_SCRIPT.md).

Research date: September 20, 2026. Recent-community window: August 21 through September 20, 2026. This recommendation replaces TransferPacket as the preferred option for the user's revised requirement: a problem affecting a much broader audience. It is a project hypothesis, not a guarantee of winning or evidence of product traction.

## Decision

**Build BackToCard, a consumer web app that follows each returned item until its refund is confirmed and keeps the record usable if the merchant charges again.**

Pitch: **“Track every return until the money is back.”**

The central object is an individual returned item and its financial history. Start with a purchase and return authorization, associate the correct items with the correct label or parcel, preserve drop-off and merchant acknowledgements, reconcile partial refunds, and ask the merchant only about the unresolved item or amount.

The distinctive moment: **two items went back; one was credited; a generic refund promise must not close the other.** A later recharge reopens the affected item without creating a second copy of the original claim.

## Why this is a broad problem

Three types of evidence support different claims:

1. **Population context:** LegalShield's December 2025 survey of 1,013 U.S. adults, balanced to Census demographics and published January 22, 2026, reports that 46% kept defective or unwanted items because returning them was too difficult or expensive. This is a commercial-provider survey about return friction, not the incidence of missing refunds. [Original survey release](https://www.legalshield.com/newsroom/new-legalshield-study-americans-forgo-returns-on-broken-unwanted-products-citing-barriers-from-retailers)
2. **Recurring consumer activity:** Shorr's November 2025 survey of 2,013 American consumers reports 91% returned something in the prior year and nearly five returns annually. This is an older commercial survey, not a current-month trend or a representative count of victims. [Original report](https://www.shorr.com/resources/blog/consumer-report-return-habits/)
3. **Recent concrete failure:** A September 19 discussion describes items returned but not recorded, initial refunds followed by later charges, and time spent reconstructing the history. Independent September 16 and 19 discussions also describe return-proof disputes and delayed refunds. These are consumer self-reports, not adjudicated merchant wrongdoing. [September 19 discussion](https://www.reddit.com/r/amazonprime/comments/1wkpfcg/amazon_retroactively_charges_me_for_things_i_do/), [September 16 discussion](https://www.reddit.com/r/amazonprime/comments/1whm0ti/is_anyone_else_having_issues_with_amazon_charging/), [delayed refund discussion](https://www.reddit.com/r/amazonprime/comments/1wkz138/delayed_refunds_via_ups/)

Two exact comments from the September 19 thread:

> “The most recent I returned 2 books in the same package and they only recorded one as returned.” - [u/BAHGate](https://reddit.com/r/amazonprime/comments/1wkpfcg/comment/pat135z/)

> “And then a month later, Amazon says they have received a different item” - [u/vwaldoguy](https://reddit.com/r/amazonprime/comments/1wkpfcg/comment/paskfhg/)

The second quotation is an exact excerpt, not the full comment. Other commenters report never having the problem; the thread cannot establish a failure rate.

NRF and Happy Returns estimated $849.9 billion in U.S. retail returns for 2025. That is merchandise returned, **not lost refunds**, revenue available to this app, or proof of the number of people affected by wrongful recharges. [NRF original release](https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025)

## What the current competitors already do

The live tag page listed 48 projects during this research. All 48 detail pages were retrieved. They list 44 GitHub repositories and one GitLab repository; 44 repositories were accessible across both hosts. The static review includes 42 READMEs and 181 selected GitHub source/configuration/log files. Deployed apps were not tested end to end. The complete links and coverage are in [the audit](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/ALLGAS_CURRENT_SUBMISSIONS_AUDIT.md) and [the CSV](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/allgas_submissions_2026-09-20.csv).

| Crowded direction | Existing submissions | Consequence |
|---|---|---|
| Cancellation and renewal tracking | Exorcist, Subzero | A receipt-driven cancellation ledger is already covered |
| Claims, demand letters, and escalation | Recourse, Duebell, TenantShield, ClaimHero | Cited emails and follow-up are baseline features, not a differentiator |
| Home-service and venue quotes | Compari, Quote Arena, Bidzy, One Table | Quote research, extraction and chasing are crowded |
| Receipt-based recall response | RecallReady, NoticeProof | Receipt-to-safety-alert is already covered |
| Household information | Backpack, OurSpaces | Shared state and family inboxes alone are not distinctive |
| Public-page promise verification | Get It in Writing | Source-backed requirement checking is already covered |
| Page and document monitoring | Pigeon, still-true | Crawling a policy and emailing its changes is not sufficient |

Bidzy's current description, schema and hackathon log include scope changes and stale quote handling. Its README describes a different product, so the README alone would have missed this competitive overlap. This further weakens the earlier BidPatch recommendation as an obvious gap.

## Closest competitor: Recourse

Recourse already researches supporting and opposing policy clauses, attaches evidence, sends approved messages, interprets replies and schedules escalation. It also has manual resolution and reopening. Do not pitch any of those as new.

The inspected source gives a specific distinction. At commit `207eca795c756f9c17d959fb4f89465be5db3277`, `convex/replies.ts` maps an `accepted` reply to `resolved`, clears further nudges, and sets a settled amount from the offer or claimed amount. Its schema models cases and replies, without separate item, parcel and refund-payment records. This is a static observation about this snapshot, not a finding about every path in its deployed app. [Reply handler](https://github.com/Spagero763/recourse/blob/207eca795c756f9c17d959fb4f89465be5db3277/convex/replies.ts), [schema](https://github.com/Spagero763/recourse/blob/207eca795c756f9c17d959fb4f89465be5db3277/convex/schema.ts)

**Judge's strongest objection:** “Why is this more than Recourse with a refund-confirmed checkbox?”

**Required answer in the product:** separate items, return authorizations, parcels, promised credits, confirmed credits and reversals. A partial refund resolves only its matched amount. A later recharge restores only its matching balance. The user can inspect which source supports every allocation, correct a mismatch, and see the balance update without duplicated events.

Outside the hackathon, ReturnQueen already advertises return pickup and tracking; its FAQ says merchants issue refunds. Pine AI advertises refund assistance across calls, email and forms. The proposed difference is specific reconciliation behavior, not a claim that consumer refund tools do not exist. [ReturnQueen](https://returnqueen.com/faq), [Pine positioning](https://www.19pine.ai/blog/best-refund-apps)

## A real email route for the first version

The current [Boden US returns page](https://us.boden.com/pages/returns-and-refunds) asks customers who have not heard within 21 days of posting a return to contact support with their order number and the items returned. It also publishes `custserv@bodenusa.com` for return/refund questions. The page currently warns of processing delays. Treat the stated timing as a published service target with that qualification, not a statutory deadline.

This provides a credible pilot: the app assembles precisely the item-level evidence that support requests. Initiating a return still belongs in Boden's returns portal. Contact from an app inbox may need customer verification; do not assume the retailer will accept the alias as proof of account ownership.

Amazon discussions establish pain. They do not establish that an app can resolve Amazon cases by email. For chat/portal-only merchants, prepare a copyable evidence packet and let the user use the documented channel.

## The four-step workflow

1. **Research:** Firecrawl reads the correct regional merchant policy and official contact page. Save the exact relevant passage, source URL and retrieval time. Separate the policy available today from the policy that applied to a historical purchase.
2. **Evidence:** OpenAI proposes matches between user-supplied purchase receipts, return authorization, item identifiers, labels, drop-off receipt and support correspondence. The user confirms uncertain matches. A parcel delivery scan proves delivery, not necessarily every item inside.
3. **Email:** Prepare a short request about the particular unmatched item, amount or refund reference. Attach selected evidence and send through AgentMail after the user approves the recipient and message. Do not send another generic demand for the full order amount.
4. **Follow-up:** Store the reply and its commitment. A promised refund starts a waiting state, not a money-received state. Schedule an appropriate reminder; reconcile a confirmed partial credit; keep the rest open; reopen the matching amount if a later charge is supplied.

## Scope that can be completed before submission

Three screens:

- **Refund board:** expected, promised, user-confirmed received, and unresolved amounts, clearly distinguished.
- **Return detail:** item-to-label/parcel mapping and dated evidence timeline.
- **Resolution thread:** cited policy, editable email, replies and next action.

Support one merchant's process, readable receipts/PDFs and forwarded emails. Preserve currency and use integer minor units for amounts. Show manual review when taxes, discounts, shipping, restocking fees, preorders or store credit make the expected amount uncertain. Separate pending credit from posted credit and avoid claiming any payment is wrongful just because it differs from the purchase price.

Without bank integration, financial events come from explicit user confirmation or user-supplied evidence. This is sufficient for an honest hackathon MVP. It cannot automatically discover unseen card charges.

## Meaningful sponsor use

| Sponsor | Product function |
|---|---|
| Firecrawl | Current regional return rules, timeframes, exclusions and official support route |
| OpenAI | Structured receipt/reply extraction, proposed item matches, explanations of uncertain allocations and precise drafts |
| AgentMail | Per-case correspondence, real approved sends, inbound reply and attachment handling |
| Convex | Authenticated ownership, items/parcels/evidence/refund events, reactive balances, atomic reconciliation, duplicate-event prevention, scheduled reminders, cancellation/reopening and shared household views |

Suggested records: `households`, `orders`, `orderItems`, `returnAuthorizations`, `parcels`, `parcelItems`, `evidence`, `policySnapshots`, `refundEvents`, `refundAllocations`, `threads`, `reminders`, `processedWebhookEvents`.

Keep refund promises separate from financial ledger events. When matching a new event, never allocate one credit twice. Reprocessing the same inbound webhook must not change the balance twice. Reminder handlers re-check current item state before dispatch. A single transaction should update an allocation and its corresponding resolved/unresolved state.

## Demo, 2 minutes 45 seconds

Use visibly labelled sample records and controlled test inboxes with actual integrations.

| Time | Action | What it proves |
|---|---|---|
| 0:00-0:20 | Show two returned items, $120 expected, $80 confirmed received | Familiar monetary problem |
| 0:20-0:45 | Import receipt and authorized return record; reveal the unmatched $40 item | Item-level reconciliation |
| 0:45-1:05 | Crawl the merchant's policy and show the relevant wait/contact rule | Firecrawl affects the next action |
| 1:05-1:30 | Approve and send the exact $40 enquiry with selected evidence | Real AgentMail integration |
| 1:30-1:55 | Receive “Your refund is being processed”; the $40 stays pending | A reply is not a confirmed payment |
| 1:55-2:20 | Confirm the actual $40 credit; the balance reaches zero and reminder stops | Convex state and correct completion |
| 2:20-2:35 | Supply a sample later $40 recharge; only that item's balance reopens | The distinct failure mode |
| 2:35-2:45 | Show observed user testing and the scope limits | Credibility |

The $120/$80/$40 figures are a demonstration fixture, not recovered money. If a real refund has not arrived by submission, report the actual observed outcome, such as correctly reconstructed evidence or a sent enquiry.

## Build order and validation

1. Build the deterministic item/refund ledger and the partial-credit/recharge demo first.
2. Connect forwarding/upload intake, then Firecrawl policy evidence and AgentMail send/receive.
3. Add ownership checks, deduplication, reminders, uncertainty review and a polished public sample case.
4. Test with five people who made a recent return. Use their redacted records with permission. Measure correct matches, false discrepancies, time to assemble the support request and whether they understand what is still pending.
5. Publish a product clip and genuine tester observations; complete the deployment, root hackathon.md and under-three-minute video.

Those five tests are proposed work, not completed validation. The strongest social proof is a real person finding a forgotten pending refund or correcting a mistaken assumption, not a large invented “money saved” counter.

## Alternatives and why they rank lower

- **TradeInProof:** track device serial/condition evidence, the quoted trade-in amount, shipment and final credit. A recent Google Store non-return-charge complaint supports this direction, but device-specific terms and disputed condition add complexity and it is less frequent than general returns.
- **CareConfirm:** help people check whether a mental-health provider is accepting patients and their specific plan. Official historical ghost-network research supports a serious problem, but current local demand, email feasibility and provider adoption were not sufficiently validated in this pass. Existing Ombuds also overlaps with research-plus-availability enquiries.
- **TransferPacket:** remains a feasible narrow document-collection project. It no longer wins against the user's broader-audience requirement.

**Selection rule:** choose BackToCard if you can demonstrate item-level reconciliation with real return documents. If the implementation becomes only a chatbot that writes refund emails, its distinction disappears and the audit does not support calling it a strong competitive entry.
