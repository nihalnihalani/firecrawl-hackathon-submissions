# BackToCard: deeper product and hackathon decision

Research date: September 20, 2026. This is a researched product specification and proposed validation plan. No application, banking connection, merchant correspondence or customer validation was performed during this research.

## Revised decision

**Build a focused return-discrepancy resolver: “Know whether your refund adds up, and what to ask next.”**

The broad refund-tracker proposition is weaker than the first research pass suggested. A current competitor, Refundly, already advertises automatic Gmail discovery, shipment tracking, missing-refund alerts and Plaid-linked card-credit matching. Its published version history distinguishes refund initiation from money reaching the payment account. Those features cannot be presented as BackToCard's invention.

The proposed entry should earn its place through a specific job: turn selected return records into an understandable item-by-item explanation, identify the evidence still missing, and prepare the exact next support interaction. Its most convincing case is two items in one parcel with only one credited. Its practical advantage must be measured in less reconstruction work and fewer incorrect enquiries, not inferred from an impressive architecture.

This remains a conditional build recommendation. The research supports a real problem and a feasible demonstration; it does not establish a unique feature gap, willingness to pay, or a likely win.

## What the deeper research changed

| Earlier assumption | Deeper finding | Product consequence |
|---|---|---|
| Tracking through actual payment is a differentiator | Refundly already advertises this and describes it in its App Store history | Describe a specific case-audit workflow; avoid first-ever claims |
| Most consumers are a practical initial audience | Returns are occasional; some people already solve this with email snoozing or spreadsheets | Start with people handling several returns and one confusing partial credit |
| Selective forwarding is automatically easier | It avoids required account connections but still asks users to find records | Show value after one document, then request only missing evidence |
| Delivery proves the returned items arrived | A parcel scan does not establish its contents or every warehouse action | Keep carrier evidence, merchant statements and money confirmation separate |
| The original price minus credit is the missing refund | Fees, discounts, taxes, store credit and other adjustments can explain the difference | Separate expected, uncertain, unallocated and confirmed amounts |
| Any retailer can be chased by email | Several current help pages expose forms/chat without a verified email route | Gate correspondence by documented merchant channel |
| A scheduled backend job guarantees one email | Convex database guarantees do not make an external mail request atomic | Use durable outbox state, version checks and provider reconciliation |

## Current competitive evidence

