# Swing Trading 3% Screen — 2026-04-26

## Run Details

| Field | Value |
|---|---|
| Run date | 2026-04-26 |
| Screen URL | https://www.screener.in/screens/3474384/return-over-3-months |
| Screen thesis | Momentum stocks with >30% 3-month return AND >₹3,000 Cr market cap, filtered for Mar 2026 quarterly results — surfaces stocks where recent price strength is backed by identifiable operating evidence |
| Parsed universe size | 125 stocks (5 pages) |
| User-specified pre-rank cap | 20 |
| Working universe after pre-rank | 20 |
| Coverage mode | Top 15 technically reviewed |
| Technical data mode | tradingview_mcp |

## Counts

| Category | Count |
|---|---|
| Fundamentally analyzed (from cache) | 20 |
| Technically reviewed | 15 |
| Pending technical review | 5 |
| Selected (Best Aligned) | 5 |
| Watchlist (Near-Valid) | 6 |
| Rejected (Likely To Break) | 4 |
| Technical dossiers written | 15 |

## Top 5 Fundamentally Strongest

1. **LLOYDSME** — Strongly Sponsored (High) — 120% iron ore volume inflection, 33% OPM sustained
2. **ATLANTAELE** — Strongly Sponsored (High) — EHV approval, 50% ROCE, margin expansion
3. **GVT&D** — Strongly Sponsored (High) — 58% revenue growth, zero debt, ₹14,380 Cr order book
4. **SHARDACROP** — Strong (High) — 366% PAT recovery, zero debt, ₹826 Cr cash
5. **ACUTAAS** — Sponsored (High) — 140% NP growth, 38% OPM, Fermion/Bayer contracts

## Top 5 Technically Strongest (Among Reviewed)

1. **LLOYDSME** — Best Aligned — four-layer support confluence in stop band
2. **SHARDACROP** — Best Aligned — three-tier support, 3% floor tested and recovered
3. **RUBICON** — Best Aligned — four support layers, healthy consolidation near ATH
4. **CUPID** — Best Aligned — prior day low anchors stop, EMA convergence
5. **ATLANTAELE** — Best Aligned — dense 3-layer cluster in band despite parabolic extension

## Top 5 Overall Combined

1. **LLOYDSME** — #1 fundamental, Best Aligned technical — strongest combined setup
2. **SHARDACROP** — #4 fundamental, Best Aligned technical — best risk-reward balance
3. **ATLANTAELE** — #2 fundamental, Best Aligned technical — elite fundamentals, parabolic risk noted
4. **RUBICON** — #14 fundamental, Best Aligned technical — strongest chart structure
5. **CUPID** — #9 fundamental, Best Aligned technical — clean setup with moderate fundamentals

## How To Read `3pct-ranked-by-stop-safety.md`

The fifth file contains three ranking views. The first two sections show the top ten in fundamental and technical rankings respectively. The third section is the **Overall Combined Ranking** — the master ranking for the full 20-stock universe. Reviewed names show a technical verdict; pending names are explicitly marked. The top row is the stock least likely to break a practical 3% stop; the bottom row is most likely.

## Technical Dossier Directory

`technical-dossiers/` contains one markdown file per technically reviewed stock, named `<RANK>-<SYMBOL>.md`. Each dossier is a concise audit record with core fields, five timeframe notes, support/resistance inventories, trade parameters, and a verdict. They are user-facing records only and are not reused as cache inputs.

## Pre-Rank Methodology

The full 125-stock universe was scored using `PreRankScore = 0.35 × rank(Qtr Profit Var%) + 0.35 × rank(Qtr Sales Var%) + 0.20 × rank(ROCE%) + 0.10 × rank(3mth return%)`. Soft penalties were applied: −12 for negative QPV or QSV, −8 for ROCE<15%, −8 for negative 3-month return, −12 for negative ROCE (with ROCE contribution zeroed). Top 20 by adjusted score formed the working universe.
