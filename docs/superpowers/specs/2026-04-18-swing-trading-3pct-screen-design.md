# Swing Trading 3pct Screen Skill Redesign

## Goal

Redesign the `swing-trading-3pct-screen` skill so it:

- investigates the full Screener universe fundamentally before chart triage
- ranks the full universe from strongest to weakest fundamental sponsorship
- performs technical analysis in that ranked order
- evaluates stop survivability across a practical `2%` to `4%` downside zone around the usual `3%` reference
- produces concise but complete report files that remain useful even when technical coverage is intentionally limited

The redesigned skill must help the agent answer two questions:

1. `Is this stock's momentum credibly sponsored by recent business evidence?`
2. `If yes, is the current chart structure likely to defend a practical 2% to 4% stop zone?`

## Problems In The Current Skill

The current skill still leaves too much room for shallow execution. The transcript exposed these gaps:

1. Technical analysis drifted toward `daily EMA 10` distance as an early rejection shortcut.
2. The skill did not force a `full-universe fundamental ranking` before chart work began.
3. The skill did not guarantee a `descending strongest-to-weakest` master ranking across the whole universe.
4. Delegated workers were not defined with enough precision, so fresh-session sub-agents could miss the real goal.
5. The technical method was still too EMA-centered and did not explicitly require `support/resistance`, `supply/demand`, `chart patterns`, and `market structure` across all required timeframes.
6. The reporting contract did not clearly distinguish `reviewed` names from `pending technical review` names in limited runs.
7. The execution model for fundamentals versus technicals was not separated cleanly enough.

## Design Summary

The skill should run in two stages:

1. `Fundamental stage`
   Analyze every stock in the fetched universe, rank them by sponsorship strength, and produce a full-universe fundamental ordering.
2. `Technical stage`
   Analyze stocks in that ranked order, one stock per technical sub-agent, strictly sequentially because TradingView MCP is shared mutable state.

This is a `fundamental-first ranked pipeline`, not a rolling mixed loop.

The skill must stop treating `3%` as a hard binary wall. It should keep `3% Floor = CMP x 0.97` as the anchor, but judge a practical `2%` to `4%` downside band using multi-timeframe structure rather than one indicator.

## Execution Architecture

### Main Agent Responsibilities

The main agent should:

- parse the user prompt for an optional technical coverage limit such as `analyze 12 stocks`
- fetch the user-provided Screener URL as HTML across all pages
- extract a compact `screen thesis` from the visible title and filters
- normalize and deduplicate the full stock universe
- dispatch `fundamental sub-agents` for every stock with bounded parallelism
- collect all stock-level fundamental results
- build the full-universe fundamental ranking
- dispatch `technical sub-agents` in ranked order only after the ranking exists
- run technical sub-agents strictly one at a time
- synthesize the five report files
- keep report status honest when technical review is intentionally limited

The main agent must stay focused on orchestration and synthesis rather than carrying raw per-stock investigation detail for the entire run.

### Screen-Thesis Extraction

Before any sub-agent is dispatched, the main agent must build a compact context package:

- `screen title`
- `visible filter rules`
- `why this universe is momentum-biased`
- `what kind of sponsorship the analysis is trying to validate`
- `coverage mode`
  - full universe, or
  - top `N` technically reviewed names

This context must be passed into every delegated worker. The skill must not hardcode assumptions such as `30% over 3 months`, because the user can provide different momentum-biased screens.

### Fundamental Sub-Agents

Fundamental sub-agents should:

- own one stock each
- analyze the stock in the context of the parsed screen thesis
- decide whether current momentum appears credibly sponsored by recent business evidence
- use news only as an exception-based escalation layer
- return concise structured outputs for ranking

Fundamental sub-agents may run in parallel, but only with bounded concurrency.

### Technical Sub-Agents

Technical sub-agents should:

- own one stock each
- receive the stock's fundamental rank and sponsorship result
- inspect `weekly`, `daily`, `60`, `30`, and `15`
- determine whether the current structure is likely to defend a practical `2%` to `4%` stop zone
- return concise structured outputs for ranking and reporting

Technical sub-agents must run strictly sequentially. No overlap is allowed because TradingView MCP uses a shared chart session.

## Coverage Logic

The skill should treat the user prompt as the authority on technical review depth.

- If the user says `analyze 12 stocks`, the agent must:
  - complete fundamental analysis for the full universe
  - build the full-universe fundamental ranking
  - run technical analysis only for the top `12` fundamentally ranked names

