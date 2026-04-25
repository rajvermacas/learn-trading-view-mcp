# Swing Trading Screen — 2026-04-25

## Run Details

- **Run Date**: 2026-04-25
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Thesis**: Momentum screen seeking stocks with 3-month return > 30% AND market cap > 3000 Cr — surfaces mid-to-large cap names with recent price strength, then tests whether that strength is backed by credible fundamental sponsorship and defendable stop-loss geometry
- **Technical Data Mode**: api_fallback (TradingView MCP disconnected)

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe size | 125 stocks |
| Pre-rank cap (user-specified) | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 (all cached fresh) |
| Technical coverage requested | Top 15 |
| Technically reviewed | 15 |
| Technical dossiers written | 15 |
| Selected (tradeable) | 0 (all Near-Valid or Likely To Break at CMP) |
| Watchlist (Near-Valid, pullback entry) | 13 |
| Rejected (Likely To Break) | 2 |
| Pending technical review | 5 |

## Pre-Rank Step

PreRankScore computed from 4 scoring columns (`Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, `3mth return %`) using percentile ranking with weights 0.35/0.35/0.20/0.10. Soft penalties applied for negative growth, low ROCE (<15%), and negative momentum. The top 20 by adjusted PreRankScore form the working universe. All 20 had zero penalties — strong operating metrics across the board.

## Top 5 Fundamentally Strongest

1. **GVT&D** — Strongly Sponsored (order book, 58% YoY revenue, zero debt)
2. **LLOYDSME** — Strongly Sponsored (120% iron ore production growth, OPM 33%)
3. **SHARDACROP** — Strongly Sponsored (3 recovery quarters, zero debt, Rs 826 Cr cash)
4. **ACUTAAS** — Strongly Sponsored (NP +140% YoY, margin transformation 25%→38%)
5. **ATLANTAELE** — Strongly Sponsored (ROCE 50%, 6-quarter margin expansion)

## Top 5 Technically Strongest (Among Reviewed)

1. **SHARDACROP** — Near-Valid, tight 1080–1087 stop with 3.6:1 R:R; demand cluster at 1086–1092
2. **SKYGOLD** — Near-Valid, 400–403 stop with 1:3 R:R to ATH 440; flag consolidation
3. **PRECWIRE** — Near-Valid, 377–380 stop backed by S/R flip + 60m 50-EMA; 2.5:1 R:R
4. **ACUTAAS** — Near-Valid, 2310–2325 stop at Apr 17 low + VWMA; post-crash recovery orderly
5. **CUPID** — Near-Valid, 108.57–109.70 stop above Apr 23 wick low; tight bull flag

## Top 5 Overall Combined

1. **SHARDACROP** — Strongly Sponsored + Near-Valid (best stop geometry among top-ranked names)
2. **ACUTAAS** — Strongly Sponsored + Near-Valid (earnings inflection + orderly recovery)
3. **GVT&D** — Strongly Sponsored + Near-Valid (elite fundamentals but fragile stop at CMP)
4. **LLOYDSME** — Strongly Sponsored + Near-Valid (volume inflection but double-top at 1701)
5. **GROWW** — Strongly Sponsored + Near-Valid (122% profit surge + valid stop structure)

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality alone
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names only
3. **Overall Combined Ranking** — master ranking combining fundamental sponsorship + technical stop-survivability; reviewed and pending names are clearly distinguished

## Technical Dossiers

15 dossiers written to `technical-dossiers/`. Each file is named `<RANK>-<SYMBOL>.md` where RANK is the stock's fundamental rank (left-padded to 2 digits). Read each dossier for the full multi-timeframe technical verdict, support/resistance inventory, trade parameters, and summary rationale.
