# Swing Trading 3% Methodology

## Goal

Find the stocks in a Screener.in universe that are fundamentally strong and least likely to break a practical `2%` to `4%` stop zone around the usual `3%` reference.

## Required Inputs

- Screener.in HTML screen URL
- TradingView MCP access
- the ability to run stock-analysis sub-agents sequentially
- `10 in 1 Different Moving Averages` study configured as:
  - `MA 1 = EMA 10 on Close`
  - `MA 2 = EMA 20 on Close`
  - `MA 3 = EMA 50 on Close`
  - `MA 4 = EMA 100 on Close`
  - `MA 5 = EMA 200 on Close`
- Fundamental data required for each shortlisted candidate:
  - quarterly sales growth
  - quarterly profit growth
  - ROCE
  - debt quality or leverage context from the screen or company page

If any required chart state or required fundamental data cannot be verified, stop or reject with a clear reason. Do not assume missing values.

## Execution Model

Keep the main agent focused on orchestration and synthesis:

- fetch the full Screener universe
- verify TradingView connectivity and EMA study configuration once
- dispatch one stock-analysis sub-agent per ticker
- run those stock-analysis sub-agents strictly one at a time
- synthesize the returned stock-level evidence into selections, rejections, and rankings

Treat TradingView MCP as a single shared chart session:

- never run stock-analysis sub-agents in parallel
- never let two workers mutate chart symbol or timeframe at the same time
- fail fast if the orchestration layer cannot guarantee sequential chart access

Each stock-analysis sub-agent must return a compact structured payload with:

- symbol
- CMP
- `3% Floor`
- practical stop zone
- verdict
- fundamental quality summary
- `Weekly`, `Daily`, `60`, `30`, and `15` notes
- support inventory
- resistance inventory
- primary risk
- ranking reason

If a stock-analysis sub-agent omits a required field, that stock result is invalid and must be rerun or explicitly marked as analysis-failed.

## Timeframes

- `Weekly`: trend, major higher low, major resistance, extension risk
- `Daily`: active swing, breakout base, retest quality, nearest meaningful resistance
- `60`: local invalidation, demand shelf, support density near price
- `30`: main lower-timeframe support map, EMA layering, breakout retest, base quality
- `15`: micro higher lows, rejection behavior, air-pocket risk into the stop zone

## Fundamental Filter

Use the screen columns first, then the Screener company page when a shortlisted name needs missing context confirmed.

Require for `Selected Now` names:

- positive quarterly profit growth
- positive quarterly sales growth
- acceptable or strong ROCE relative to the screen universe
- no obvious balance-sheet stress, profit collapse, or business deterioration

Allow `Watchlist / Near-Valid` names only when:

- the business quality is still acceptable
- one quality field is merely average rather than clearly strong
- the technical setup is close but not yet actionable

Downgrade or reject when:

- profit growth is sharply negative
- sales growth is sharply negative
- ROCE is weak relative to the universe
- debt or leverage profile is clearly unsafe for a tight-stop swing
- the chart is good but fundamentals are too weak to justify a tight-stop swing

## Technical Filter

`Selected Now`:

- weekly trend is bullish or clearly constructive
- daily structure is bullish and clean
- hourly structure is constructive and not sloppy
- `30` minute structure confirms the hourly thesis with visible support layering and clean resistance mapping
- `15` minute structure confirms there is no obvious air pocket straight into the stop zone
- the support case includes both structural references and EMA references
- price is close enough to the support cluster that a defendable stop can sit inside or close to the usual `3%` reference

`Watchlist / Near-Valid`:

- the broader trend is good
- support exists near the practical stop zone
- the entry is still too extended, the support stack is not dense enough yet, or `60`, `30`, or `15` structure is not clean enough

`Reject For Now`:

- no credible support map exists near the practical stop zone
- the support case relies mostly on duplicate EMAs and lacks real structure
- lower timeframes show an air pocket into the stop area
- daily, hourly, `30`, or `15` structure is too messy for a tight-stop swing
- fundamentals are too weak relative to the rest of the screen
- every rejection must cite the primary failing timeframe or structure issue

## Support Layer Logic

Count support references near the practical `2%` to `4%` stop zone below `CMP`. Stronger cases usually have several of these clustered together:

- `30` minute EMA20
- `30` minute EMA50
- `30` minute EMA100
- `30` minute EMA200
- `30` minute swing low
- `30` minute pullback base or consolidation shelf
- `30` minute breakout retest
- `15` minute swing low
- `15` minute pullback base or consolidation shelf
- `15` minute breakout retest
- `60` EMA20
- `60` EMA50
- `60` EMA100
- `60` EMA200
- `60` swing low
- `60` pullback base or prior resistance turned support
- `Daily` EMA10
- `Daily` EMA20
- recent `Daily` swing low
- `Daily` breakout retest shelf
- `Weekly` higher low or base if it sits near the stop zone

