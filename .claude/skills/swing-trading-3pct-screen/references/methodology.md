# Swing Trading 3% Methodology

## Purpose

Rank a user-provided Screener.in stock screen by sponsorship strength and stop survivability around a practical `2%` to `4%` downside zone centered on the usual `3%` reference.

The skill must:

- extract the screen thesis from the user-provided screen before analysis starts
- pre-rank the parsed universe with `PreRankScore` before any fundamental dispatch
- require a user-provided pre-rank cap instead of assuming one
- rank the capped working universe by fundamental sponsorship first
- run technical review only after the fundamental ranking exists
- keep technical review sequential because TradingView MCP is shared mutable state
- write a five-file report set with reviewed versus pending status made explicit
- write one verbose technical dossier for every technically reviewed stock

If any required input, chart state, or company data is missing, stop with a clear exception. Do not invent values.

## Required Inputs

- Screener.in HTML screen URL
- user-provided pre-rank cap for the working universe
- TradingView MCP access or explicit `api_fallback` technical-data mode when
  TradingView MCP is disconnected or unreachable
- fundamental stock-analysis sub-agents with hard concurrency cap `6`
- technical stock-analysis sub-agents available for sequential technical review
- `10 in 1 Different Moving Averages` configured as:
  - `EMA 10`
  - `EMA 20`
  - `EMA 50`
  - `EMA 100`
  - `EMA 200`

## Execution Order

1. Fetch the full Screener universe across all HTML pages.
2. Extract the screen thesis from the screen title, visible filters, and the user’s stated intent.
3. Require the user prompt to provide the pre-rank cap. If it is missing, stop with a clear exception.
4. Compute `PreRankScore` from the visible Screener columns and apply the soft penalties defined below.
5. Sort the parsed universe by adjusted `PreRankScore` descending and keep only the top user-capped names as the working universe.
6. Read `docs/swing-trading/fundamentals/index.md`.
7. Build one fundamental refresh queue from working-universe runtime `missing`, all `hard_stale`, and exactly top `3` `review_due`.
8. Dispatch fundamental workers from that queue with no more than `6` workers inflight at once, using one newly created fundamental worker per stock.
9. As each accepted fundamental result arrives, immediately write the stock dossier and update `index.md` before dispatching another queued fundamental stock.
10. Reuse all `fresh` and remaining `review_due`.
11. Build the capped-universe fundamental sponsorship ranking from dossiers only.
12. Select `technical_data_mode` before technical work starts.
13. If the user specified a technical coverage count such as `analyze 12 stocks`, dispatch one technical worker per stock only for the top `12` fundamentally ranked names; otherwise continue through the full capped universe.
14. Dispatch technical workers only after the ranking exists.
15. Run technical workers strictly one at a time.
16. After each accepted technical result, immediately write that stock's
    technical dossier before dispatching the next technical worker.
17. Synthesize three ranking views, five output files, and the technical
    dossier directory.

The main agent should orchestrate, verify, and synthesize. It should not hold raw per-stock detail longer than necessary.
The main agent alone compares one stock's fundamentals against another stock's fundamentals and assigns the sponsorship ranking across the capped working universe.
The main agent must turn every accepted technical worker result into a
user-facing dossier immediately while the one-stock review context is still
current.

`index.md` is a registry and freshness surface only. Per-stock markdown dossiers are the authoritative ranking inputs, and the main agent must never rank from index rows alone.

## Dispatch Discipline

Sub-agent ownership is always one worker to one stock.

- One fundamental worker analyzes exactly one stock.
- One technical worker analyzes exactly one stock.
- Fundamental workers may be dispatched multiple at a time with bounded concurrency because they do not touch TradingView, but each fundamental worker must process exactly one stock.
- Fundamental worker concurrency is hard-capped at `6` inflight workers.
- Every stock that needs fresh fundamental analysis must be assigned to a newly created fundamental worker.
- A fundamental worker that has already analyzed one stock must never be reused for another stock.
- When one fundamental worker finishes with an accepted dossier, the main agent must persist that dossier immediately before replenishing the queue.
- Fundamental workers do not compare stocks against each other and do not assign cross-stock rank.
- Technical workers must run sequentially because TradingView MCP is shared mutable state.

The main agent must never assign:

- multiple symbols to one worker
- symbol batches such as `stocks 1-5`
- tranche-based prompts such as `analyze these five names together`

