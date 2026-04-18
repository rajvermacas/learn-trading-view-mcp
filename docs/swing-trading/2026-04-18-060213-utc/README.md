# Swing Trading 3% Screen — Run Summary

**Date:** 2026-04-18 06:25 UTC  
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months/  
**Screen Criteria:** 3-month return > 30% AND Market Cap > ₹3,000 Cr  
**Universe:** 74 stocks across 3 pages  

---

## Methodology Snapshot

- Fundamental filter: ROCE, quarterly profit growth, quarterly sales growth, P/E
- Technical analysis performed **only on the top 10 fundamentally strongest** (ranked by ROCE)
- 5-timeframe chart analysis per stock: Weekly, Daily, 60-min, 30-min, 15-min
- Stop zone: practical 2%–4% below CMP, centered on `CMP × 0.97`
- Chart study verified: `10 in 1 Different Moving Averages` — MA1=EMA 10, MA2=EMA 20, MA3=EMA 50, MA4=EMA 100, MA5=EMA 200, all on Close
- TradingView MCP sub-agents run sequentially (one stock at a time, shared chart state)

---

## Counts

| Category | Count |
|---|---|
| Universe | 74 |
| Technically analyzed (top 10 by ROCE) | 10 |
| Selected Now | 3 |
| Watchlist / Near-Valid | 7 |
| Rejected (outside top 10 fundamentally) | 64 |

---

## Top-Ranked Preview

| Rank | Symbol | CMP | Stop Zone | Verdict |
|---|---|---|---|---|
| 1 | WAAREEENER | ₹3,485 | ₹3,412–₹3,414 | Selected — tightest stop, best R:R |
| 2 | ATLANTAELE | ₹1,374 | ₹1,322–₹1,372 | Selected — dense EMA support, 2.6:1 R:R |
| 3 | PREMIERENE | ₹1,048 | ₹1,008–₹1,015 | Selected — ATH breakout on 8x volume |
| 4 | NATCOPHARM | ₹1,118 | ₹1,082–₹1,085 | Watchlist — ideal entry on pullback |
| 5 | CGPOWER | ₹774 | ₹767–₹748 | Watchlist — overhead resistance 0.3% away |

---

## How to Read the Ranked File

`3pct-ranked-by-stop-safety.md` has three sections:

1. **Fundamentally Strongest Top Ten** — ordered by ROCE (highest to lowest)
2. **Technically Strongest Top Ten** — ordered by stop zone quality: density of independently-justified supports above the 3% floor, distribution across timeframes, and absence of air pockets
3. **Overall Combined Ranking** — every analyzed stock combined, ranked from least likely to most likely to break the practical stop zone

The top row of the third section is the stock where fundamental quality and technical structure together make a stop violation least probable. The bottom row is the stock most likely to trade through the stop before the swing matures.
