---
name: swing-trading-3pct-screen
description: Use when screening Indian stocks from a Screener.in HTML universe for swing trades that must respect a hard 3% stop and require multi-timeframe TradingView structure analysis plus fundamental quality filtering.
---

# Swing Trading 3pct Screen

## Overview

Use this skill for the exact workflow of screening Indian stocks from Screener.in and narrowing them to swing-trade candidates that are least likely to violate a hard 3% stop. The output is a markdown report that explains every number used for entry, stoploss, first trouble area, swing target, and every support level sitting between current price and the 3% floor.

## Workflow

1. Run [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh) first.
2. Confirm TradingView MCP connectivity with `tv_health_check`.
3. Fetch the Screener.in screen as HTML across every page. Do not use the JSON endpoint.
4. Capture the fundamental fields required by [references/methodology.md](references/methodology.md). If required fields cannot be verified from the screen or company page HTML, stop with a clear error.
5. Confirm the chart contains `10 in 1 Different Moving Averages ( SMA/EMA/WMA/RMA/HMA/VWMA )`.
6. Confirm `MA 1-5` are `EMA 10/20/50/100/200` on `Close`. If they are wrong, fix them before analysis. Do not continue with guessed values.
7. Analyze weekly, daily, `60`, `30`, and `15` minute charts for every serious candidate.
8. Build a multi-timeframe market-structure map, not just an EMA map. Check swing highs/lows, breakout and retest zones, consolidation shelves, rejection lows, and nearby resistance.
9. Apply the selection rules from [references/methodology.md](references/methodology.md).
10. Create a fresh timestamped report directory under `docs/swing-trading/`.
11. Write the markdown report set inside that timestamped directory.

## Screen Fetch Rules

- Fetch the user-provided Screener.in screen URL directly as HTML.
- Follow every page shown by pagination text such as `Showing page 1 of 2`.
- Deduplicate by company slug from `/company/<slug>/`.
- Record the full universe, not just the selected names.
- Capture the raw screen columns used for the quality filter and ranking.
- If a candidate needs confirmation beyond the screen table, fetch the Screener company page as HTML and extract the missing fields there.
- Fail fast if the screen table or pagination text cannot be found.
- Do not use `?format=json` or any sign-in-protected export path.

## TradingView Rules

- Ensure the `socat` tunnel exists before any TradingView MCP calls.
- Use `quote_get`, `chart_get_state`, `data_get_indicator`, and `data_get_study_values` to verify the chart state.
- Use the EMA stack from the `10 in 1` study as context, not as the only decision input.
- Use weekly, daily, `60`, `30`, and `15` minute timeframes for every actionable name.
- On each timeframe, inspect structure directly: recent swing highs and lows, pullback bases, breakout retests, prior resistance turned support, consolidation shelves, and visible rejection levels.
- Use the `30` minute chart as the main lower-timeframe deep-dive for moving averages, support and resistance mapping, and validation of the hourly structure.
- Require evidence that multiple support references sit between CMP and the `3% Floor`, and list each support with its timeframe and support type.
- Prefer current-price setups only when support is already stacked directly below price across more than one timeframe.
- Reject or downgrade names where lower-timeframe structure shows an air pocket between CMP and the stop area even if the daily chart looks strong.
- If the chart setup is missing or TradingView is unreachable, stop with a clear error instead of inventing levels.

## Report Output

Create a new folder first:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/`

Write these files inside that folder:

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/README.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/3pct-selected-and-watchlist.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/3pct-rejected.md`
- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/screen-universe.md`

Keep the report readable:

- `README.md`: short summary, counts, and top table.
- `3pct-selected-and-watchlist.md`: full reasoning for selected and near-valid names, including fundamental snapshot, multi-timeframe structure summary, and support table.
- `3pct-rejected.md`: compact rejection table for the rest of the universe, with the failed condition called out.
- `screen-universe.md`: raw full-screen appendix proving that all pages were covered.
- Use a fresh timestamped folder on every run so older analyses remain intact.

For each selected or watchlist name, explicitly include:

- `Fundamental Quality`: the exact fields used and why the name passed or failed the quality bar.
- `Market Structure Summary`: one short block each for weekly, daily, hourly, `30` minute, and `15` minute charts.
- `Support Inventory`: every support between CMP and the `3% Floor` with columns for timeframe, support type, level, distance from CMP, and whether it sits above the stop.
- `Resistance Inventory`: the nearest resistances above CMP with timeframe, structure type, level, and why they matter for `First Trouble Area` and `Swing Target`.
- `Entry / Stop / First Trouble Area / Swing Target`: each tied back to visible structure.

## Number Discipline

- Explain every number you publish.
- `3% Floor` must be `CMP x 0.97`.
- `Stoploss` must stay at or above that floor.
- `Entry` must be either current price or a tightly defined pullback zone.
- `First Trouble Area` must be the nearest clear resistance.
- `Swing Target` must be tied to resistance and at least a defensible `2R` style framework.
- Every support level must be linked to a named timeframe and structure type.
- If a valid setup does not exist inside the 3% risk rule, reject it or keep it on watch. Do not stretch the stop.

## Resource Use

- Use [references/methodology.md](references/methodology.md) for the fundamental and technical filters, ranking logic, and report language.
- Use [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh) for the TradingView prerequisite instead of rewriting that shell logic.
