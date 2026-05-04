# Swing Trading Analysis — 2026-05-04

## Run Details

- **Run Date:** 2026-05-04
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Title:** Return over 3 months
- **Filters:** Return over 3 months > 30% AND Market Capitalization > 3000 Cr

## Screen Thesis

Surface mid-to-large cap Indian stocks showing strong 3-month price momentum (>30%) backed by recent operating improvement. The screen targets quarterly profit growth, sales growth, and ROCE as evidence of business sponsorship behind price moves. Stocks are ranked by fundamental sponsorship strength first, then assessed for technical stop-survivability within a practical 2%-4% downside zone.

## Universe Summary

| Metric | Count |
|--------|-------|
| Full parsed universe | 95 stocks |
| Pre-rank cap (user-specified) | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 |
| Technically reviewed | 15 |
| Pending technical review | 5 (ranks 16-20) |
| Technical dossiers written | 15 |

## Coverage Mode

- Pre-rank: top 20 by PreRankScore (percentile-weighted QPV/QSV/ROCE/3M with soft penalties)
- Fundamental: all 20 stocks analyzed (4 refreshed, 16 cached)
- Technical: top 15 fundamentally ranked stocks reviewed
- Technical data mode: **api_fallback** (TradingView MCP disconnected)

## Fundamental Refresh

- **Missing (new):** DEEDEV (1)
- **Refreshed (review_due top 3):** POWERINDIA, CUPID, EMMVEE (3)
- **Reused (fresh):** 13 stocks
- **Reused (remaining review_due):** WEBELSOLAR, UTLSOLAR, DIACABS (3)

## Top 5 Fundamentally Strongest

1. **ENGINERSIN** — Strongly Sponsored (High) — P/E 18x, ROCE 25%, ₹1,400 Cr net cash
2. **EMMVEE** — Strongly Sponsored (High) — P/E 17x, ROCE 44.8%, Q4 confirmed
3. **LLOYDSME** — Strongly Sponsored (Medium-High) — Highest-ever results, pellet ramp
4. **QPOWER** — Strongly Sponsored (Medium-High) — Record Q3, HVDC orders
5. **ATLANTAELE** — Strongly Sponsored (Medium-High) — PGCIL 400kV, ROCE 50%

## Top 5 Technically Strongest (Reviewed)

1. **LLOYDSME** — Defensible (Moderate-High) — 3-session demand zone at 3% floor
2. **SKYGOLD** — Conditional Buy (Adequate) — Gap-open structural stop at 3%
3. **ENGINERSIN** — Survivable Conditional (Moderate) — Dual-stop (2% demand / 4% base)
4. **CPPLUS** — Conditional Pass (Moderate-Strong) — Daily 10-EMA at stop level
5. **EMMVEE** — Conditional Pass (Survivable) — Apr 16 low anchors stop zone

## Top 5 Overall Combined

1. **ENGINERSIN** — #1 fundamental, #3 technical — best risk-adjusted entry
2. **EMMVEE** — #2 fundamental, #5 technical — best value in solar
3. **LLOYDSME** — #3 fundamental, #1 technical — strongest technical setup
4. **ACUTAAS** — #6 fundamental, survivable stop on breakout base — CDMO contract-backed
5. **SKYGOLD** — #11 fundamental, #2 technical — best stop structure in universe

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names only
3. **Overall Combined Ranking** — master ranking combining both, with technical review status explicit

## Technical Dossier Directory

`technical-dossiers/` contains 15 crisp markdown dossiers, one per technically reviewed stock. Filenames use `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank. Each dossier covers core fields, 5-timeframe notes, support/resistance inventories, trade parameters, verdict, and summary rationale.

## Pre-Rank Methodology

PreRankScore uses percentile ranks within the 95-stock universe across 4 scoring columns:
- Qtr Profit Var % (weight 0.35)
- Qtr Sales Var % (weight 0.35)
- ROCE % (weight 0.20)
- 3mth return % (weight 0.10)

Soft penalties: QPV<=0 (-12), QSV<=0 (-12), ROCE<15 (-8), 3M<=0 (-8), ROCE<0 (contribution zeroed + -12 extra).
