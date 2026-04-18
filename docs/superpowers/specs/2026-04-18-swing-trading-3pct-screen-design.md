# Swing Trading 3pct Screen Skill Redesign

## Goal

Improve the `swing-trading-3pct-screen` skill so the agent evaluates Indian swing-trade candidates by multi-timeframe stop survivability rather than by a rigid single-indicator cutoff, and so every run produces a ranked full-universe report ordered from least likely to most likely to break a practical `2%` to `4%` stop zone.

## Problems In The Current Skill

The current skill text says to use multi-timeframe structure, but the sample run still allowed early rejection based mainly on daily `EMA 10` distance and pattern extrapolation. That created three concrete problems:

1. Names were rejected too early because one timeframe or one moving average failed, even when lower timeframes or nearby structure may have offered a defendable setup.
2. The final report did not include a full-universe ranking from safest to weakest against the stop area.
3. Rejection writeups were too compressed in the wrong way: they were short, but they hid the actual reasoning and therefore did not show enough research quality.

There is also an execution-model gap:

4. A single agent handled the universe and the per-stock chart reading in one thread, which bloated context and made the workflow fragile.

## Design Summary

Keep `3%` as the center reference, but stop treating it as a hard binary wall. The skill should evaluate a practical `2%` to `4%` downside zone and judge whether price is structurally likely to hold above that area. The decision model should rank names by `stop survivability`, not by one EMA being barely inside or outside a fixed threshold.

The redesigned skill will:

- use `weekly`, `daily`, `60`, `30`, and `15` minute structure for every serious candidate
- require both market-structure references and EMA references in the support case
- forbid blanket rejection by extrapolation without minimum direct chart review
- produce `5` report files per run instead of `4`
- add a ranked universe file that orders all analyzed stocks from least likely to most likely to break the `2%` to `4%` stop zone
- require stock-by-stock delegation after universe fetch so the main agent stays focused on orchestration and synthesis
- require those stock-analysis sub-agents to run sequentially, not in parallel, because TradingView MCP uses shared chart state and parallel access can corrupt data

## Execution Architecture

The workflow should be split into two layers.

### Main Agent

The main agent should:

- fetch and parse the Screener HTML universe
- verify TradingView connectivity and EMA-study configuration once
- dispatch one stock-analysis sub-agent per ticker
- run those stock-analysis sub-agents strictly one at a time
- collect normalized stock-level outputs
- build the selection list, rejection list, ranked universe, and README from those outputs

The main agent must not carry the raw chart-reading detail for the whole universe in one thread.

### Stock-Analysis Sub-Agent

Each stock-analysis sub-agent should:

- own exactly one stock
- inspect `Weekly`, `Daily`, `60`, `30`, and `15`
- evaluate both market structure and EMA context
- return a compact structured payload for synthesis rather than long narrative chart logs

### Concurrency Rule

The skill must explicitly forbid parallel stock-analysis sub-agents. TradingView MCP uses a shared mutable chart session, so two workers changing symbols or timeframes at once can create race conditions and corrupt the analysis.

## Evaluation Model

### Reference Zone

- `CMP` remains the decision price
- `3% Floor` remains `CMP x 0.97`
- the actual evaluation band becomes roughly `2%` to `4%` below `CMP`
- supports slightly above or slightly below the exact `3%` floor remain valid context if the structure is strong enough

This means the agent must not reject a setup merely because support sits `0.5%` to `1.0%` outside the exact `3%` line. It must instead judge whether the broader stop area is defendable.

### Required Technical Checks

For every serious candidate, the agent must assess:

- `Weekly`: trend health, extension risk, major higher low, major resistance
- `Daily`: breakout base, retest quality, recent higher low, nearest meaningful resistance
- `60`: local invalidation level, demand shelf, support density near price
- `30`: main lower-timeframe support map, EMA layering, breakout retest, base quality
- `15`: micro higher lows, rejection behavior, air-pocket risk into the stop zone

### Support Classification

The support case must distinguish between:

- structural support: swing lows, pullback bases, breakout retests, prior resistance turned support, consolidation shelves
- dynamic support: EMA 10, 20, 50, 100, 200 where visible and relevant

The agent must not treat multiple nearby EMAs as enough by themselves. Structural references must be present or the name must be downgraded.

### Verdict Buckets

- `Selected Now`: stop area looks defendable now, structure is aligned, and nearby resistance still allows a sensible trade
- `Watchlist / Near-Valid`: setup is close, but price needs tighter entry, one more higher low, or clearer confirmation around the stop zone
- `Rejected For Now`: support is too thin, too low-quality, too widely spaced, or contradicted by lower-timeframe structure

