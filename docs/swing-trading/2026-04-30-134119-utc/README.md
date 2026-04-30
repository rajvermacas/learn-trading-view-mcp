# Swing Trading 3% Screen — 2026-04-30

## Run Details

- **Run Date:** 2026-04-30
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Technical Data Mode:** api_fallback (TradingView MCP disconnected)

## Screen Thesis

**"Return over 3 months"** — Momentum screen filtering for mid-to-large cap Indian stocks (market cap > 3000 Cr) with >30% three-month price return. The intent is to surface stocks where strong recent price momentum is backed by genuine operating sponsorship (quarterly profit growth, sales growth, capital efficiency) suitable for swing trading within a practical 2-4% stop band.

## Universe and Coverage

| Metric | Count |
|---|---|
| Full parsed universe | 113 stocks |
| Pre-rank cap (user-specified) | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 |
| Technically reviewed | 15 |
| Pending technical review | 5 |
| **Selected (trade-ready)** | **3** |
| **Watchlist** | **8** |
| **Rejected** | **4** |
| Technical dossiers written | 15 |

## Pre-Rank Step

PreRankScore computed from 4 scoring columns: `Qtr Profit Var %` (0.35), `Qtr Sales Var %` (0.35), `ROCE %` (0.20), `3mth return %` (0.10). Percentile ranks within the 113-stock universe, then soft penalties applied: -12 for negative profit/sales growth, -8 for ROCE < 15%, -8 for negative 3-month return, -12 for negative ROCE. Top 20 by adjusted PreRankScore became the working universe.

## Fundamental Refresh

- **Fresh (reused):** 16 stocks
- **Review due (refreshed):** 3 (SKYGOLD, RUBICON, RRWL)
- **Missing (new):** 1 (HFCL)
- **Hard stale:** 0

## Top 5 Fundamentally Strongest

1. **ENGINERSIN** — Engineers India Ltd (Strongly Sponsored, High confidence)
2. **ORIANA** — Oriana Power Ltd (Strongly Sponsored, High confidence)
3. **GVT&D** — GE Vernova T&D India Ltd (Strongly Sponsored, High confidence)
4. **BSE** — BSE Ltd (Strongly Sponsored, High confidence)
5. **LLOYDSME** — Lloyds Metals & Energy Ltd (Strongly Sponsored, Medium-High)

## Top 5 Technically Strongest (among reviewed)

1. **ENGINERSIN** — Best Aligned, HIGH stop survivability
2. **BSE** — Best Aligned, Strong stop survivability
3. **ORIANA** — Best Aligned, Moderate stop survivability (ATR caution)
4. **GVT&D** — Near-Valid, Borderline (timing issue, not quality)
5. **LLOYDSME** — Near-Valid, Thin Ice (parabolic)

## Top 5 Overall Combined

1. **ENGINERSIN** — Fund #1 + Best Aligned = strongest combined conviction
2. **BSE** — Fund #4 + Best Aligned = densely defended stop with catalyst
3. **ORIANA** — Fund #2 + Best Aligned = strong but ATR-wide, manage with daily-close stops
4. **GVT&D** — Fund #3 + Near-Valid = excellent quality, wait for 30m reversal confirmation
5. **LLOYDSME** — Fund #5 + Near-Valid = strong fundamentals, parabolic structure limits entry

## How to Read 3pct-ranked-by-stop-safety.md

The fifth file contains three sections: (1) Fundamentally Strongest Top Ten, (2) Technically Strongest Top Ten, and (3) Overall Combined Ranking for all 20 stocks. The combined ranking places stocks least likely to break the practical stop zone at the top and most likely at the bottom. Reviewed and pending stocks are clearly distinguished.

## Technical Dossier Directory

`technical-dossiers/` contains one crisp markdown dossier for each of the 15 technically reviewed stocks. Filenames are `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank. Each dossier covers: core price levels, 5 timeframe notes (weekly/daily/60/30/15), support and resistance inventories, trade parameters, verdict, and summary rationale. These are audit records only and are not reused as cache inputs.
