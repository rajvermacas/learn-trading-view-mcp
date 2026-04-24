# API Output Schemas

Use this file when inspecting raw JSON outputs from the local API fallback
scripts. Read the exact keys shown here instead of guessing names from memory.

## `stock.json`

Produced by `scripts/fetch_stock_data.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "start_date": "2026-01-17",
  "end_date": "2026-04-17",
  "interval": "1d",
  "record_count": 58,
  "columns": ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"],
  "records": [
    {
      "Date": "2026-01-19T00:00:00",
      "Open": 280.7,
      "High": 284.7,
      "Low": 275.9,
      "Close": 276.55,
      "Adj Close": 276.55,
      "Volume": 980338
    }
  ]
}
```

Notes:

- price rows are stored under `records`, not `history`
- `record_count` is the authoritative row count
- `Date` values are ISO timestamps, not plain `YYYY-MM-DD` strings

## `indicators.json`

Produced by `scripts/fetch_indicator_bundle.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "current_date": "2026-04-17",
  "look_back_days": 90,
  "interval": "1d",
  "indicators": [
    {
      "indicator": "rsi",
      "interval": "1d",
      "description": "...",
      "series": [
        {"date": "2026-04-16", "value": 74.8}
      ]
    }
  ]
}
```

Notes:

- each bundle entry is under `indicators`
- series values may be `null`
- if all current values are `null`, treat the bundle as unavailable for that
  ticker and compute only the minimum manual observations needed from OHLCV