If a worker handoff or worker output covers more than one stock, the result is invalid and the main agent must redo that work with one-stock ownership.

## Incremental Fundamental Persistence

Fundamental refresh is a queue, not a wait-for-everything batch.

- The first accepted dossier must be written as soon as it arrives.
- Each later accepted dossier must also be written immediately on receipt.
- The main agent must never wait for all inflight fundamental workers to finish before updating cache files.
- Queue replenishment must happen by creating a new fundamental worker for the next stock, not by reusing a completed one.
- If a dossier is malformed, reject it and redo that one stock.
- If a cache write cannot complete, stop with a clear exception instead of continuing with stale state.

## Screen Thesis Extraction

Before any stock-level work starts, build a compact thesis package from the screen:

- screen title
- visible filter rules
- screen intent
- what kind of sponsorship the screen is trying to surface
- whether the run is full-universe or coverage-limited

Use that thesis in every worker handoff. The thesis is the lens for both fundamental and technical interpretation.

## Pre-Ranked Working Universe

Before any fundamental worker is dispatched, the main agent must reduce the
parsed Screener universe to a user-capped working universe.

Fail fast rules:

- if the user prompt does not specify the pre-rank cap, stop with a clear exception
- if the Screener headers do not contain all four scoring columns below, stop with a clear exception
- column presence is checked from the Screener HTML headers only
- do not assume `15`, do not assume `top 10`, and do not assume the whole parsed universe

### Fixed Screener Columns

The skill assumes this exact visible screen schema:

- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Qtr Profit Var %`
- `Sales Qtr Rs.Cr.`
- `Qtr Sales Var %`
- `ROCE %`
- `3mth return %`

### Pre-Rank Scoring Columns

Only these visible columns contribute to `PreRankScore`:

- `Qtr Profit Var %`
- `Qtr Sales Var %`
- `ROCE %`
- `3mth return %`

### Context-Only Visible Columns

These columns are part of the screen and must remain available for context and reporting, but they do not contribute to `PreRankScore`:

- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

### PreRankScore

Convert each scoring column into a percentile rank within the parsed Screener
universe.

Pre-rank must use only the values already present in the Screener HTML table for
that run. The main agent must not fetch stock-specific pages or other endpoints
to repair missing pre-rank values because that increases cost and defeats the
purpose of this reduction step.

- Base weights:
  - `Qtr Profit Var %`: `0.35`
  - `Qtr Sales Var %`: `0.35`
  - `ROCE %`: `0.20`
  - `3mth return %`: `0.10`

- higher-is-better columns:
  - `Qtr Profit Var %`
  - `Qtr Sales Var %`
  - `ROCE %`
  - `3mth return %`

### Row-Level Value Handling

Column headers are mandatory. Individual row values are not.

For each scoring metric on each stock row:

- if the cell parses as a valid numeric value and is not distorted by the corner cases below, use it in the metric ranking pool
- if the cell is blank, missing, `-`, `--`, `NaN`, or otherwise non-numeric, do not fetch that value elsewhere; assign that metric a percentile contribution of `0` and add a reporting flag
- compute percentile ranks only from valid values for that metric
- ties should receive the same percentile rank

This keeps the run cheap while preventing sparse rows from breaking the flow.

Compute:

`PreRankScore = 0.35 * rank(Qtr Profit Var %) + 0.35 * rank(Qtr Sales Var %) + 0.20 * rank(ROCE %) + 0.10 * rank(3mth return %)`

### Soft Penalties

Apply these deductions after `PreRankScore` is computed.

- if `Qtr Profit Var % <= 0`, subtract `12`
- if `Qtr Sales Var % <= 0`, subtract `12`
- if `ROCE % < 15`, subtract `8`
- if `3mth return % <= 0`, subtract `8`

### Distortion And Corner-Case Rules

The pre-rank must explicitly neutralize row values that can distort the result.

- if `ROCE % < 0`, treat the `ROCE` metric contribution as `0` and subtract `12`
- if `Qtr Profit Var % < 0`, keep the ranked contribution but still apply the negative-growth penalty
- if `Qtr Sales Var % < 0`, keep the ranked contribution but still apply the negative-growth penalty
- if `3mth return % < 0`, keep the ranked contribution but still apply the negative-momentum penalty
- if any scoring metric is missing or invalid for a row, keep that metric contribution at `0`

Rationale:

- `Qtr Profit Var %`, `Qtr Sales Var %`, and `ROCE %` capture the recent operating sponsorship this screen is trying to surface
- `3mth return %` keeps the pre-rank aligned with the user’s momentum-biased universe without overpowering operating evidence
- percentile ranking already limits the damage from unusually large positive values, so extra clipping is not required here

### Selection Rule

- sort by adjusted `PreRankScore` descending
- keep only the top user-capped names
- use that reduced working universe for cache lookup, fundamental refresh,
  fundamental ranking, and later technical review
- do not dispatch any fundamental worker until this selection step is complete
- do not fetch stock-specific pages or other endpoints to repair missing pre-rank values

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

The capped working universe must be ranked from strongest sponsorship to weakest sponsorship before any technical review begins.
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

## Technical Data Source Selection

The main agent must choose and record `technical_data_mode` before dispatching
the first technical worker.

- `tradingview_mcp`: allowed only after `scripts/ensure_socat.sh` succeeds and
  TradingView plus the EMA study setup are verified.
- `api_fallback`: allowed only when TradingView MCP is disconnected or
  unreachable.

When `technical_data_mode=api_fallback`, fetch deterministic technical data from
this skill's local scripts instead of attempting chart actions:

- read `references/api-workflow.md`, `references/api-output-schemas.md`, and
  `references/api-indicators.md`
- resolve an exchange-qualified ticker such as `ATLANTAELE.NS`
- resolve explicit ISO `current_date`, price start date, and look-back days
- run `scripts/fetch_stock_data.py` for OHLCV price history on every required
  interval: `15m`, `30m`, `60m`, `1d`, `1wk`
- run `scripts/fetch_indicator_bundle.py` with exact supported names such as
  `close_10_ema`, `close_20_ema`, `close_50_ema`, `close_100_ema`,
  `close_200_ema`, `close_50_sma`, `close_200_sma`, `macd`, `macds`, `macdh`,
  `rsi`, `boll`, `boll_ub`, `boll_lb`, `atr`, `vwma`, and `mfi` on every
  required interval
- keep stdout JSON and stderr logs in separate files
- read price rows from `stock.json["records"]`
- read indicator rows from `indicators.json["indicators"]`
- treat TradingView as the source-of-truth capability floor: API fallback may
  include more indicators, but it must not include fewer timeframes or EMA
  periods than TradingView mode

Fail fast in API mode when:

- the ticker cannot be resolved to an exchange-qualified symbol
- price history is empty
- a required interval or EMA cannot be supported by the fetched API data
- JSON output is mixed with stderr logs
- required payload keys are missing

If the indicator bundle returns current values that are all `null`, state that
limitation and analyze only OHLCV-derived price structure and volume. Do not
fabricate EMA, momentum, volatility, or volume-indicator signals.

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

## Technical Dossier Persistence

Every technically reviewed stock must produce one dossier under the run folder:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/technical-dossiers/<RANK>-<SYMBOL>.md`