- If the user does not specify a technical coverage limit, the agent must:
  - complete fundamental analysis for the full universe
  - build the full-universe fundamental ranking
  - continue technical analysis from the top downward until the full universe is covered

This rule exists so an interrupted or limited run still spends technical effort on the strongest fundamentally sponsored names first.

## Fundamental Sponsorship Model

The fundamental stage should not behave like long-term investing analysis and should not depend on rigid absolute thresholds. Its job is narrower:

`Determine whether the stock's current momentum is being credibly sponsored by recent business evidence, catalyst context, and acceptable near-term fragility.`

### Required Fundamental Dimensions

Every fundamental worker should investigate:

1. `Recent trigger`
   What likely put the stock into this screen now.
2. `Operating evidence`
   Sales direction, profit direction, margin direction, acceleration or deceleration.
3. `Earnings quality read`
   Whether the improvement is clean or noisy.
4. `Balance-sheet comfort`
   Not as a hard cutoff, but as a fragility read.
5. `Catalyst status`
   Company-specific or sector/macro support for the move.
6. `Evidence-to-price alignment`
   Whether price strength is justified, slightly ahead of proof, or far ahead of proof.
7. `Event-risk modifier`
   Only when relevant and likely to matter for a short swing.

### News Usage

News should not be a default research step for every stock.

Use news only when needed to:

- resolve contradiction between price and fundamentals
- validate a suspected company-specific catalyst
- validate a likely sector or macro catalyst
- assess short-horizon event risk

### Fundamental Outputs

Each stock must receive:

- `Fundamental Rank`
- `Sponsorship Label`
- `Why it got that label`
- `Whether news escalation was needed`
- `Whether technical review has been run yet`

Recommended labels:

- `Strongly Sponsored`
- `Moderately Sponsored`
- `Mixed`
- `Weakly Sponsored`

## Technical Stop-Survivability Model

The technical stage should answer:

`Can this stock, at or near current location, realistically defend a practical 2% to 4% downside zone around the usual 3% reference?`

### Required Timeframes

Every technically reviewed stock must be analyzed on:

- `Weekly`
- `Daily`
- `60`
- `30`
- `15`

### Required Technical Factors

On those timeframes, the worker must evaluate all relevant factors, not just EMA distance:

- `EMA context`
- `support and resistance zones`
- `supply and demand zones`
- `chart patterns`
- `market structure`

The skill must explicitly forbid:

- selecting or rejecting from EMA distance alone
- selecting or rejecting from one timeframe alone
- treating clustered EMAs as multiple independent reasons unless structure confirms them

### Timeframe Roles

- `Weekly`
  Trend health, extension risk, major higher low, major resistance.
- `Daily`
  Active swing, breakout base, retest quality, recent meaningful higher low, visible resistance.
- `60`
  Local invalidation, demand shelf, support density, sloppiness versus control.
- `30`
  Main lower-timeframe execution and support-mapping frame.
- `15`
  Micro-structure and air-pocket check into the stop zone.

### Technical Labels

Recommended technical labels:

- `Best Aligned`
- `Constructive`
- `Near-Valid`
- `Fragile`
- `Likely To Break`

The final report may still translate these into `Selected`, `Watchlist`, and `Rejected`, but analysis should stay more nuanced internally.

## Delegation Contract

Every main-agent to sub-agent handoff must include:

- `Goal`
- `Context`
- `Few-shot examples`
- `Output schema`

If any of those four pieces are missing, the delegation should be treated as invalid.

### Fundamental Handoff Requirements

The fundamental worker handoff must include:

- the worker goal:
  - determine whether this stock's current momentum is credibly sponsored by recent business evidence
- the screen context:
  - title, filters, screen thesis, and why the stock is in this universe
- phase context:
  - this is a `fundamental-ranking` task, not long-term investing analysis
- exception-based news rules
- few-shot examples covering:
  - `Strongly Sponsored`
  - `Mixed`
  - `Weakly Sponsored`
  - `News escalation needed`
- output schema fields

### Technical Handoff Requirements

The technical worker handoff must include:

- the worker goal:
  - determine whether this stock can defend a practical `2%` to `4%` stop zone
- context:
  - symbol
  - screen thesis
  - fundamental rank
  - sponsorship label
  - ranking reason
  - coverage mode
- required timeframe list:
  - `weekly`, `daily`, `60`, `30`, `15`
