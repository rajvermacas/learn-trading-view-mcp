# Swing Trading Analysis — 2026-04-27

**Run Date:** 2026-04-27
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
**Screen Thesis:** Mid/large-cap stocks (Market Cap > 3000 Cr) with 3-month return > 30% — screening for momentum-backed names with credible fundamental sponsorship and defendable 2–4% stop zones for 1–8 week swing trades.

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed Universe Size | 151 stocks |
| User-Specified Pre-Rank Cap | 20 |
| Working Universe (after pre-rank) | 20 |
| Fundamentally Analyzed | 20 (all cached fresh) |
| Selected for Technical Review | 15 (user-specified) |
| Technically Reviewed | 15 |
| Technical Dossiers Written | 15 |
| Selected | 3 |
| Watchlist | 12 |
| Rejected | 0 |
| Pending Technical Review | 5 (ranks 16–20) |

**Coverage Mode:** Top 15 of 20 fundamentally ranked stocks for technical review
**Technical Data Mode:** api_fallback (TradingView MCP disconnected)

## Top 5 Fundamentally Strongest

1. **GVT&D** — Strongly Sponsored (High) — cleanest evidence quality across all dimensions
2. **ORIANA** — Strongly Sponsored (High) — extraordinary operating delivery, govt offtake confirmed
3. **ACUTAAS** — Sponsored (High) — highest-quality CDMO earnings, contract-backed
4. **LLOYDSME** — Strongly Sponsored (Medium-High) — broad multi-factor sponsorship
5. **QPOWER** — Strongly Sponsored (Medium-High) — best blend of growth/ROCE/momentum

## Top 5 Technically Strongest (Among Reviewed)

1. **QPOWER** — Best Aligned — 30m 50-EMA + intraday lows confluence in stop zone
2. **GVT&D** — Near-Valid (Selected) — 3.1x volume ATH breakout, thin but anchored stop
3. **SKYGOLD** — Near-Valid (Selected) — structural support at 396–400, healthy consolidation
4. **ORIANA** — Near-Valid (Watchlist) — weekly 50 EMA cluster, needs 2100 clearance
5. **ACUTAAS** — Near-Valid (Watchlist) — perfect 30m EMA ribbon but ATR concern

## Top 5 Overall Combined

1. **QPOWER** — F#5 + Best Aligned stop = strongest combined entry
2. **GVT&D** — F#1 + Selected (Near-Valid) = best fundamental + technical breakout
3. **SKYGOLD** — F#14 + Selected (Near-Valid) = healthy pullback consolidation with structural stop
4. **ORIANA** — F#2 + Near-Valid Watchlist = elite fundamentals, needs entry trigger
5. **ACUTAAS** — F#3 + Near-Valid Watchlist = exceptional earnings, wait for pullback

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship evidence quality
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names
3. **Overall Combined Ranking** — the master ranking with technical review status explicit

The combined ranking places technically reviewed and confirmed names above pending names at similar fundamental quality. Reviewed names that are "Likely To Break" are ranked below pending names with stronger fundamentals.

## Technical Dossier Directory

`technical-dossiers/` contains one markdown file per technically reviewed stock (15 files). Each dossier includes core fields, 5-timeframe notes, support/resistance inventories, trade parameters, and verdict with summary rationale. Filename format: `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank left-padded to 2 digits.

## Pre-Rank Step

The full 151-stock universe was reduced to 20 using `PreRankScore`:
- `PreRankScore = 0.35 × rank(Qtr Profit Var%) + 0.35 × rank(Qtr Sales Var%) + 0.20 × rank(ROCE%) + 0.10 × rank(3mth return%)`
- Soft penalties: QPV ≤ 0 (−12), QSV ≤ 0 (−12), ROCE < 15 (−8), ROCE < 0 (−12 + zero contribution), 3mth return ≤ 0 (−8)
- All 20 selected stocks had zero penalties, reflecting strong operating metrics across the board
