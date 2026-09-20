# BackToCard synthetic demo kit

These records specify proposed application behavior. They are not real purchases, bank events, customer outcomes, or passed integration tests.

Use [the recording script](../BACKTOCARD_DEMO_SCRIPT.md) for the complete 2:45 sequence, sample messages, disclosure labels and controlled-inbox requirements. The [research blueprint](../BACKTOCARD_DEEP_RESEARCH.md) explains the source evidence and build boundaries.

## Reading fixtures.json

- All amounts are integer US cents.
- `sequential_delta` records form one case, in `priorFixture` order. Apply only `newEvents`; carry earlier events forward and deduplicate by case/event identity.
- `merchant_promise` is nonfinancial. It must never increase confirmed credit.
- `later_debit` reduces net confirmed credit only after a supported match to the case.
- `independent_case` records reset state. Do not append their amounts to the hero case.
- `expected` describes desired future behavior, not an output already produced by a working app.
- A null expected amount means the evidence is insufficient. It does not mean zero.

The main video uses the partial credit, promise, later confirmed credit and legitimate-fee examples. Label the transition to the later credit **Sample later credit - time advanced**. The later-charge and duplicate-replay examples belong in the optional interactive walkthrough.

The Everlane control is an eligible US mail-label return to the original card, with $120 net refundable merchandise and an applicable $7 label fee. Other payment destinations, in-store returns and additional adjustments are outside that fixture. This is an arithmetic example tied to the reviewed policy, not a legal entitlement determination.

Original-charge cancellation is a separate path from a posted refund. It is listed in the script's challenge cases but is not represented by a fabricated credit in this fixture pack.

Use operator-controlled, allowlisted inboxes for demonstration mail. No service credentials, real card numbers, real customer documents or merchant recipients are included.
