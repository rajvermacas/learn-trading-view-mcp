# Swing Trading 3% Screen — 2026-04-21

## Run Details

- **Run Date**: 2026-04-21
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Thesis**: Surface mid/large cap stocks (>₹3,000 Cr market cap) showing strong 3-month price momentum (>30% return), implying recent business catalysts or fundamental improvement. Screen filters: `Return over 3months > 30 AND Market Capitalization > 3000`.
- **Parsed Universe Size**: 110 stocks across 5 pages
- **User-Specified Pre-Rank Cap**: 15
- **Working Universe Size**: 15 (after PreRank)
- **Coverage Mode**: Top 10 fundamentally ranked stocks for technical analysis

## Counts

| Category | Count |
|----------|-------|
| Fundamentally analyzed | 15 |
| Technically reviewed | 10 |
| Selected (Best Aligned) | 2 |
| Watchlist (Near-Valid) | 5 |
| Rejected (Likely To Break) | 3 |
| Pending technical review (ranks 11-15) | 5 |
| Technical dossiers written | 10 |

## Top 5 Fundamentally Strongest

1. **BSE** — Strongly Sponsored (High) — zero debt, 174% profit growth, EBITDA margin 31%→59%
2. **LLOYDSME** — Strongly Sponsored (High) — 120% iron ore volume inflection, OPM 33% x4 quarters
3. **GVT&D** — Strongly Sponsored (High) — OPM 12%→27%, ₹14,380 Cr order book, zero debt
4. **ACUTAAS** — Strongly Sponsored (High) — NP +140%, OPM 25%→38%, Fermion/Bayer 10-year contract
5. **ATLANTAELE** — Strongly Sponsored (High) — PGCIL EHV approval, ROCE 50%

## Top 5 Technically Strongest (Among Reviewed)

1. **GVT&D** — Best Aligned — 6+ support references across stop band including daily swing low + EMA confluence
2. **ACUTAAS** — Best Aligned — 13 support references between CMP and stop zone floor, Daily EMA10 inside stop zone
3. **BSE** — Near-Valid — support cluster at 3,340-3,365 but ATH rejection and 3% air gap from CMP
4. **LLOYDSME** — Near-Valid — EMA-based support in stop zone but no structural confirmation
5. **SAATVIKGL** — Near-Valid — Daily EMA10 + April 14 swing low confluence at 447

## Top 5 Overall Combined

1. **GVT&D** — Fundamental #3 + Technical #1 = strongest combined — HVDC order book + best stop-zone defense
2. **ACUTAAS** — Fundamental #4 + Technical #2 = dense EMA support + patent-protected CDMO
3. **BSE** — Fundamental #1 + Technical #3 = top fundamentals, needs pullback for entry
4. **LLOYDSME** — Fundamental #2 + Technical #4 = iron ore inflection, needs pullback for entry
5. **ATLANTAELE** — Fundamental #5 + Technical #5 = EHV catalyst, needs 1,362 retest to confirm demand

## How to Read the Report Files

- **3pct-selected-and-watchlist.md**: Full trade-level writeups for the 2 selected and 5 watchlist stocks
- **3pct-rejected.md**: Compact rejection summaries with reasons and re-check status
- **screen-universe.md**: Full 110-stock parsed universe with PreRankScore, penalties, and working-universe inclusion
- **3pct-ranked-by-stop-safety.md**: Three ranking sections — Fundamental Top 10, Technical Top 10, and Overall Combined for all 15 working-universe stocks

## Technical Dossier Directory

`technical-dossiers/` contains 10 verbose markdown dossiers, one per technically reviewed stock. Each dossier includes: core fields, 5-timeframe notes (weekly/daily/60/30/15), support and resistance inventories, trade parameters, verdict fields, and a summary rationale. Dossier filenames use the stock's fundamental rank: `01-BSE.md` through `10-SAATVIKGL.md`.

## Pre-Rank Methodology

The PreRankScore reduces the 110-stock parsed universe to 15 using percentile ranks on 4 scoring columns: `Qtr Profit Var %` (weight 0.35), `Qtr Sales Var %` (0.35), `ROCE %` (0.20), `3mth return %` (0.10). Soft penalties deduct points for negative growth, low ROCE (<15%), or negative momentum. Context-only columns (CMP, P/E, Market Cap, Div Yield, NP Qtr, Sales Qtr) are preserved for reporting but do not affect the score.
