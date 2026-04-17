# Troubleshooting

Use this file when the skill workflow fails during execution.

## Common Failures

### `fetch_stock_data.py: error: the following arguments are required: --start-date --end-date`

Cause: `fetch_stock_data.py` does not accept `--days`.

Fix: derive explicit ISO dates and pass both:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_stock_data.py \
  --ticker ATLANTAELE.NS \
  --start-date 2026-01-17 \
  --end-date 2026-04-17
```

### `fetch_fundamentals.py: error: the following arguments are required: --current-date`

Cause: fundamentals are keyed off a single analysis date, not a range.

Fix:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_fundamentals.py \
  --ticker ATLANTAELE.NS \
  --current-date 2026-04-17
```

### `fetch_company_news.py: error: the following arguments are required: --start-date --end-date`

Cause: company news also uses explicit date boundaries, not `--days`.

Fix:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_company_news.py \
  --ticker ATLANTAELE.NS \
  --start-date 2026-03-17 \
  --end-date 2026-04-17
```

### `fetch_indicator_bundle.py` usage shows missing `--current-date`, `--look-back-days`, or `--indicators`

Cause: indicator bundles require all three.

Fix: pick names from `references/indicators.md` and pass them explicitly:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_indicator_bundle.py \
  --ticker ATLANTAELE.NS \
  --current-date 2026-04-17 \
  --look-back-days 90 \
  --indicators close_10_ema close_50_sma close_200_sma macd macds macdh rsi boll boll_ub boll_lb atr mfi
```

### `FileNotFoundError` or `load_json_file(...)` failure inside `generate_market_report.py`

Cause: the report generator expects paths to existing JSON files. It does not accept inline JSON captured in shell variables.

Fix: write the upstream outputs to files first, then pass those file paths:

```bash
TMP_DIR=$(mktemp -d)
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_stock_data.py \
  --ticker ATLANTAELE.NS \
  --start-date 2026-01-17 \
  --end-date 2026-04-17 > "$TMP_DIR/stock.json"
```

### `json.decoder.JSONDecodeError: Extra data` or mixed log lines inside `stock.json`

Cause: stderr was merged into stdout with `2>&1` while capturing JSON. The scripts log to stderr, so combining the streams contaminates the JSON file.

Fix: keep the output streams separate and inspect the log file independently:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_stock_data.py \
  --ticker PARKHOSPS.NS \
  --start-date 2026-01-17 \
  --end-date 2026-04-17 \
  > "$TMP_DIR/stock.json" \
  2> "$TMP_DIR/stock.log"
```

If you already wrote a mixed file, discard it and re-fetch. Do not try to strip log lines heuristically.

### The generated report still contains placeholder text

Cause: `generate_market_report.py` produces a deterministic scaffold, not the final investment write-up.

Fix: open the generated markdown file and replace the placeholder sections with your own synthesis grounded in the fetched data.

### One failed parallel shell call cancels other fetches

Cause: some agent shells cancel sibling calls when one parallel command exits non-zero.

Fix: validate the command contract from `references/workflow.md` first, then parallelize only the independent fetch commands that already have the correct argument shapes.

### `company_news["articles"]` is empty

Cause: Yahoo Finance news coverage is often sparse for smaller or regional tickers.

Fix: treat the empty result as a data limitation, mention it explicitly in the analysis, and avoid inferring a bullish or bearish narrative from the absence of articles.

### Manual inspection shows `Total rows: 0` even though `record_count` is non-zero

Cause: you likely read the wrong key from `stock.json`. The price history lives under `records`, not `history`.

Fix: inspect the payload shape first, then read the correct array:

```bash
python3 -c 'import json,sys; data=json.load(sys.stdin); print(data["record_count"]); print(len(data["records"]))' < "$TMP_DIR/stock.json"
```

### `fetch_indicator_bundle.py` succeeds but the indicator values are all `null`

Cause: some tickers come back with insufficient or misaligned source data for `stockstats`, even though the OHLCV history itself is present.

Fix: treat the bundle as unavailable for that ticker instead of fabricating signals. Use `stock.json` to analyze price structure, trend, and volume directly, and manually derive a minimal set of indicators from OHLCV if needed. State that fallback explicitly in the final report.

### `TypeError: 'NoneType' object is not subscriptable` while printing article summaries

Cause: news payloads can contain `summary: null`, and ad-hoc inspection code often assumes `summary` is always a string.

Fix: guard nullable fields explicitly:

```bash
python3 -c 'import json,sys; data=json.load(sys.stdin); [print((article.get("summary") or "")[:150]) for article in data["articles"]]' < "$TMP_DIR/global-news.json"
```

Do the same for `published_at`, `publisher`, and `link` if you format them in quick inspection scripts.
