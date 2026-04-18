# Swing Trading 3% Methodology

## Purpose

Rank a user-provided Screener.in stock screen by sponsorship strength and stop survivability around a practical `2%` to `4%` downside zone centered on the usual `3%` reference.

The skill must:

- extract the screen thesis from the user-provided screen before analysis starts
- rank the full universe by fundamental sponsorship first
- run technical review only after the fundamental ranking exists
- keep technical review sequential because TradingView MCP is shared mutable state
- write a five-file report set with reviewed versus pending status made explicit

If any required input, chart state, or company data is missing, stop with a clear exception. Do not invent values.

## Required Inputs

- Screener.in HTML screen URL
- TradingView MCP access
- sequential stock-analysis sub-agents
- `10 in 1 Different Moving Averages` configured as:
  - `EMA 10`
  - `EMA 20`
  - `EMA 50`
  - `EMA 100`
  - `EMA 200`

## Execution Order

1. Fetch the full Screener universe across all HTML pages.
2. Extract the screen thesis from the screen title, visible filters, and the user’s stated intent.
3. Read `docs/swing-trading/fundamentals/index.md`.
4. Create one fundamental worker task per stock for all runtime `missing` and all `hard_stale`.
5. Create one fundamental worker task per stock for exactly top `3` `review_due`.
6. Reuse all `fresh` and remaining `review_due`.
7. Build the full-universe fundamental sponsorship ranking from dossiers only.
8. If the user specified a technical coverage count such as `analyze 12 stocks`, dispatch one technical worker per stock only for the top `12` fundamentally ranked names; otherwise continue through the full universe.
9. Dispatch technical workers only after the ranking exists.
10. Run technical workers strictly one at a time.
11. Synthesize three ranking views and five output files.

The main agent should orchestrate, verify, and synthesize. It should not hold raw per-stock detail longer than necessary.
The main agent alone compares one stock's fundamentals against another stock's fundamentals and assigns the sponsorship ranking across the universe.

`index.md` is a registry and freshness surface only. Per-stock markdown dossiers are the authoritative ranking inputs, and the main agent must never rank from index rows alone.

## Dispatch Discipline

Sub-agent ownership is always one worker to one stock.

- One fundamental worker analyzes exactly one stock.
- One technical worker analyzes exactly one stock.
- Fundamental workers may be dispatched multiple at a time with bounded concurrency because they do not touch TradingView, but each fundamental worker must process exactly one stock.
- Fundamental workers do not compare stocks against each other and do not assign cross-stock rank.
- Technical workers must run sequentially because TradingView MCP is shared mutable state.

The main agent must never assign:

- multiple symbols to one worker
- symbol batches such as `stocks 1-5`
- tranche-based prompts such as `analyze these five names together`

If a worker handoff or worker output covers more than one stock, the result is invalid and the main agent must redo that work with one-stock ownership.

## Screen Thesis Extraction

Before any stock-level work starts, build a compact thesis package from the screen:

- screen title
- visible filter rules
- screen intent
- what kind of sponsorship the screen is trying to surface
- whether the run is full-universe or coverage-limited

Use that thesis in every worker handoff. The thesis is the lens for both fundamental and technical interpretation.

## Fundamental Sponsorship Model

The fundamental stage answers one question:

`What stocks in this screen are most credibly sponsored by recent business evidence, catalyst context, and acceptable near-term fragility?`

Fundamental workers must examine:

- recent trigger
- operating evidence
- earnings quality
- balance-sheet comfort
- catalyst status
- evidence-to-price alignment
- event-risk modifier when relevant

Use screen columns first, then the company page only when context is missing or needs confirmation.

### Sponsorship Labels

Use these labels:

- `Strongly Sponsored`
- `Moderately Sponsored`
- `Mixed`
- `Weakly Sponsored`

Assign labels by evidence quality, not by whether the chart looks attractive.

### News Escalation

News is exception-based, not mandatory.

Use news only when needed to:

- resolve a contradiction between price and fundamentals
- validate a company-specific catalyst
- validate a sector or macro catalyst
- assess near-term event risk

Do not browse news for every stock by default.

### Fundamental Ranking Rule

The full universe must be ranked from strongest sponsorship to weakest sponsorship before any technical review begins.
That comparison is the main agent's responsibility.

Technical review may not reorder the fundamental stage. It only refines stop survivability after sponsorship exists.

The fundamental ranking must be built from:

- fresh accepted worker dossiers for refreshed names
- cached dossiers for reused names

## Technical Stop-Survivability Model

The technical stage answers:

`Can this stock defend a practical 2% to 4% stop zone at or near the current location?`

Every technically reviewed stock must be analyzed across:

- `Weekly`
- `Daily`
- `60`
- `30`
- `15`

Every timeframe must consider all relevant factors, not just EMA distance:

- EMA context
- support and resistance zones
- supply and demand zones
- chart patterns
- market structure

EMA context can support the case, but it cannot be the case.

### Timeframe Roles

- `Weekly`: trend health, major higher low, major resistance, extension risk
- `Daily`: active swing, breakout base, retest quality, visible resistance
- `60`: local invalidation, demand shelf, support density, sloppiness versus control
- `30`: execution frame, lower-timeframe support map, breakout retest, base quality
- `15`: micro higher lows, rejection behavior, and air-pocket risk into the stop zone

