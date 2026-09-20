# BackToCard: a 2:45 demonstration that proves the product

Prepared September 20, 2026. This is a recording plan and sample-case specification, not evidence that the application or integrations have been built.

## The promise

**“Know whether your refund adds up, and what to ask next.”**

Opening line: “I returned two items in one parcel, but I can only match one refund. BackToCard turns the receipts into the exact question support needs to answer.”

The audience should remember the missing scarf and its $40, not an agent architecture diagram. The live product should keep that item and amount visible while evidence, policy, mail and confirmed payment change.

The broader tracker category is established. Do not say “the first refund tracker,” “nobody checks bank credits,” or “we automatically recover your money.” Refundly's published product already includes automatic tracking and card-credit matching. Demonstrate this particular audit clearly and let the work speak for itself.

## Sample case and disclosure

Use a visible, persistent **Sample case** badge. Use synthetic documents clearly marked as test material. Display **Controlled merchant inbox** in the reply view. Use real API integrations with these controlled inputs, but do not imply an actual retailer answered or actual money moved.

| Fact | Sample value and source |
|---|---|
| Merchant policy reference | Boden US current official returns/refunds page |
| Order | `SAMPLE-BTC-120`; two items; one currency; original card payment |
| Purchase | August 25, 2026; final attributable paid values $80 sweater + $40 scarf |
| Return | Authorised August 27; posted August 28; both items recorded under one sample return authorisation and one parcel |
| Expected amount | $120, based on supplied sample records; no fee, preorder, exchange, gift or uncertain tax adjustment in this fixture |
| Merchant record | Sample acknowledgement identifies the sweater and its $80 only |
| Financial evidence | User explicitly confirms a posted $80 credit and its match to that acknowledgement |
| Remaining question | What happened to the scarf and its $40? |
| Current date | September 20, 2026; 23 days after posting |

Boden's current page aims for processing within 21 days, asks for order/item details when contacting support, and warns that returns are taking longer. The case is suitable for a precise status enquiry; do not put “illegal,” “guaranteed overdue” or a legal countdown on it. A carrier record does not prove every item was inside the parcel.

The synthetic facts do not establish that all real Boden orders have zero fees or adjustments. Real cases must be checked individually.

## Main recording: 165 seconds

| Time | What to click/show | Exact narration | Evidence of functionality |
|---|---|---|---|
| 0:00-0:12 | Open the public app directly into the sample case | “I returned two items in one parcel, but I can only match one refund.” | No slides or authentication obstacle before the problem is visible |
| 0:12-0:35 | Import the prepared return/receipt bundle; accept the clearly sourced item match | “These are the two items and the return record. The $80 credit belongs to the sweater. The scarf is still unmatched.” | Actual extraction output, editable matches, visible source excerpts |
| 0:35-0:55 | Open Research and inspect the fetched policy/contact passage | “Boden asks for the order number and the specific returned items. Its page also warns of delays, so this is a status enquiry, not an accusation.” | Real Firecrawl result, source URL and retrieval time; relevant next action |
| 0:55-1:15 | Review the recipient, attachments and short draft; approve Send | “The message asks only about the missing $40 scarf. I choose exactly what to share.” | Actual AgentMail send to an operator-controlled inbox; product shows queued/sent honestly |
| 1:15-1:35 | Send the prepared reply from the controlled inbox; inspect the unsent follow-up draft and user-chosen reminder date | “Approval is not payment. The next draft asks whether the refund was issued. I choose when to check again.” | Real inbound email/webhook; waiting-for-credit state, follow-up draft and persisted Convex schedule; no invented policy deadline |
| 1:35-1:50 | Display “Sample later credit - time advanced”; confirm the supplied sample $40 posted credit | “Later, once I confirm the credit, the balance clears and the reminder stops.” | One Convex mutation updates allocation, amount and reminder state; amount labelled user-confirmed sample credit |
| 1:50-2:20 | Open the separate Everlane control: eligible US mail-label return to original card, $120 net refundable merchandise, applicable $7 label deduction, $113 confirmed credit | “A smaller refund is not always wrong. This mail return has an applicable seven-dollar label fee. The policy explains the difference, so the app does not generate a complaint.” | Inspect source and applicability; policy evidence changes expected amount; no false missing-money alert |
| 2:20-2:35 | Show one actual tester observation and the supported-channel label | Use only a measured fact, for example: “This tester assembled the correct packet in X minutes, compared with Y using their existing method.” | Redacted consented evidence, actual values and denominator; no invented recovery |
| 2:35-2:45 | Finish on the case detail and public app URL | “BackToCard makes a confusing return understandable, then helps you ask the right question.” | Working public product, coherent unresolved/resolved state |

Keep the later-charge and duplicate-replay challenges in the interactive walkthrough, outside the main video. If no actual user test is completed, say “This is a working prototype tested against these labelled cases” and show only tests that actually ran. Do not leave placeholder X/Y values in the recording.

The Everlane fee case is a separate merchant/policy example. Do not apply Everlane's policy to the Boden case. Establish an eligible US mail-label return to the original card, excluding store credit, in-store returns, tax, shipping and other adjustments from this fixture. Show the applicable official passage. Explain the arithmetic without presenting it as a legal ruling.

## What must be real and what may be simulated

