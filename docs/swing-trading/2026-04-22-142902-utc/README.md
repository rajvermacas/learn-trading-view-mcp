# Swing Trading 3% Screen — Run Report

**Run Date**: 2026-04-22
**Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
**Screen Thesis**: Momentum screen — stocks with >30% 3-month return AND market cap >₹3,000 Cr. Surfaces companies where recent price momentum is backed by business evidence, not just sector drift.

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe (all pages) | 115 stocks |
| User-specified pre-rank cap | 20 |
| Working universe (post pre-rank) | 20 |
| Fundamentally analyzed | 20 (all cached fresh) |
| Technical coverage requested | Top 15 |
| Technically reviewed | 15 |
| **Selected (Buy)** | **2** |
| **Watchlist (Near-Valid)** | **5** |
| **Rejected (Likely To Break)** | **8** |
| Pending technical review | 5 (ranks 16–20) |
| Technical dossiers written | 15 |

## Coverage Mode

Coverage-limited: top 15 of 20 fundamentally ranked stocks received technical review. Stocks ranked 16–20 (CUPID, SKYGOLD, ENGINERSIN, KRN, KRISHANA) did not receive technical review due to user-imposed limit.

## Top 5 Fundamentally Strongest

1. **SHARDACROP** — Strong, High confidence (zero debt, ₹826 Cr cash, P/E 17.7x, CFO/OP 103%)
2. **LLOYDSME** — Strongly Sponsored, High (120% volume inflection, 33% OPM, SEBI-filed)
3. **GVT&D** — Strongly Sponsored, High (₹14,380 Cr backlog, zero debt, 27% OPM)
4. **ATLANTAELE** — Strongly Sponsored, High (PGCIL EHV approval, ROCE 50%)
5. **GROWW** — Strongly Sponsored, Medium-High (122% profit surge, BofA Buy)

## Top 5 Technically Strongest (Among Reviewed)

1. **SHARDACROP** — Best Aligned (14 support references in 0-4% band, least extended)
2. **ACUTAAS** — Best Aligned (14 support references, cup-and-handle, 2.8R to ATH)
3. **LLOYDSME** — Near-Valid (powerful trend, needs pullback to 1620-1640)
4. **GVT&D** — Near-Valid (tight consolidation below ATH, triple-confluence at 4134-4149)
5. **ATLANTAELE** — Near-Valid (fresh ATH breakout, needs retest at 1427-1440)

## Top 5 Overall Combined

1. **SHARDACROP** — #1 fundamental + Best Aligned technical = highest conviction
2. **ACUTAAS** — #7 fundamental + Best Aligned technical = best risk-reward to ATH
3. **LLOYDSME** — #2 fundamental + Near-Valid = watchlist for pullback entry
4. **GVT&D** — #3 fundamental + Near-Valid = watchlist for ATH breakout or pullback
5. **ATLANTAELE** — #4 fundamental + Near-Valid = watchlist for retest entry

## How To Read The Report Files

- **3pct-selected-and-watchlist.md** — Full trade-level writeups for Selected and Watchlist names only
- **3pct-rejected.md** — Compact rejection summaries with re-check eligibility
- **screen-universe.md** — Full 115-stock universe with PreRankScore and working-universe status
- **3pct-ranked-by-stop-safety.md** — Three ranking views: fundamental top 10, technical top 10, combined master ranking

## Technical Dossier Directory

`technical-dossiers/` contains one verbose markdown dossier per technically reviewed stock (15 files). Each dossier includes core fields, 5-timeframe notes, support/resistance inventories, trade parameters, verdict fields, and a summary rationale. Filename format: `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank.

## Pre-Rank Methodology

PreRankScore computed from 4 scoring columns (Qtr Profit Var % weight 0.35, Qtr Sales Var % weight 0.35, ROCE % weight 0.20, 3mth return % weight 0.10) using percentile ranking within the 115-stock universe. Soft penalties applied: -12 for negative growth columns, -8 for ROCE <15%, -8 for negative 3-month return. Top 20 by adjusted PreRankScore retained as the working universe.