### Hard Bans

Do not make a decision from:

- EMA distance alone
- one timeframe alone
- duplicate EMAs treated as separate reasons when structure does not confirm them
- a chart that looks fine on one timeframe but breaks on lower timeframes

Reject or downgrade any setup where lower timeframes contradict the higher-timeframe thesis near the trade location.

## Support Layer Logic

Judge the practical stop zone by the density and quality of support references below `CMP`.

Useful support references include:

- `30` EMA20, EMA50, EMA100, EMA200
- `30` swing low
- `30` pullback base or consolidation shelf
- `30` breakout retest
- `15` swing low
- `15` pullback base or consolidation shelf
- `15` breakout retest
- `60` EMA20, EMA50, EMA100, EMA200
- `60` swing low
- `60` pullback base or prior resistance turned support
- `Daily` EMA10, EMA20
- recent `Daily` swing low
- `Daily` breakout retest shelf
- `Weekly` higher low or base when it sits near the stop zone

Do not count nearly identical levels twice unless they come from clearly different timeframes or structure types.

Prefer support stacks that are:

- independently justified
- spread across the stop band instead of stacked at one point
- structural, not just moving averages
- confirmed on lower timeframes with no clean air pocket from `CMP` to the stop zone

## Ranking Views

Maintain three ranking views:

1. `Fundamental`
   Full universe, strongest sponsorship to weakest sponsorship.
2. `Technical`
   Only technically reviewed names, least likely to most likely to break the stop zone.
3. `Combined`
   Default master ranking with technical review status made explicit.

The combined ranking must not pretend equal certainty for reviewed and pending names in limited runs.

## Technical Review Status

Every stock in the output must be clearly marked as one of:

- `technically reviewed`
- `pending technical review`

If coverage is limited, pending names must not be presented as full technical rejects.

When the user explicitly requests a coverage limit, technical review must start at rank `#1` and proceed downward through the fundamentally ranked list until that limit is reached.

## Number Definitions

- `CMP`: current TradingView price used for the decision
- `3% Floor`: `CMP x 0.97`
- `Practical Stop Zone`: roughly `2%` to `4%` below `CMP`, centered on the usual `3%` reference
- `Entry`: current price only if support is already underneath; otherwise a narrower pullback entry zone
- `Stoploss`: below the lowest defendable support that still respects the practical stop zone logic
- `First Trouble Area`: nearest obvious resistance where a stall is likely
- `Swing Target`: broader target that still respects visible resistance and a roughly `2R` payoff idea
- `Support Map`: the support layers near the stop zone with timeframe, support type, level, and distance below `CMP`

## Output Contract

Create a fresh timestamped directory on each run:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Produce exactly five files:

1. `README.md`
2. `3pct-selected-and-watchlist.md`
3. `3pct-rejected.md`
4. `screen-universe.md`
5. `3pct-ranked-by-stop-safety.md`

### README.md

Include:

- run date and screen URL
- parsed screen thesis
- universe size
- coverage mode
- counts for fundamentally analyzed, technically reviewed, selected, watchlist, rejected, and pending technical review
- top `5` fundamentally strongest
- top `5` technically strongest among reviewed names
- top `5` overall combined
- a short explanation of how to read the fifth file

### 3pct-selected-and-watchlist.md

Include only names that deserve full trade-level writeups.

For each name, include:

- rank header
- verdict block
- fundamental snapshot with the exact fields used
- `Weekly` note
- `Daily` note
- `60` note
- `30` note
- `15` note
- support inventory table
- resistance inventory table
- entry, stoploss, first trouble area, and swing target with reasoning
- explicit technical review status

### 3pct-rejected.md

Keep rejects compact but evidence-based.

For each reject, include:

- one-line verdict reason
- primary failing timeframe or structure issue
- best support found near the stop zone
- why that support was insufficient
- whether the stock is a re-check candidate or a hard reject
- technical review status if the name was not reviewed
- `technical review not run in this execution` when limited coverage prevented chart work

### screen-universe.md

List every stock parsed from the full HTML universe.

### 3pct-ranked-by-stop-safety.md

This is the master ranking file.

It must contain three sections:

1. `Fundamentally Strongest Top Ten`
2. `Technically Strongest Top Ten`
3. `Overall Combined Ranking`

Ordering rules:

- the first two sections are top-ten only
- the combined section includes every stock in the analyzed universe
- the combined section is the default master ranking
- the top row in the combined section is the stock least likely to break the practical stop zone after combining fundamental and technical evidence
- the bottom row is the stock most likely to break and trade through that stop zone

Every row in the ranking file must show:

- symbol
- fundamental rank
- sponsorship label
- technical review status
- technical label or combined verdict
- combined rank
- key reason

## Reporting Rules

- Full-universe fundamental ranking comes first.
- Technical review happens only after that ranking exists.
- Technical analysis must use weekly, daily, 60, 30, and 15.
- Decisions must use EMA context plus structure, not EMA context alone.
- Decisions must use multiple timeframes, not one timeframe alone.
- The practical stop zone should be treated as a `2%` to `4%` band around the usual `3%` reference.
