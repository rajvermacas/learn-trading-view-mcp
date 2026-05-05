# Swing Trading Analysis — 2026-05-05

## Run Details

- **Run Date:** 2026-05-05
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Title:** Return over 3 months
- **Filters:** Return over 3 months > 30% AND Market Capitalization > 3000 Cr

## Screen Thesis

Mid-to-large cap Indian stocks with >30% 3-month price momentum, seeking names where price strength is backed by improving business fundamentals rather than speculative momentum. Stocks are ranked by fundamental sponsorship strength first, then assessed for technical stop-survivability within a practical 2%-4% downside zone.

## Universe Summary

| Metric | Count |
|--------|-------|
| Full parsed universe | 92 stocks |
| Pre-rank cap (user-specified) | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 |
| Technically reviewed | 15 |
| Pending technical review | 5 (ranks 16-20) |
| Technical dossiers written | 10 |

## Coverage Mode

- Pre-rank: top 20 by PreRankScore (percentile-weighted QPV/QSV/ROCE/3M with soft penalties)
- Fundamental: all 20 stocks analyzed (4 refreshed, 16 cached)
- Technical: top 15 fundamentally ranked stocks reviewed
- Technical data mode: **api_fallback** (TradingView MCP disconnected)

## Fundamental Refresh

- **Missing (new):** TIMEX (1)
- **Refreshed (review_due top 3):** KRISHANA, GROWW, UTLSOLAR (3)
- **Reused (fresh/cached):** 16 stocks

## Top 5 Fundamentally Strongest

1. **ENGINERSIN** — Strongly Sponsored — Two consecutive 29% OPM, Rs 1400 Cr net cash, 25% ROCE, 18x P/E
2. **GVT&D** — Strongly Sponsored — 58% revenue growth, 54.7% ROCE, debt-free, strong order book
3. **QPOWER** — Strongly Sponsored — Record Q3, 256% revenue growth, strong order flow
4. **ATLANTAELE** — Strongly Sponsored — 80% revenue growth, PGCIL 400kV approval, record order book
5. **LLOYDSME** — Strongly Sponsored — Highest-ever revenue/EBITDA/PAT, doubled iron ore production

## Top 5 Technically Strongest (Reviewed)

1. **ENGINERSIN** — Best Aligned — only Best Aligned verdict in universe
2. **EBGNG** — Near-Valid — fresh breakout, 3% floor aligns with structural stop at 437
3. **ACUTAAS** — Near-Valid — borderline stop at 3.1%, supply at 2710 ATH
4. **QPOWER** — Near-Valid — corrective pullback, Boll LB confluence at 1295-1305
5. **GVT&D** — Near-Valid — ATR exceeds stop band, air pocket below 4391

## Top 5 Overall Combined

1. **ENGINERSIN** — #1 fundamental, #1 technical — only Best Aligned; best risk-adjusted entry
2. **ACUTAAS** — #7 fundamental, #3 technical — contract-backed CDMO, borderline stop manageable
3. **QPOWER** — #3 fundamental, #4 technical — record Q3, corrective pullback offers entry
4. **EBGNG** — #9 fundamental, #2 technical — PAT doubling, fresh breakout with structural stop
5. **GVT&D** — #2 fundamental, #5 technical — elite franchise, ATR risk manageable with sizing

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names only
3. **Overall Combined Ranking** — master ranking combining both, with technical review status explicit

## Technical Dossier Directory

`technical-dossiers/` contains markdown dossiers for technically reviewed stocks. Filenames use `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank. Each dossier covers core fields, 5-timeframe notes, support/resistance inventories, trade parameters, verdict, and summary rationale. 10 of 15 reviewed stocks have dossiers written; 5 were reviewed from cached/API data without separate dossier files.

## Pre-Rank Methodology

PreRankScore uses percentile ranks within the 92-stock universe across 4 scoring columns:
- Qtr Profit Var % (weight 0.35)
- Qtr Sales Var % (weight 0.35)
- ROCE % (weight 0.20)
- 3mth return % (weight 0.10)

Soft penalties: QPV<=0 (-12), QSV<=0 (-12), ROCE<15 (-8), 3M<=0 (-8), ROCE<0 (contribution zeroed + -12 extra).
