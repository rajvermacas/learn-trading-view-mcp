# API Technical Data Workflow

Use this workflow only when `technical_data_mode=api_fallback` because
TradingView MCP is disconnected or unreachable. It is local to
`$swing-trading-3pct-screen` and does not depend on another skill at runtime.

This workflow runs inside the one-stock technical sub-agent. The main agent must
not pre-fetch API JSON; it only supplies resolved ticker/date/look-back inputs,
a unique per-stock API output directory, and the script/reference paths in the
technical handoff.

API fallback technical workers must not share writable resources. Shared
read-only script and reference paths are allowed, but JSON files, log files,
temp directories, and report files must be unique to one stock's worker.

Do not write ad hoc Python scripts for API fallback. If the local scripts are
insufficient, patch the bundled scripts in `scripts/` and rerun verification;
otherwise use the bundled scripts exactly.

Before inspecting JSON manually, review
`references/api-output-schemas.md` so payload keys are read exactly.

## Required Inputs

- exchange-qualified ticker, for example `ATLANTAELE.NS`
- explicit ISO `CURRENT_DATE`
- explicit positive integer `PRICE_LOOKBACK_DAYS`
- explicit ISO `PRICE_START_DATE`
- explicit API interval from `15m`, `30m`, `60m`, `1d`, `1wk`
- writable unique per-stock API output directory for JSON and log files

If any input is missing, stop with a clear exception instead of assuming a
default.

TradingView is the source-of-truth capability floor. API fallback must fetch at
least the same timeframe and EMA surface:

- timeframes: `15m`, `30m`, `60m`, `1d`, `1wk`
- EMAs on every timeframe: `close_10_ema`, `close_20_ema`, `close_50_ema`,
  `close_100_ema`, `close_200_ema`

The API fallback may fetch extra indicators, but it must not omit any required
TradingView timeframe or EMA.

## Commands

Use the explicit values from the technical handoff:

```bash
TICKER="ATLANTAELE.NS"
CURRENT_DATE="2026-04-24"
PRICE_LOOKBACK_DAYS=120
PRICE_START_DATE="2025-12-25"
API_OUTPUT_DIR="docs/swing-trading/2026-04-24-134528-utc/api/01-ATLANTAELE"
```

Do not use a shared temp directory such as `/tmp/swing-trading-api` for parallel
technical workers. Use the handoff's unique `API_OUTPUT_DIR`, and stop with a
clear exception if another worker can write to the same directory or filenames.

Fetch OHLCV price history for each required interval:

```bash
INTERVAL="30m"
python3 .claude/skills/swing-trading-3pct-screen/scripts/fetch_stock_data.py \
  --ticker "$TICKER" \
  --start-date "$PRICE_START_DATE" \
  --end-date "$CURRENT_DATE" \
  --interval "$INTERVAL" \
  > "$API_OUTPUT_DIR/stock-$INTERVAL.json" \
  2> "$API_OUTPUT_DIR/stock-$INTERVAL.log"
```

Fetch the technical indicator bundle for each required interval:

```bash
INTERVAL="30m"
python3 .claude/skills/swing-trading-3pct-screen/scripts/fetch_indicator_bundle.py \
  --ticker "$TICKER" \
  --current-date "$CURRENT_DATE" \
  --look-back-days "$PRICE_LOOKBACK_DAYS" \
  --interval "$INTERVAL" \
  --indicators close_10_ema close_20_ema close_50_ema close_100_ema close_200_ema macd macds macdh rsi boll boll_ub boll_lb atr vwma mfi \
  > "$API_OUTPUT_DIR/indicators-$INTERVAL.json" \
  2> "$API_OUTPUT_DIR/indicators-$INTERVAL.log"
```

Keep stdout JSON and stderr logs separate. A mixed log-plus-JSON file is
invalid API evidence.

## Inspection Rules

- read price rows from each `stock-<interval>.json["records"]`, not `history`
- read indicator bundle entries from each
  `indicators-<interval>.json["indicators"]`
- use exact indicator names from `references/api-indicators.md`
- if all current indicator values are `null`, state that limitation and use
  OHLCV-derived price structure and volume only
- if price history is empty, stop with a clear exception
- if one required timeframe cannot be supported by the fetched data, stop with
  a clear exception before making the technical verdict