Do not count duplicated references at nearly the same price as separate support unless they come from clearly different timeframes or structure types.

Judge both density and spacing. A support stack is stronger when:

- supports are independently justified
- supports are distributed through the band instead of sitting at one tight cluster
- structural supports exist, not just moving averages
- lower timeframes confirm there is no clean air pocket from `CMP` to the stop zone

## Market Structure Checks

For every serious stock, read the chart from higher to lower timeframe:

- `Weekly`: confirm the broader trend, major higher low, and whether price is extended into resistance
- `Daily`: map the active swing, nearest resistance, prior breakout zone, and the most recent meaningful higher low
- `60`: identify the active pullback, local demand shelf, and where the setup becomes structurally invalid
- `30`: map the lower-timeframe support stack, nearest resistance shelves, EMA alignment, and the key levels that define whether price still has room to hold above the stop zone
- `15`: inspect the immediate path below `CMP` for micro higher lows, rejection candles, base building, or an air pocket straight to the stop area

Reject or downgrade the setup if lower timeframes contradict the higher-timeframe thesis near the trade location.

## Ranking Logic

Rank higher when a stock has:

- stronger fundamentals than peers in the same screen
- clear `Weekly` and `Daily` alignment
- more independently justified supports near the stop zone
- better distribution of supports across `Daily`, `60`, `30`, and `15`
- cleaner lower-timeframe structure with fewer air pockets
- a support case built from both structure and EMA context
- a workable resistance map and acceptable risk-reward

Rank lower when:

- the name is extended from support
- support depends mostly on one level or one support type
- lower timeframes are loose or contradictory
- the fundamental case is merely acceptable rather than strong
- the stock result is incomplete, weakly evidenced, or suspicious because sequential TradingView access was not preserved

## Number Definitions

- `CMP`: current TradingView price used for the decision
- `3% Floor`: `CMP x 0.97`
- `Practical Stop Zone`: roughly `2%` to `4%` below `CMP`, centered on the usual `3%` reference
- `Entry`: current price only if support is already underneath, otherwise define a narrower pullback entry zone
- `Stoploss`: below the lowest defendable support that still respects the practical stop zone logic
- `First Trouble Area`: nearest obvious resistance where a stall is likely
- `Swing Target`: broader target that still respects visible resistance and supports a roughly `2R` style payoff
- `Support Map`: the exact layers near the stop zone with timeframe, support type, level, and distance below `CMP`

## Output Structure

Create a fresh timestamped directory on each run:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Produce five files inside that directory:

- `README.md`: summary, counts, methodology snapshot, top-ranked preview, and how to read the fifth file
- `3pct-selected-and-watchlist.md`: full writeups for selected and watch names
- `3pct-rejected.md`: concise but evidence-based rejection summaries
- `screen-universe.md`: all names scraped from all HTML pages
- `3pct-ranked-by-stop-safety.md`: structured ranking file

The ranked file must contain three sections:

1. `Fundamentally Strongest Top Ten`
2. `Technically Strongest Top Ten`
3. `Overall Combined Ranking`

Ordering rules:

- the first two sections are top-ten only
- the third section must include every stock in the analyzed universe
- the third section is the default master ranking
- the top row in the third section is the stock least likely to break the practical stop zone after combining fundamental and technical evidence
- the bottom row in the third section is the stock most likely to break and trade through that stop zone

Each selected or watchlist writeup must show:

- fundamental quality snapshot with the exact fields used
- `Weekly` structure note
- `Daily` structure note
- `60` structure note
- `30` minute structure note
- `15` minute structure note
- support inventory table with timeframe and support type
- resistance inventory table with timeframe and structure type
- entry, stoploss, first trouble area, and swing target with reasoning
- one concise verdict block on stop survivability

Each rejected name must still preserve reasoning in compact form:

- verdict reason in one line
- primary failing timeframe or structure issue
- best support found near the stop zone
- why that support was insufficient
- whether the name is a hard reject or a future re-check candidate

## Writing Style

- explain why each chosen setup is less likely than peers to break the practical stop zone
- be direct about weak setups
- if nothing qualifies, say so clearly
- use exact numbers and tie each number back to structure or EMA support
- name the timeframe whenever citing a support or resistance level
- mention the date so the report is clearly point-in-time
- keep the language concise, precise, surgical, and complete
- avoid wall-of-text output by preferring compact tables and short evidence blocks
