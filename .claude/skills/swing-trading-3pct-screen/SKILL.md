---
name: swing-trading-3pct-screen
description: Use when screening Indian stocks from a Screener.in HTML universe for swing trades that must be ranked by multi-timeframe stop survivability, fundamental quality, and delegated stock-by-stock sub-agent analysis around a practical `2%` to `4%` downside zone.
---

# Swing Trading 3pct Screen

## Overview

Use this skill for screening Indian stocks from Screener.in and ranking them by how likely they are to hold above a practical stop zone. Keep `3%` as the central reference with `3% Floor = CMP x 0.97`, but do not treat it as a rigid binary wall. The analysis must judge a practical `2%` to `4%` downside zone and decide which names are least likely to violate it.

The main agent must stay lean. Once the screen universe and chart configuration are verified, the per-stock chart analysis must be delegated so one isolated sub-agent owns one stock at a time. These sub-agents must run sequentially, not in parallel, because TradingView MCP works against shared chart state and parallel chart access can corrupt the readings. The main agent should synthesize structured outputs, not carry the raw chart-reading context for the whole universe in one thread.

The output is a five-file markdown report set that is concise, precise, surgical, and complete. It must preserve decision-critical information without turning into a wall of text.

## Workflow

1. Run [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh) first.
2. Confirm TradingView MCP connectivity with `tv_health_check`.
3. Fetch the Screener.in screen as HTML across every page. Do not use the JSON endpoint.
4. Capture the fundamental fields required by [references/methodology.md](references/methodology.md). If required fields cannot be verified from the screen or company page HTML, stop with a clear error.
5. Confirm the chart contains `10 in 1 Different Moving Averages ( SMA/EMA/WMA/RMA/HMA/VWMA )`.
6. Confirm `MA 1-5` are `EMA 10/20/50/100/200` on `Close`. If they are wrong, fix them before analysis. Do not continue with guessed values.
7. Dispatch one isolated sub-agent per stock only after the screen universe and chart setup are verified.
8. Require each stock sub-agent to analyze `weekly`, `daily`, `60`, `30`, and `15` minute charts for its assigned stock only.
9. Require each stock sub-agent to return a compact structured result defined by [references/methodology.md](references/methodology.md).
10. Run stock sub-agents sequentially so only one worker touches TradingView MCP at a time.
11. Build the final multi-timeframe market-structure map from those stock-level outputs, not from a single monolithic analysis thread.
12. Apply the selection and ranking rules from [references/methodology.md](references/methodology.md).
13. Rank the full universe from least likely to most likely to break the practical stop zone.
14. Create a fresh timestamped report directory under `docs/swing-trading/`.
15. Write the five-file markdown report set inside that timestamped directory.

## Screen Fetch Rules

- Fetch the user-provided Screener.in screen URL directly as HTML.
- Follow every page shown by pagination text such as `Showing page 1 of 2`.
- Deduplicate by company slug from `/company/<slug>/`.
- Record the full universe, not just selected names.
- Capture the raw screen columns used for quality filtering and ranking.
- If a candidate needs confirmation beyond the screen table, fetch the Screener company page as HTML and extract the missing fields there.
- Fail fast if the screen table or pagination text cannot be found.
- Do not use `?format=json` or any sign-in-protected export path.

## TradingView Rules

- Ensure the `socat` tunnel exists before any TradingView MCP calls.
- Use `quote_get`, `chart_get_state`, `data_get_indicator`, and `data_get_study_values` to verify the chart state.
- Use the EMA stack from the `10 in 1` study as context, not as the only decision input.
- Use `weekly`, `daily`, `60`, `30`, and `15` minute timeframes for every stock analysis sub-agent.
- Treat TradingView MCP as a single shared mutable chart session. Never run chart-manipulating stock-analysis sub-agents in parallel.
- On each timeframe, inspect structure directly: recent swing highs and lows, pullback bases, breakout retests, prior resistance turned support, consolidation shelves, visible rejection levels, and nearby resistance.
- Use the `30` minute chart as the main lower-timeframe deep-dive for support and resistance mapping, EMA layering, and validation of the hourly structure.
- Require evidence from both structure and EMA context. Multiple nearby EMAs alone are not enough for a high-conviction support case.
- Treat supports slightly above or slightly below the exact `3% Floor` as valid context when the broader `2%` to `4%` stop zone is structurally defendable.
- Prefer current-price setups only when support is already stacked directly below price across more than one timeframe.
- Downgrade names where lower-timeframe structure shows an air pocket between `CMP` and the stop zone even if the daily chart looks strong.
- Do not reject a name from one indicator or one timeframe alone.
- Do not use blanket extrapolation labels for unreviewed names. Every rejection still needs minimum direct chart evidence and a concrete reason.
- If the chart setup is missing or TradingView is unreachable, stop with a clear error instead of inventing levels.