## Ranking Logic

Every run must rank the full analyzed universe in descending order of stop safety:

- `Rank 1` = least likely to break the `2%` to `4%` stop area
- last rank = most likely to break and trade through that stop area

Ranking should consider:

- fundamental quality relative to peers
- weekly and daily alignment
- number of independent support references near the stop area
- quality of structural support, not just quantity
- spacing of support through the band
- lower-timeframe air-pocket risk
- entry extension versus nearby support
- quality of resistance map and practical risk-reward

The skill should require the agent to explain rank with concise evidence, not long narrative paragraphs.

## Report Output

Each run must create a new timestamped directory under `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/` and write these `5` files:

1. `README.md`
2. `3pct-selected-and-watchlist.md`
3. `3pct-rejected.md`
4. `screen-universe.md`
5. `3pct-ranked-by-stop-safety.md`

### README.md

Purpose:

- concise run summary
- counts by verdict
- methodology summary
- top-ranked names preview
- explicit explanation of how the fifth ranked file should be read
- explicit mention that the fifth file contains three sections:
  - fundamentally strongest top ten
  - technically strongest top ten
  - overall combined universe ranking in descending order of fundamental plus technical strength

### 3pct-selected-and-watchlist.md

Purpose:

- full but structured writeups for `Selected Now` and `Watchlist / Near-Valid`

For each name, require:

- fundamental snapshot
- weekly, daily, `60`, `30`, `15` structure blocks
- support inventory
- resistance inventory
- entry / stop / first trouble area / swing target
- concise verdict block explaining why the stop area is or is not defendable now

### 3pct-rejected.md

Purpose:

- concise but evidence-based rejection summaries

For each rejected name, require:

- verdict reason in one line
- primary failing timeframe or structure issue
- best support found near the stop area
- why that support was insufficient
- whether the name is a hard reject or only a future re-check candidate

This file must avoid wall-of-text prose. It should be compact, scan-friendly, and still preserve the reasoning.

### screen-universe.md

Purpose:

- prove full HTML coverage across all Screener pages
- show the raw captured universe and the fields used in filtering and ranking

### 3pct-ranked-by-stop-safety.md

Purpose:

- rank every analyzed stock from safest to weakest against the practical stop zone
- separate pure fundamental leadership, pure technical leadership, and the default combined ranking

This file must contain three sections:

1. `Fundamentally Strongest Top Ten`
2. `Technically Strongest Top Ten`
3. `Overall Combined Ranking`

Section rules:

- `Fundamentally Strongest Top Ten`: rank the ten strongest businesses in the universe by the skill's quality framework, independent of whether the current entry is technically ideal
- `Technically Strongest Top Ten`: rank the ten names whose current structure is strongest against breaking the practical `2%` to `4%` stop zone
- `Overall Combined Ranking`: rank the full universe in descending order using both fundamental quality and technical stop-survivability, with the top name being the least aligned toward breaking the stop zone and the last name being the most likely to break it

Each row should include concise, information-dense fields such as:

- rank
- symbol
- verdict
- `CMP`
- reference stop zone
- support count
- structural support grade
- air-pocket risk
- fundamental quality grade
- short reason

The ordering rules must be explicit:

- the first two sections are top-ten only
- the third section must include every stock in the analyzed universe
- the third section is the default master ranking
- the top row in the third section is the stock least likely to break the `2%` to `4%` stop zone after combining fundamental and technical evidence
- the bottom row in the third section is the stock most likely to break and trade through that stop zone

## Writing Style

The report language must be:

- concise
- precise
- surgical
- complete

It must not become a wall of text. The skill should explicitly favor short evidence blocks, compact tables, and reason summaries that retain decision-critical information.

## Skill Changes Required

Update `.claude/skills/swing-trading-3pct-screen/SKILL.md` to:

- redefine the technical decision model around stop survivability
- soften the exact `3%` boundary into a `2%` to `4%` evaluation band
- forbid rejection by single-indicator logic or broad extrapolation
- require sequential one-stock-per-sub-agent analysis after universe fetch
- require the fifth report file
- require concise but complete reasoning in all output files

Update `.claude/skills/swing-trading-3pct-screen/references/methodology.md` to:

- redefine the methodology around practical stop-zone survivability
- document how to rank names from safest to weakest
- define the main-agent versus stock-sub-agent execution contract
- forbid parallel stock-analysis workers against TradingView MCP
- specify the minimum evidence needed before rejection
- define the concise output format for the ranked and rejected files

## Scope Check

This remains one focused skill redesign. It does not require creating a new plugin, adding new external dependencies, or changing TradingView tooling.