| Element | Required handling |
|---|---|
| Order, return and payment documents | Synthetic or permissioned/redacted; visibly distinguish which |
| OpenAI extraction | Real model call/result in the integrated demo; cached results labelled when used |
| Firecrawl policy | Actual fetched official page, stored source and retrieval time; label a cached snapshot |
| Email send and inbound reply | Actual AgentMail transport between controlled inboxes |
| Merchant identity | Explicitly a controlled test correspondent, not a claimed real retailer employee |
| Money movement | Supplied sample event or explicit user confirmation; no actual payment processing claim |
| Scheduler demonstration | Label accelerated time; production uses the real policy/user-approved timing |
| Product state | Derived from Convex records and mutations, not a frontend timer that swaps staged screens |
| Social proof | Actual post engagement and consented tester outcomes only |

Record the deployed product. A public sample case should be isolated per visitor/session, allow reset of that visitor's sample data, and never expose real receipts or unrestricted email sending. Judges should be able to inspect it without an invitation. Real personal cases still require authentication and ownership controls.

## Controlled inbox setup for the eventual build

1. Create a case inbox and a second operator-controlled test correspondent. Show both as test addresses in the demo setup.
2. Restrict sample-mode recipients to an allowlist of addresses the team controls. Do not allow anonymous visitors to email arbitrary merchants.
3. Register and verify the real webhook path. Confirm a reply appears through ingestion before recording.
4. Keep outbound approval tied to the recipient, final body, selected evidence and current case version.
5. Pre-write the test response in the second inbox, but send it only at the appropriate point during the recording. This is a staged response through a real integration.
6. If an external request times out, show pending/unknown and reconcile its status. Do not issue a new send merely to make a green badge appear.

No inboxes were provisioned and no messages were sent while preparing this research.

## Exact sample messages

These are demo copy, not messages authorised for delivery to a real merchant.

### User-approved enquiry

Subject: SAMPLE CASE - item-level refund check for SAMPLE-BTC-120

Hello,

I am checking the refund for the two items recorded in return SAMPLE-RMA-120, posted on August 28.

The sweater's $80 refund is confirmed. The scarf was also listed on the return record, but I cannot match its $40 to a refund acknowledgement or credit.

Could you confirm the scarf's processing status and the refund amount or any applicable deduction? I have attached the selected return record and drop-off receipt.

Thank you.

### Controlled merchant reply

Subject: Re: SAMPLE CASE - item-level refund check for SAMPLE-BTC-120

This is a controlled demonstration response, not correspondence from a retailer.

For this sample case, the additional $40 scarf refund is approved and being processed. The earlier $80 refund was for the sweater.

### Follow-up draft if the stated processing period passes

Hello,

I am following up on the additional $40 scarf refund referenced in your reply. I have not yet confirmed a corresponding credit.

Could you confirm whether it has been issued, the issue date, and any available refund reference? If a deduction or a different payment destination applies, please identify it so I can reconcile the record.

Thank you.

Do not insert a universal ARN demand or invented bank-posting deadline. References and timing vary by processor, payment method and merchant. Do not send a follow-up when an unresolved provider status could mean the prior message was already sent.

## Reviewer challenge cases

These are acceptance criteria for the future application, not completed test results.

| Challenge | Correct result |
|---|---|
| Two items, one parcel, $80 credited against $120 established expectation | $40 remains unmatched on the correct item |
| Merchant promises the remaining $40 | No confirmed credit created |
| User confirms the posted $40 and its match | Balance zero; reminder state updated |
| Same credit or inbound event arrives twice | No duplicate allocation or duplicate draft |
| A later supplied $40 debit is matched to the scarf | Only scarf reopens; history preserved |
| Another $40 purchase from the same merchant appears | Do not assume it is a recharge; request matching evidence |
| Two items have the same price | Amount alone does not decide the item allocation |
| One refund covers several items | Allow reviewed split allocation; total cannot exceed credit |
| $120 gross return, applicable documented $7 fee, $113 received | No missing-refund complaint |
| Fee applicability is unknown | Expected amount needs review; do not assert $7 owed |
| Public policy pages disagree about the clock anchor | Show the conflict and avoid an automatic deadline claim |
| Original charge disappears after cancellation | Do not require a separate credit to exist |
| Store credit received for a card purchase | Label store credit separately; do not silently count it as money back on card |
| Old promise email arrives after confirmed credit | Preserve confirmed credit; do not regress to awaiting payment |
| User changes the amount after approving an email | Invalidate old approval and request review |
| Reminder starts while a user resolves the case | Re-check state/version before dispatch; handle unavoidable external-send races honestly |
| An unrelated account requests the case or attachment | Access denied |

## Recording reliability

Warm the public page and verify the supported integrations immediately before recording. Use the same prepared synthetic bundle for repeat takes, with fresh isolated case IDs. Keep a timestamped cached policy as a labelled fallback, not an invisible substitute for a failed crawl.

If the model is uncertain, show the correction interaction; do not edit it out to imply guaranteed extraction. If an email takes longer than the allotted segment, cut waiting time transparently or show a previously recorded genuine send/reply sequence with its timestamp. A fabricated live-reply animation would invalidate the demonstration.

A backup recording can protect against presentation-network failure, but it must show the working deployed product. The submission itself still needs an accessible live URL and a video under three minutes.

## Build order for this demo

1. Make the deterministic sample-case amounts and evidence view correct.
2. Connect selective input and real extraction, with one uncertain-match correction.
3. Fetch and display applicable policy evidence.
4. Complete the real controlled send/reply loop.
5. Make confirmation cancel the reminder; demonstrate duplicate handling.
6. Add the legitimate-fee negative control.
7. Add later-charge handling only if the core is reliable.
8. Test real records, record actual observations, deploy and prepare the submission assets.

The main experiment is whether this workflow helps a real person faster than their email folder or spreadsheet. A polished sample story alone does not answer that.