## Delegation Rules

- After the screen universe is fetched and the chart study is verified, do the stock analysis in isolated sub-agents rather than in the main agent thread.
- One stock sub-agent owns one ticker only.
- Run stock sub-agents strictly sequentially. Do not execute them in parallel because TradingView MCP chart state is shared and race conditions will corrupt the analysis.
- The main agent is responsible for universe fetch, setup validation, dispatch, deduplication, ranking, report writing, and consistency checks across stocks.
- Each stock sub-agent is responsible for one compact evidence package: fundamentals, multi-timeframe structure notes, support inventory, resistance inventory, verdict, and ranking reason.
- Stock sub-agents should return structured concise evidence only. They should not dump long chart narration back into the main thread.
- If a stock sub-agent omits required fields or fails to verify required evidence, reject that result and rerun or mark the stock as analysis-failed with a clear reason.
- Do not synthesize the ranked universe until every stock has either a valid sub-agent result or an explicit analysis failure note.

## Report Output

Create a new folder first:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Write these files inside that folder:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/README.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/3pct-selected-and-watchlist.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/3pct-rejected.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/screen-universe.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/3pct-ranked-by-stop-safety.md`

Keep the report readable:

- `README.md`: short run summary, counts, methodology summary, top-ranked preview, and an explanation of the fifth file.
- `3pct-selected-and-watchlist.md`: structured reasoning for selected and near-valid names, including fundamentals, multi-timeframe structure, support inventory, resistance inventory, and trade levels.
- `3pct-rejected.md`: concise but evidence-based rejection summaries for the rest of the universe. Avoid wall-of-text prose.
- `screen-universe.md`: raw full-screen appendix proving that all pages were covered.
- `3pct-ranked-by-stop-safety.md`: the ranked file with three sections:
  - `Fundamentally Strongest Top Ten`
  - `Technically Strongest Top Ten`
  - `Overall Combined Ranking`
- Use a fresh timestamped folder on every run so older analyses remain intact.

For `3pct-ranked-by-stop-safety.md`, enforce these ordering rules:

- The first section ranks the ten strongest businesses by the quality framework.
- The second section ranks the ten strongest current technical structures against the practical stop zone.
- The third section is the default master ranking and must include every stock in the analyzed universe.
- The top row in the third section is the stock least likely to break the practical `2%` to `4%` stop zone after combining fundamental and technical evidence.
- The bottom row in the third section is the stock most likely to break and trade through that stop zone.
- The master ranking must be built from the normalized stock sub-agent outputs so every row has comparable evidence.

For each selected or watchlist name, explicitly include:

- `Fundamental Quality`: exact fields used and why the name passed or failed the quality bar.
- `Market Structure Summary`: one short block each for `weekly`, `daily`, `60`, `30`, and `15`.
- `Support Inventory`: every relevant support near the stop zone with timeframe, support type, level, distance from `CMP`, and whether it sits above the reference floor.
- `Resistance Inventory`: nearest resistances above `CMP` with timeframe, structure type, level, and why they matter for `First Trouble Area` and `Swing Target`.
- `Entry / Stop / First Trouble Area / Swing Target`: each tied back to visible structure.
- `Verdict Block`: one concise decision paragraph explaining why the stop zone is or is not defendable now.

## Number Discipline

- Explain every number you publish.
- `3% Floor` must be `CMP x 0.97`.
- Judge stop survivability across a practical `2%` to `4%` downside zone around that floor.
- `Stoploss` should usually cluster near the `3%` reference, but slight deviation is acceptable when structure justifies it.
- `Entry` must be either current price or a tightly defined pullback zone.
- `First Trouble Area` must be the nearest clear resistance.
- `Swing Target` must be tied to resistance and at least a defensible `2R` style framework.
- Every support level must be linked to a named timeframe and structure type.
- If a valid setup does not exist, reject it or keep it on watch. Do not invent support or stretch the reasoning.

## Writing Style

- Be concise, precise, surgical, and complete.
- Prefer compact tables, short evidence blocks, and one-line verdicts over long narrative paragraphs.
- Do not drop material information just to sound brief.
- Be direct about weak setups.
- Name the timeframe whenever citing a support or resistance level.
- Mention the date so the report is clearly point-in-time.

## Resource Use

- Use [references/methodology.md](references/methodology.md) for the fundamental and technical filters, ranking logic, and report language.
- Use [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh) for the TradingView prerequisite instead of rewriting that shell logic.
