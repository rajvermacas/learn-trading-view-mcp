# Swing Trading Analysis — 2026-04-29

**Run Date:** 2026-04-29
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months

## Screen Thesis

- **Title:** Return over 3 months
- **Filters:** Return over 3months > 30 AND Market Capitalization > 3000
- **Intent:** Momentum screen seeking stocks with strong 3-month returns (>30%) among mid-to-large caps (>₹3,000 Cr market cap)
- **Sponsorship sought:** Stocks where recent price momentum is backed by operating improvement, earnings acceleration, and identifiable catalysts

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe (full HTML, 6 pages) | 132 |
| User-specified pre-rank cap | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed (fresh + cached) | 20 |
| Technically reviewed | 15 |
| Selected (trade-ready with entry plans) | 8 |
| Watchlist (near-valid, need pullback/confirmation) | 5 |
| Rejected (technically reviewed) | 2 |
| Pending technical review (user coverage limit) | 5 |
| Technical dossiers written | 15 |

## Coverage Mode

- **Fundamental:** Full 20-stock working universe analyzed
- **Technical:** Top 15 fundamentally ranked stocks reviewed (user requested top 15)
- **Technical data mode:** `api_fallback` (TradingView MCP disconnected)

## Top 5 Fundamentally Strongest

| Rank | Symbol | Sponsorship | Key Metric |
|------|--------|-------------|------------|
| 1 | ENGINERSIN | Strongly Sponsored | 18x P/E, ₹1,400 Cr net-cash, 25% ROCE |
| 2 | GVT&D | Strongly Sponsored | 54.74% ROCE, debt-free, 138% profit growth |
| 3 | ORIANA | Strongly Sponsored | 149% profit growth, SECI 10-yr ₹3,135 Cr |
| 4 | LLOYDSME | Strongly Sponsored | 169% profit growth, 202% sales growth |
| 5 | QPOWER | Strongly Sponsored | 169% profit growth, 291% sales growth |

## Top 5 Technically Strongest (among reviewed)

| Rank | Symbol | Verdict | R:R Highlight |
|------|--------|---------|---------------|
| 1 | ENGINERSIN | Near-Valid | Entry 252-255, target 278-285 |
| 2 | GVT&D | Near-Valid | Entry 4500-4545, target 4737-4750 |
| 3 | CUPID | Near-Valid | Entry 111-112, target 118-120 (3.5:1 R:R) |
| 4 | ORIANA | Near-Valid | Entry 2140-2165, target 2320-2340 |
| 5 | NETWEB | Near-Valid | Entry 3990-4020, target 4350-4400 |

## Top 5 Overall Combined

| Rank | Symbol | Fund Rank | Tech Verdict | Combined Reason |
|------|--------|-----------|-------------|-----------------|
| 1 | ENGINERSIN | #1 | Near-Valid | Best valuation + cleanest breakout |
| 2 | GVT&D | #2 | Near-Valid | Highest ROCE + textbook breakout |
| 3 | ORIANA | #3 | Near-Valid | SECI contract + V-recovery |
| 4 | LLOYDSME | #4 | Near-Valid | Multi-track acceleration + ascending demand |
| 5 | ATLANTAELE | #6 | Near-Valid | PGCIL catalyst + constructive recovery |

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality
2. **Technically Strongest Top Ten** — among reviewed names, ranked by stop survivability
3. **Overall Combined Ranking** — all 20 stocks, with technical review status explicit; top row is the stock least likely to break the 2-4% stop zone

## Technical Dossier Directory

`technical-dossiers/` contains 15 markdown files, one per technically reviewed stock. Each file includes core metrics, 5-timeframe analysis, support/resistance inventory, trade parameters, and verdict. Filename format: `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank.

## Pre-Rank Step

The 132-stock parsed universe was reduced to 20 using `PreRankScore`:
- Weighted percentile ranks of 4 scoring columns: Qtr Profit Var % (0.35), Qtr Sales Var % (0.35), ROCE % (0.20), 3mth return % (0.10)
- Soft penalties: QPV ≤ 0 (−12), QSV ≤ 0 (−12), ROCE < 15 (−8), 3m return ≤ 0 (−8), ROCE < 0 (contribution 0 + −12)
- Sorted descending, top 20 kept as working universe
