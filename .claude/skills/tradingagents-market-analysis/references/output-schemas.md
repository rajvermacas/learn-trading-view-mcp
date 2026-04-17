# Output Schemas

Use this file when inspecting raw JSON outputs from the workflow scripts. Read the exact keys shown here instead of guessing names from memory.

## `stock.json`

Produced by `fetch_stock_data.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "start_date": "2026-01-17",
  "end_date": "2026-04-17",
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
- Price rows are stored under `records`, not `history`.
- `record_count` is the authoritative row count.
- `Date` values are ISO timestamps, not plain `YYYY-MM-DD` strings.

## `indicators.json`

Produced by `fetch_indicator_bundle.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "current_date": "2026-04-17",
  "look_back_days": 90,
  "indicators": [
    {
      "indicator": "rsi",
      "description": "...",
      "series": [
        {"date": "2026-04-16", "value": 74.8}
      ]
    }
  ]
}
```

Notes:
- Each bundle entry is under `indicators`.
- Series values may be `null`.
- If all current values are `null`, treat the bundle as unavailable for that ticker and compute only the minimum manual indicators you need from `stock.json`.

## `fundamentals.json`

Produced by `fetch_fundamentals.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "current_date": "2026-04-17",
  "company_summary": {},
  "balance_sheet": [],
  "cashflow": [],
  "income_statement": [],
  "insider_transactions": [],
  "availability": {
    "balance_sheet": {"status": "available", "reason": null},
    "cashflow": {"status": "unavailable", "reason": "..."}
  }
}
```

Notes:
- Statement tables are top-level arrays such as `balance_sheet` and `income_statement`.
- Availability lives under the top-level `availability` object.

## `company-news.json`

Produced by `fetch_company_news.py`.

```json
{
  "ticker": "BAJAJCON.NS",
  "start_date": "2026-03-18",
  "end_date": "2026-04-17",
  "articles": [
    {
      "title": "Example title",
      "summary": null,
      "publisher": "Example publisher",
      "link": "https://example.com",
      "published_at": "2026-04-10T09:00:00"
    }
  ],
  "availability": {"status": "available", "reason": null}
}
```

Notes:
- News rows live under `articles`.
- `summary`, `publisher`, `link`, and `published_at` may be `null`.
- Empty company news is expressed through `articles: []` plus `availability.status: "unavailable"`.

## `global-news.json`

Produced by `fetch_global_news.py`.

```json
{
  "current_date": "2026-04-17",
  "look_back_days": 14,
  "limit": 5,
  "articles": [
    {
      "title": "Example title",
      "summary": null,
      "publisher": "Example publisher",
      "link": "https://example.com",
      "published_at": null
    }
  ]
}
```

Notes:
- Global news also uses `articles`.
- `summary` can be `null`; guard for that in inspection commands.
- `published_at` can be `null`; missing timestamps are not a parse failure.
