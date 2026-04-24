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
- exchange-qualified ticker when `technical_data_mode=api_fallback`
- explicit ISO current date when `technical_data_mode=api_fallback`
- explicit price start date when `technical_data_mode=api_fallback`
- explicit positive look-back days when `technical_data_mode=api_fallback`
- API output directory when `technical_data_mode=api_fallback`
- API script and reference paths when `technical_data_mode=api_fallback`

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
- `technical_data_mode=api_fallback`: fetch the one-stock JSON payloads inside
  this technical worker using this skill's local API scripts.
- In API mode, the main agent supplies resolved inputs and paths only. It must
  not supply pre-fetched per-stock JSON for interpretation.
- In API mode, run `scripts/fetch_stock_data.py` for `15m`, `30m`, `60m`,
  `1d`, and `1wk` before making the technical verdict.
- In API mode, run `scripts/fetch_indicator_bundle.py` for the same intervals
  with at least `close_10_ema`, `close_20_ema`, `close_50_ema`,
  `close_100_ema`, and `close_200_ema`.
- In API mode, write script stdout JSON and stderr logs separately in the API
  output directory.
- In API mode, do not browse or invent missing chart levels.
- In API mode, reject the handoff if the fetched data cannot support one of
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

- each timeframe note must be crisp enough for the main agent to write a
  decision-useful technical dossier without re-reading the chart
- each timeframe note must explicitly discuss market structure, chart patterns,
  and volume analysis instead of implying them indirectly
- `support_inventory` and `resistance_inventory` must preserve timeframe,
  structure type, and price-level evidence instead of loose summaries
- `summary_rationale` must tie the multi-timeframe evidence to the verdict in
  plain language, including how market structure, chart patterns, and volume
  evidence affected the decision
