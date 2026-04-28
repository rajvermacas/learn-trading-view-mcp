# Swing Trading Analysis — 2026-04-28

## Run Summary

- **Run Date**: 2026-04-28
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Thesis**: Momentum stocks with >30% 3-month return and >3000 Cr market cap. The screen surfaces stocks where recent price momentum is potentially backed by credible business evidence — quarterly profit/sales acceleration, high ROCE, and visible operating catalysts.
- **Parsed Universe Size**: 129 stocks
- **User-Specified Pre-Rank Cap**: 20
- **Working Universe After Pre-Rank**: 20
- **Coverage Mode**: Top 15 of 20 fundamentally ranked stocks technically reviewed

## Counts

| Category | Count |
|----------|-------|
| Fundamentally analyzed (cached fresh) | 20 |
| Technically reviewed | 15 |
| Selected (tradeable with stop discipline) | 4 |
| Watchlist (conditional / pullback entry) | 6 |
| Rejected (stop not survivable) | 5 |
| Pending technical review | 5 |
| Technical dossiers written | 15 |

## Top 5 Fundamentally Strongest

1. **GVT&D** — Strongly Sponsored (High confidence), ROCE 54.74%, clean balance sheet, order visibility
2. **ORIANA** — Strongly Sponsored (High confidence), ROCE 42.31%, SECI green ammonia deal Rs 3135 Cr
3. **QPOWER** — Strongly Sponsored (Med-High), record Q3 FY26, ROCE 26.6%, strong order flow
4. **ATLANTAELE** — Strongly Sponsored (Med-High), 400kV PGCIL approval, revenue +80% YoY
5. **LLOYDSME** — Strongly Sponsored (Med-High), highest-ever Q3, ROCE 38.28%

## Top 5 Technically Strongest (Among Reviewed)

1. **EMMVEE** — Medium-High survivability, dense EMA support nest at 3% floor, constructive trend
2. **GVT&D** — Near-Valid, double-bottom at 4524 validated, 2.6x volume breakout
3. **SHARDACROP** — Marginal-Defensible, multi-test demand band backs 3% floor, cup-and-handle
4. **CUPID** — Moderate, 109-110 demand zone aligns with 3% floor, Boll squeeze
5. **ENGINERSIN** — Thin but structural support at 250.4, volume-confirmed breakout

## Top 5 Overall Combined

1. **GVT&D** — Fund #1, Tech Near-Valid: strongest combined profile
2. **EMMVEE** — Fund #13, Tech Medium-High: best stop defense despite lower fund rank
3. **SHARDACROP** — Fund #7, Tech Marginal-Defensible: solid structure + catalyst turnaround
4. **CUPID** — Fund #11, Tech Moderate: niche play with defensible stop
5. **QPOWER** — Fund #3, Tech Borderline: excellent fundamentals, close-based stop viable

## How to Read the Ranking File

`3pct-ranked-by-stop-safety.md` contains three sections: Fundamentally Strongest Top Ten, Technically Strongest Top Ten, and the Overall Combined Ranking. The combined ranking places stocks least likely to break the stop zone at the top and most likely to break through at the bottom. Technical review status is explicit for each name.

## Technical Dossier Directory

`technical-dossiers/` contains one markdown file per reviewed stock (15 files). Each dossier shows the multi-timeframe analysis, support/resistance inventory, trade parameters, and verdict. Filenames use the format `<RANK>-<SYMBOL>.md` where rank is the fundamental rank.

## Pre-Rank Step

The full 129-stock universe was pre-ranked using `PreRankScore = 0.35 * rank(QPV%) + 0.35 * rank(QSV%) + 0.20 * rank(ROCE%) + 0.10 * rank(3M%)`. Soft penalties were applied: −12 for QPV≤0, −12 for QSV≤0, −8 for ROCE<15, −12 for ROCE<0, −8 for 3M≤0. Only the top 20 by adjusted PreRankScore were kept as the working universe.

## Technical Data Mode

All 15 stocks were reviewed using `api_fallback` mode (TradingView MCP was disconnected).
