# Workflow

## Typical Technical Plus Fundamental Analysis

Use a deterministic temp-directory workflow. The report generator expects file paths, not inline JSON.
Before you inspect any JSON manually, review `references/output-schemas.md` so you use the correct keys.

1. Resolve exact dates and file locations first:

```bash
TICKER="NVDA"
CURRENT_DATE="2026-04-17"
PRICE_LOOKBACK_DAYS=90
NEWS_LOOKBACK_DAYS=30
GLOBAL_NEWS_LOOKBACK_DAYS=14
GLOBAL_NEWS_LIMIT=5
TMP_DIR=$(mktemp -d)
PRICE_START_DATE=$(python3 -c "from datetime import date, timedelta; print((date.fromisoformat('$CURRENT_DATE') - timedelta(days=$PRICE_LOOKBACK_DAYS)).isoformat())")
NEWS_START_DATE=$(python3 -c "from datetime import date, timedelta; print((date.fromisoformat('$CURRENT_DATE') - timedelta(days=$NEWS_LOOKBACK_DAYS)).isoformat())")
```

2. Fetch price history:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_stock_data.py \
  --ticker "$TICKER" \
  --start-date "$PRICE_START_DATE" \
  --end-date "$CURRENT_DATE" \
  > "$TMP_DIR/stock.json" \
  2> "$TMP_DIR/stock.log"
```

3. Fetch a balanced indicator bundle using exact supported names:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_indicator_bundle.py \
  --ticker "$TICKER" \
  --current-date "$CURRENT_DATE" \
  --look-back-days "$PRICE_LOOKBACK_DAYS" \
  --indicators close_10_ema close_50_sma close_200_sma macd macds macdh rsi boll boll_ub boll_lb atr mfi \
  > "$TMP_DIR/indicators.json" \
  2> "$TMP_DIR/indicators.log"
```

4. Fetch fundamentals:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_fundamentals.py \
  --ticker "$TICKER" \
  --current-date "$CURRENT_DATE" \
  > "$TMP_DIR/fundamentals.json" \
  2> "$TMP_DIR/fundamentals.log"
```

5. Fetch company news:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_company_news.py \
  --ticker "$TICKER" \
  --start-date "$NEWS_START_DATE" \
  --end-date "$CURRENT_DATE" \
  > "$TMP_DIR/company-news.json" \
  2> "$TMP_DIR/company-news.log"
```

6. Fetch macro news when needed:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/fetch_global_news.py \
  --current-date "$CURRENT_DATE" \
  --look-back-days "$GLOBAL_NEWS_LOOKBACK_DAYS" \
  --limit "$GLOBAL_NEWS_LIMIT" \
  > "$TMP_DIR/global-news.json" \
  2> "$TMP_DIR/global-news.log"
```

7. `fetch_indicator_bundle.py` already returns the bundle shape expected by the report generator:

```json
{
  "indicators": [
    {"indicator": "rsi", "...": "..."},
    {"indicator": "macd", "...": "..."}
  ]
}
```

If you merge stderr into stdout while capturing these files, the JSON becomes invalid. Keep the `*.log` files separate and inspect those when a fetch looks suspicious.

If the indicator bundle returns entries whose current values are all `null`, treat the bundle as unavailable for that ticker. Keep the generated scaffold, but base your final technical write-up on OHLCV price structure and any manual indicator calculations you derive from `stock.json`.

When you inspect the payloads:

- read stock rows from `stock.json["records"]`, not `stock.json["history"]`
- read news rows from `company-news.json["articles"]` and `global-news.json["articles"]`
- treat `article["summary"]` and `article["published_at"]` as nullable fields

8. Assemble and save the markdown draft under `docs/market-analysis/`:

```bash
python3 .claude/skills/tradingagents-market-analysis/scripts/generate_market_report.py \
  --ticker "$TICKER" \
  --report-date "$CURRENT_DATE" \
  --stock-data "$TMP_DIR/stock.json" \
  --indicators "$TMP_DIR/indicators.json" \
  --fundamentals "$TMP_DIR/fundamentals.json" \
  --company-news "$TMP_DIR/company-news.json" \
  --global-news "$TMP_DIR/global-news.json"
```

9. Open the generated markdown file and replace the placeholder sections with your synthesis. The generated output is a scaffold, not the final answer.

## Recommended Execution Notes

- Validate the ticker format before the fetches. For Indian equities, prefer exchange-qualified symbols such as `ATLANTAELE.NS`.
- Use `references/indicators.md` for exact indicator names.
- Use `references/output-schemas.md` for exact payload keys and nullable fields.
- If you want to parallelize, parallelize steps 2 through 6 only after you have confirmed the argument shapes.
- If news or fundamentals are sparse, report that limitation explicitly instead of filling the gap with speculation.

## Synthesis Expectations

After the scripts run, Codex should:

- explain trend direction
- explain momentum and volatility
- relate fundamentals to valuation or quality
- connect news to catalysts and risks
- make the final recommendation explicitly as an inference
