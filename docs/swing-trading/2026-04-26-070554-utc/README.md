# Swing Trading 3pct Screen Run

- **Run date:** 2026-04-26 07:05:54 UTC
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months/
- **Screen title:** Return over 3 months
- **Visible filters:** `Return over 3months > 30 AND Market Capitalization > 3000`
- **Screen thesis:** momentum-plus-liquidity universe, then operating sponsorship ranked by quarterly profit growth, quarterly sales growth, ROCE, and 3-month return.
- **Parsed universe:** 125 rows across 5 Screener pages; 125 unique symbols.
- **User pre-rank cap:** top 20 stocks.
- **Fundamental coverage:** top 5 pre-ranked stocks.
- **Technical coverage:** top 3 fundamentally ranked stocks.
- **Technical data mode:** `api_fallback`; `ensure_socat.sh` passed, but no TradingView MCP interface was available in this session.
- **Technical dossiers:** `technical-dossiers/` contains 3 reviewed names.

## Counts

| Metric | Count |
|---|---:|
| Parsed universe | 125 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 5 |
| Technically reviewed | 3 |
| Selected | 1 |
| Watchlist | 2 |
| Rejected after technical review | 0 |
| Technical review not run due coverage limit | 2 |

## Top Fundamental Preview

| Rank | Symbol | Verdict | Reason |
|---:|---|---|---|
| 1 | GVT&D | Strongly Sponsored | Cleanest evidence: revenue/PAT/margins, ROCE 54.74%, debt-free quality, order visibility |
| 2 | QPOWER | Strongly Sponsored | Best pre-rank operating momentum, record Q3, HVDC/reactor/BESS order flow |
| 3 | ATLANTAELE | Strongly Sponsored | Transformer capacity/order story, 50.20% ROCE, strong Q3, but very extended |
| 4 | LLOYDSME | Strongly Sponsored | Exceptional growth and utilization, but more commodity/capex complexity |
| 5 | INA | Strongly Sponsored | Solar growth and order book, but higher cyclicality and capex execution risk |

## Top Technical Preview

| Rank | Symbol | Technical Verdict | Stop Survivability |
|---:|---|---|---|
| 1 | GVT&D | Valid Pullback | Moderately Survivable |
| 2 | QPOWER | Near-Valid | Moderate but extended |
| 3 | ATLANTAELE | Near-Valid | Moderate but stretched |

## Top Combined Preview

| Rank | Symbol | Combined View |
|---:|---|---|
| 1 | GVT&D | Best candidate; valid only on pullback/hold near 4528-4595 |
| 2 | QPOWER | Watchlist; wait for pullback discipline around 1365-1385 or breakout above 1430 |
| 3 | ATLANTAELE | Watchlist; avoid chasing, prefer 1723-1744 pullback and wider stop logic |
| 4 | LLOYDSME | Fundamental candidate pending technical review due user coverage limit |
| 5 | INA | Fundamental candidate pending technical review due user coverage limit |

## How To Read The Ranking File

`3pct-ranked-by-stop-safety.md` has three ranking views: the fundamental ranking, the technical stop-safety ranking for reviewed names, and the combined master ranking. Reviewed names carry `api_fallback`; pending names are explicitly marked as technical review not run in this execution.

## Technical Dossiers

Each file under `technical-dossiers/` is a compact audit record for one technically reviewed stock. Dossiers are not reused as cache inputs.

## Pre-Rank Note

The pre-rank used only Screener-visible columns. `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, and `3mth return %` were percentile-ranked, then soft penalties were applied for weak or distorted rows.
