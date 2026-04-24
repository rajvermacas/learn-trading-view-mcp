# Technical Worker Contract

## Goal

Determine whether the stock can defend a practical `2%` to `4%` downside zone around the usual `3%` reference.

The worker owns exactly one stock. If the handoff contains multiple stocks, a batch, or a tranche, reject it and require a one-stock redo.

## Context Required From Main Agent

- symbol
- company
- screen thesis
- fundamental rank
- sponsorship label
- ranking reason
- coverage mode
- technical_data_mode
- API payload paths when `technical_data_mode=api_fallback`

## Required Timeframes

- Weekly
- Daily
- 60
- 30
- 15

## Required Factors On Each Relevant Timeframe

- EMA context
- support and resistance zones
- supply and demand zones
- chart patterns
- market structure
- volume analysis

## Decision Discipline

Do not make a technical verdict from:

- EMA distance alone
- one timeframe alone
- clustered EMAs treated as independent support without structural confirmation
- a higher-timeframe chart that looks fine while lower timeframes break the support path into the stop zone
- lower-timeframe weakness ignored because one daily or weekly reference still looks attractive

## Data Source Rules

- `technical_data_mode=tradingview_mcp`: use the verified TradingView chart state.
- `technical_data_mode=api_fallback`: use only the JSON payloads supplied by the
  main agent from this skill's local API scripts.
- In API mode, do not browse or invent missing chart levels.
- In API mode, reject the handoff if the supplied data cannot support one of
  `weekly`, `daily`, `60`, `30`, or `15`.
- In API mode, reject the handoff if any timeframe lacks EMA `10`, `20`, `50`,
  `100`, or `200`.
- In API mode, if indicator values are unavailable, say so and use OHLCV price
  structure only.

## Output Schema

- symbol
- company
- technical_data_mode
- cmp
- 3pct_floor
- practical_stop_zone
- weekly_note
- daily_note
- 60_note
- 30_note
- 15_note
- support_inventory
- resistance_inventory
- entry_zone
- stop_zone
- first_trouble_area
- swing_target
- technical_verdict
- stop_survivability_label
- primary_failure_risk
- ranking_reason
- summary_rationale

The output must cover one stock only.

## Output Quality Bar

- each timeframe note must be detailed enough for the main agent to write a
  user-facing technical dossier without re-reading the chart
- each timeframe note must explicitly discuss market structure, chart patterns,
  and volume analysis instead of implying them indirectly
- `support_inventory` and `resistance_inventory` must preserve timeframe,
  structure type, and price-level evidence instead of loose summaries
- `summary_rationale` must tie the multi-timeframe evidence to the verdict in
  plain language, including how market structure, chart patterns, and volume
  evidence affected the decision