| Product | Published/current evidence | Implication |
|---|---|---|
| [Refundly](https://www.refundly.app/) | Gmail extraction, return dashboard, shipment tracking, late/missing alerts, Plaid credit matching; FAQ advertises a free Gmail connection and two cards | A manual general-purpose tracker would have a difficult value proposition |
| [Refundly App Store listing](https://apps.apple.com/us/app/refundly/id6739789807) | Live iPhone/iPad listing and version history; separates receipt, refund initiation and statement credit | Promise-versus-payment is necessary correctness, not a novelty claim |
| [Recourse source snapshot](https://github.com/Spagero763/recourse/blob/207eca795c756f9c17d959fb4f89465be5db3277/convex/replies.ts) | Policy-backed cases, approved email, reply interpretation and follow-up; accepted reply maps to resolved, and manual reopening exists elsewhere | A generated refund letter and confirmation checkbox are insufficient |
| [ReturnQueen](https://returnqueen.com/faq) | Purchase syncing, pickup, packaging and tracking; merchants process refunds | Physical return logistics are already served and are outside this build |
| [ReturnPal](https://www.returnpal.net/) | Receipt scanning, status/calendar views and deadline reminders | OCR plus reminders is an established pattern |
| [Pine AI](https://www.19pine.ai/blog/best-refund-apps) | Advertises refund assistance across calls, email and forms | Do not claim all existing tools stop at tracking |

These sources establish published functionality, not tested accuracy. We did not install competitors, connect real accounts, or establish that they lack partial-item allocation or later-charge handling. Refundly's privacy policy specifically limits its use of Gmail data; this research does not support alleging that it sells Gmail data. [Privacy policy](https://www.refundly.app/privacy-policy)

The current 48-entry hackathon catalogue remains useful for positioning. In particular, Get It in Writing already has granular requirements and evidence, Exorcist has a receipt ledger, and RecallReady has household product state. BackToCard must demonstrate the integrated return-audit job rather than treating any of those primitives as unique. [Catalogue](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/ALLGAS_CURRENT_SUBMISSIONS_AUDIT.md)

## Stronger problem evidence from this research pass

[Which?'s original investigation](https://www.which.co.uk/news/article/big-name-retailers-breaking-the-law-on-returns-abwsM6V0eOzq), published September 14, used 12 mystery shoppers across Great Britain and more than 200 purchases from 17 retailers in June/July 2026. Fifteen retailers were comparable. It found missing product refunds and omitted delivery refunds. One River Island example received £1.05 where Which? calculated £5.05 after the return fee. This supports checking correctness after a credit arrives. It is a small controlled study, not a population failure rate. Amazon and John Lewis performed well; some retailers said they lacked transaction details to investigate. Do not export UK-specific delivery-refund conclusions to US orders.

Fresh community accounts show additional uncertainty. In a September 19 discussion, [u/machaf](https://reddit.com/r/amazonprime/comments/1wkz138/comment/paunsvh/) wrote: “Still waiting for my August refund. It was delivered to Amazon sept 2nd.” In another unresolved refund thread, [u/skinnnytv](https://reddit.com/r/amazonprime/comments/1wkuh6v/comment/pax9i6v/) wrote on September 20: “The customer support over chat was useless. But the one who responded via email was helpful. Let’s see how this is going to end”. These are allegations/experiences, not established root causes; helpful communication is not a successful recovery.

The best direct workaround discussion is older: [Online refund limbo, February 11, 2026](https://www.reddit.com/r/fashionwomens35/comments/1r2886v/online_refund_limbo/). Participants describe email folders, snooze, spreadsheets, Notes and statement checks; some say those are sufficient. Its age is explicit because it is not a last-30-days finding. It gives a useful comparison task for user testing, not current adoption proof.

The fresh social sample was limited: the deep run's two directly relevant Reddit threads add detail, not a broad new prevalence estimate. There was no strong recent independent evidence of willingness to grant a new app inbox/bank access. [Detailed evidence and scope audit](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/.firecrawl/backtocard-deep-2026-09-20/last30days/EVIDENCE.md)

## The first user and job

Recruit a person with two or more active apparel returns and one unresolved partial refund. They already have the order/return emails and want to know what to ask support. A person who declines permanent inbox/bank connections is a second, unvalidated audience hypothesis.

Job statement: **“When the returned items and refunded amount disagree, help me reconstruct the facts and send one accurate request without searching through every email again.”**

An occasional shopper whose merchant status page already explains everything may not need this app. A shopper who wants fully automatic account-wide discovery may prefer an account-connected competitor. Do not claim that everyone who shops will become an active user.

The first-use bargain should be explicit: the user shares selected records, gets a useful explanation, and can delete the case. Selective sharing reduces required permissions. It does not mean no sensitive data is processed: receipts can contain names, addresses and purchase history, and selected material may pass through the application's storage, model provider and mail provider.

## Product experience: three screens

### 1. Start with one confusing return

Primary action: forward a return email or upload a return confirmation. Do not begin with bank OAuth, a ten-field form or a dashboard full of empty charts.

Immediately show recognised merchant, order reference and candidate items. Ask for only the evidence missing for the next useful conclusion: perhaps the purchase receipt, then the amount received. If the user knows the posted amount, a plainly labelled confirmation is acceptable. Do not imply that it came from their bank.

Suggested copy: “I found two returned items. To check the refund, add the purchase receipt or confirm the amounts.”

### 2. Explain the discrepancy

The focal view is an item table with source links, not an AI chat transcript. Each item has three independent evidence dimensions:

- **Return evidence:** authorised item/parcel association, drop-off record and available carrier scan.
- **Merchant statement:** acknowledged, missing, investigating, refund promised, refund reported issued, or unresolved.
- **Payment evidence:** unconfirmed, supplied pending credit, confirmed posted credit, original-charge cancellation, later supplied debit, or ambiguous.

A parcel can be delivered while one item remains unacknowledged. A merchant can promise a refund while no financial evidence has been supplied. These facts should coexist visibly rather than overwriting one status label.

Main amounts: expected refund from the current evidence, net confirmed credit, and unresolved difference. When the expected amount is uncertain, show that explicitly. Do not turn uncertainty into a precise red debt counter.

Every suggested allocation shows its basis: order/refund reference, amount, currency, item identifiers, dates and evidence excerpts. Equal amounts alone are not enough. One payment can cover several items; two items can share a price. Let a credit remain unallocated while the user reviews it.

### 3. Take the next supported action

Show the relevant regional policy passage, retrieval time, official contact route, the specific question, and the selected attachments. The user approves the final recipient and message.

For an email-supported merchant, send through AgentMail and attach replies to the same case. For a portal/chat merchant, provide a copyable evidence packet and track the user's next action. Do not invent an email address to preserve an integration story.

Default scheduled follow-up prepares a draft or reminds the user. Automatically sending a follow-up requires explicit prior approval of its content, recipient and trigger. Any material change in amount or evidence invalidates that approval.

## Merchant scope

The preferred pilot is **Boden US**, one eligible online order, two returned items in one parcel, original card payment, and no preorder, gift or exceptional guarantee case. Its current policy publishes an email address and asks delayed-return customers for their order number and item details. It describes a 21-day processing/contact target and currently warns of slower returns. Treat that as a qualified service target, not guaranteed payment settlement or a legal deadline. [Official policy](https://us.boden.com/pages/returns-and-refunds)

A published support email does not establish that an AgentMail alias will be accepted as proof of customer identity. Use the customer's approved identity details and explain that account verification may be required. If support requires the original account channel, switch to the prepared packet.

Use other merchants as correctness comparisons, not automatically supported integrations. [Everlane's US policy](https://support.everlane.com/what-is-your-return-policy-H1fMnra0s) includes a $7 mail-return fee, waived for store-credit returns. [ASOS's refund help](https://www.asos.com/us/customer-care/returns-refunds/how-will-i-get-my-refund/) and [general returns policy](https://www.asos.com/us/customer-care/returns-refunds/what-is-your-returns-policy/) use different processing anchors and distinguish bank posting. Decathlon's several stated timings may be nested processing/posting expectations, not necessarily contradictions. The safe response to unresolved scope is review, not choosing the shortest deadline. [Five-merchant comparison and 13 official sources](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/.firecrawl/backtocard-deep-2026-09-20/merchant/FEASIBILITY.md)

Current public policy is not necessarily the policy in force on a historical purchase. Store purchase-date terms if supplied, and label the distinction when only the current page is available.

## Financial semantics that matter

Use integer minor units and one currency in the first build. The demo's $120, $80 and $40 are synthetic values, not a recovered amount.

For a captured purchase settled by refunds, with an established expected amount and reviewed event matches:

`unresolved = expected refund - confirmed credits + confirmed later debits`

This is a case accounting identity, not an entitlement calculation. Store credits, exchanges, unallocated payments and pending transactions need separate treatment. Do not silently clamp overpayments to zero; show a mismatch for review. A cancellation or void of the original charge is a separate settlement path: require evidence of that event, then mark the original charge cancelled. Never invent a credit to force this formula to balance.

Represent adjustments separately from the item price. A documented $7 fee on a $120 return can make a $113 credit correct. An unsupported fee assumption cannot. A later purchase from the same merchant is not a recharge of the old return merely because the amount matches.

Stripe's primary documentation describes an additional distinction: an early refund can cancel the original charge, so the charge disappears without a separate credit. It also describes ARN/STAN/RRN references for tracing certain refunds and notes that references may not yet be available. These facts support better questions; they do not imply BackToCard can access a retailer's payment processor. [Stripe refund documentation](https://docs.stripe.com/refunds)

Use **“later charge”** for money debited again after a credit. Avoid using “reversal” ambiguously in the interface, because payment documentation also uses reversal for cancellation of the original charge.

## Architecture with meaningful sponsor use

| Responsibility | Proposed implementation | Evidence that it actually works |
|---|---|---|
| Authentication and ownership | Convex auth and owner checks on every case, document and message operation | Another account cannot read or modify the case |
| Receipt/reply interpretation | An OpenAI model proposes structured fields, evidence spans and uncertain matches | A real extraction result can be corrected; money arithmetic remains deterministic |
| Public policy research | Firecrawl search when the official route is unknown; scrape the correct policy/contact pages and persist the result | A fetched passage changes the proposed next step and is inspectable |
| Correspondence | `@agentmail/convex` for inbox state, threads, inbound events and durable outbound handling | Real controlled-inbox send/reply updates the product through a webhook |
| Reconciliation | Convex mutations allocate confirmed events atomically | Partial credit closes only the matching amount; duplicate events do not change totals |
| Follow-up | Schedule a state/version check, then prepare the next authorised action | A resolved item suppresses a pending reminder; stale jobs do not generate a new demand |

The official Firecrawl component exposes one-shot search/scrape/map and durable crawls. For this MVP, one or two policy pages are enough; use scrape and persist the relevant snapshot yourself. A large crawl adds little to the demo. The component does not make an official-looking page correct or infer historical applicability. [Component documentation](https://www.convex.dev/components/firecrawl/firecrawl-convex)

The official AgentMail component documents thread/message persistence, reactive queries, Svix-verified webhook ingestion, event deduplication and queued sending with bounded retries. Use those capabilities rather than rebuilding email infrastructure. App-level case/event deduplication is still required. [Component documentation](https://www.convex.dev/components/agentmail/convex)

Convex scheduling from a mutation is atomic with that mutation. Scheduled mutations have stronger execution guarantees than external actions; cancelling an already-started function does not stop its current execution. Therefore a cancellation flag alone cannot guarantee that no email is ever sent during a race. Re-check state immediately before dispatch, use immutable approved message versions, and treat ambiguous provider outcomes as unknown until reconciled. [Scheduling documentation](https://docs.convex.dev/scheduling/scheduled-functions)

Suggested app records: `cases`, `items`, `returnAuthorizations`, `parcels`, `parcelItems`, `evidence`, `policySnapshots`, `financialEvents`, `allocations`, `approvals`, `followUps`, `processedEvents`. Reuse component-owned email tables instead of copying the entire inbox model. Household sharing is not necessary for the first build.

Critical invariants:

1. A promise cannot create a confirmed financial credit.
2. A financial event cannot be allocated beyond its amount or counted twice.
3. An ambiguous credit cannot silently settle an arbitrary same-price item.
4. A later debit must be supported and matched before reopening an amount.
5. A fee changes the expectation only when its applicability is established.
6. An older or duplicate reply cannot overwrite newer confirmed evidence.
7. A changed case invalidates an old outbound approval.
8. The app must not claim an external email was delivered merely because it queued a request.

## What to cut

Cut bank connections, Gmail OAuth, automatic carrier integrations, universal merchants, return initiation, chargebacks, legal escalation, subscription cancellation, household collaboration, pricing and analytics dashboards. They distract from the core demonstration and create unvalidated dependencies.

Retain selective input, evidence provenance, uncertain-match review, correct partial allocation, supported correspondence, ownership and duplicate handling. Those are the minimum product, not polish to postpone.

## Hackathon fit and deadline

The official criteria reward everyday usefulness, creativity, Convex depth, real sponsor integrations, a public live URL, social engagement and a video under three minutes. They do not publish numerical weights, so any weighted scorecard would be our own estimate. [Official rules and criteria](https://www.convex.dev/hackathons/all-gas)

Deadline: **September 22, 2026 at noon Pacific, September 23 at 00:30 IST**. The project must satisfy the new-build rule, use Convex, provide a public GitHub repository and root `hackathon.md`, and deploy to an accessible `convex.site` or `chatgpt.site` URL. The official page also asks builders to share on X or LinkedIn and tag the sponsors. No posting was performed as part of this research.

| Criterion | What the entry should show |
|---|---|
| Everyday usefulness | A real person's confusing return reconstructed with less effort |
| Creativity | A clear item/evidence/money explanation and precise next action, with no inflated novelty claim |
| Convex depth | Ownership, live email state, transactional allocation, versioned follow-up and actual components |
| Sponsor integrations | Visible OpenAI extraction, Firecrawl policy evidence, AgentMail send/receive and Convex state changes |
| Social proof | An actual public post plus real engagement and honest tester observations |
| Short demo | A single understandable case, with the unresolved amount visible throughout |

## Build and validation sequence

This is a suggested focused 36-hour work plan, not a claim about available team capacity or a promise of completion time.

| Work block | Result |
|---|---|
| Hours 0-4 | Test one real redacted case; define truth labels and deterministic amounts; reject unclear scope |
| Hours 4-12 | Convex case/item/event model, owner access, file intake, OpenAI extraction and correction UI |
| Hours 12-18 | Policy snapshot, precise evidence packet and AgentMail controlled send/reply |
| Hours 18-24 | Follow-up version checks, duplicate handling, uncertain matches and negative controls |
| Hours 24-30 | Test with willing recent-return users; simplify intake; correct false discrepancies |
| Hours 30-36 | Publish accessible app, verify from a fresh session, record demo, update build log and submit |

Reserve real time for the last block. If extraction or inbox reliability slips, cut the later-charge demo before cutting the public deployment or honest evidence labels.

### Validation that would change the recommendation

Proposed recruitment: five people with recent returns, ideally including at least three confusing partial-credit cases. Do not count the same household as independent evidence without saying so. Collect only consented, redacted records.

For each person, first observe their current method. Then measure app intake time, corrected fields, allocation accuracy, false discrepancies, time to prepare an accurate support request, and whether they can explain the result without coaching. Ask whether they would bring a second case. Do not lead with “Would you use an AI refund app?”

Suggested decision gates, not industry benchmarks or completed results:

- At least three testers independently understand and value the explanation.
- The app reduces the work for those cases compared with their existing process.
- No confident false debt appears in the tested negative controls.
- At least one tester returns with another document or case without being coached.
- A documented support route works for at least one real intended pilot, or the supported product is honestly framed as a packet for the user's channel.

If users must type most of the case again, stop calling it low-effort. If the only value is a generic email, the competitive case is weak. If no real records are tested, present it as a working prototype with sample cases rather than a validated recovery product.

Do not promise recovered money before it is confirmed. Valid early outcomes include a correctly explained amount, an avoided false complaint, a completed packet, and a real enquiry sent with consent. Genuine social proof can report those outcomes accurately before a merchant has resolved the refund.

## Demo and working materials

The complete recording plan is in [BACKTOCARD_DEMO_SCRIPT.md](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/BACKTOCARD_DEMO_SCRIPT.md). It specifies the exact screen actions, narration, controlled inboxes, sample facts, fallback behavior and reviewer challenge cases.

The interactive rehearsal in this conversation is a local state explanation with simulated records. It does not call sponsors, send email or prove the application has been built.

The [synthetic fixture pack](/Users/nihalnihalani/Desktop/Github/firecrawl-hackathon-submissions/backtocard-demo-kit/fixtures.json) contains expected outcomes for partial credit, promises, confirmed credit, later charge, duplicate import, valid fee and ambiguous amount matching. These are future acceptance cases, not passed application tests.

Raw research and independent memos are saved under `.firecrawl/backtocard-deep-2026-09-20/`; prior submission and source-code captures remain under `.firecrawl/audit-2026-09-20/`.