Rules:

- write the dossier immediately after the accepted one-stock technical result
- use the stock's full-universe fundamental rank in the filename
- do not create dossiers for stocks that were not technically reviewed
- do not reuse dossier files as cache or ranking inputs on later runs
- stop with a clear exception if dossier persistence fails

## Number Definitions

- `CMP`: current TradingView price or API close price used for the decision
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

Produce exactly five files plus one dossier directory:

1. `README.md`
2. `3pct-selected-and-watchlist.md`
3. `3pct-rejected.md`
4. `screen-universe.md`
5. `3pct-ranked-by-stop-safety.md`
6. `technical-dossiers/`

### README.md

Include:

- run date and screen URL
- parsed screen thesis
- parsed universe size
- user-specified pre-rank cap
- working-universe size after pre-rank
- coverage mode
- counts for fundamentally analyzed, technically reviewed, selected, watchlist, rejected, and pending technical review
- count of technical dossiers written
- top `5` fundamentally strongest
- top `5` technically strongest among reviewed names
- top `5` overall combined
- a short explanation of how to read the fifth file
- a short explanation of the technical dossier directory
- a short explanation of the pre-rank step and soft penalties

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
- technical dossier filename for reviewed names

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

It must also show:

- adjusted `PreRankScore`
- the fixed screen schema used in that run
- the four scoring columns used for `PreRankScore`
- the six context-only visible columns
- whether the stock made the capped working universe
- the key penalty flags that changed the adjusted score
- the key missing or distorted metric flags that forced zero contribution

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