- required factor list:
  - EMA context
  - support/resistance zones
  - supply/demand zones
  - chart patterns
  - market structure
- few-shot examples covering:
  - `Best Aligned`
  - `Near-Valid`
  - `Likely To Break`
  - `bad EMA-only analysis`
- output schema fields

## Ranking Views

The redesigned skill should maintain three ranking views:

1. `Fundamental ranking`
   Full universe, strongest sponsorship to weakest sponsorship.
2. `Technical ranking`
   Only among technically reviewed names, least likely to most likely to break the stop zone.
3. `Combined ranking`
   Default master ranking with status made explicit when technical review is pending.

The combined ranking must not pretend equal certainty for technically reviewed and not-yet-reviewed names in limited runs.

## Report Contract

Every run must create a fresh timestamped directory:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Each run must produce these files:

1. `README.md`
2. `3pct-selected-and-watchlist.md`
3. `3pct-rejected.md`
4. `screen-universe.md`
5. `3pct-ranked-by-stop-safety.md`

### README.md

This should be the quick control panel for the run. It should contain:

- run date and screen URL
- parsed screen thesis
- universe size
- user coverage mode
- counts of:
  - fundamentally analyzed stocks
  - technically reviewed stocks
  - selected
  - watchlist
  - rejected
  - pending technical review
- top previews:
  - top `5` fundamentally strongest
  - top `5` technically strongest among reviewed names
  - top `5` overall combined
- a short explanation of the fifth file and its three sections

### 3pct-selected-and-watchlist.md

This should contain only names that deserve full trade-level writeups.

For each name, include:

- rank header
- one compact verdict block
- compact fundamental confirmation bullets
- one short technical block each for `Weekly`, `Daily`, `60`, `30`, and `15`
- support inventory table
- resistance inventory table
- entry / stop / first trouble area / swing target
- one short block on why the stop is or is not defendable now

### 3pct-rejected.md

This should be concise, table-first, and evidence-based.

For each stock, include:

- `symbol`
- `fundamental rank`
- `technical review status`
- `primary rejection reason`
- `sponsorship label`
- `best support found`
- `why it was insufficient`
- `re-check or hard reject`

If a stock was not technically reviewed because of a user-imposed limit, it must not be presented as a full technical reject. It should be labeled as `technical review not run in this execution`.

### screen-universe.md

This is the audit appendix. It should prove:

- full HTML coverage across all pages
- pagination handling
- deduplication
- the normalized raw universe used for analysis

### 3pct-ranked-by-stop-safety.md

This is the default decision surface and must contain three sections:

1. `Fundamentally Strongest Top Ten`
2. `Technically Strongest Top Ten`
3. `Overall Combined Ranking`

Rules:

- the first two sections are top-ten only
- the third section must include every stock in the universe
- the third section is the default master ranking
- each row must show whether the stock has been technically reviewed
- reviewed and pending names must be distinguishable

Recommended row fields:

- `Overall Rank`
- `Symbol`
- `Fundamental Rank`
- `Sponsorship Label`
- `Technical Review Status`
- `Technical Label`
- `Combined Verdict`
- `Key Reason`

## Files To Update

The implementation should update:

- `.claude/skills/swing-trading-3pct-screen/SKILL.md`
- `.claude/skills/swing-trading-3pct-screen/references/methodology.md`
- `.claude/skills/swing-trading-3pct-screen/agents/openai.yaml`

The implementation should likely add focused reference files to keep the skill concise:

- `references/fundamental-worker-contract.md`
- `references/technical-worker-contract.md`
- `references/delegation-examples.md`
- `references/reporting-contract.md`

## Implementation Guidance

When implementation begins, use the `skill-creator` skill for the skill-authoring workflow and the `writing-skills` skill as the validation lens.

The implementation should prefer progressive disclosure:

- keep orchestration rules in `SKILL.md`
- keep detailed decision logic in `references/`
- keep delegation contracts and few-shot examples out of the top-level skill body unless they are short enough to justify the token cost

## Scope Check

This remains one focused skill redesign. It does not require:

- changes to TradingView MCP itself
- changes to Screener access patterns beyond HTML parsing
- new external services
- a new plugin

## Spec Review Notes

Inline self-review targets for implementation:

- do not reintroduce hardcoded screen assumptions
- do not let technical logic collapse back into EMA-only behavior
- do not blur the difference between full-universe fundamental ranking and limited technical coverage
- do not let delegation proceed without goal, context, few-shots, and output schema
