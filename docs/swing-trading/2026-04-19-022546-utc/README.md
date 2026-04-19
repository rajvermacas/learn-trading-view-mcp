# Swing Trading 3% Screen Run — 2026-04-19 UTC

## Run metadata

- **Run timestamp**: 2026-04-19 02:25:46 UTC
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months/?page=1
- **Coverage mode**: Page 1 only (25 stocks) per explicit user directive; pages 2, 3, 4 intentionally not fetched
- **Technical coverage limit**: Top 5 fundamentally ranked names only (user directive)
- **Main agent model**: Opus 4.7
- **Sub-agent model**: Sonnet (both fundamental and technical)

## Screen thesis (extracted this run)

`Return over 3 months > 30% AND Market Capitalization > ₹3,000 Cr` — surface Indian equities that have advanced more than 30% in the preceding 90 days while maintaining a market cap above ₹3,000 Cr. The intent is **price momentum credibly backed by business evidence**. The thesis was extracted from the screen title + visible filter clause at fetch time; it was not hardcoded.

## Universe size

- 25 stocks parsed from page 1 (total results reported by Screener: 89 across 4 pages — pages 2/3/4 not within scope)
- All 25 mapped 1-to-1 to cached dossiers; no duplicates detected
- Cache freshness derivation: all 25 were classified `fresh` (next review on 2026-04-27 or 2026-04-28 ≥ today 2026-04-19), so **zero fundamental refresh workers** were dispatched; ranking was built entirely from cached dossiers

## Counts

| Bucket | Count |
|---|---|
| Fundamentally analyzed (cache-read or fresh-refresh) | 25 |
| Technically reviewed this run | 5 |
| Selected | 0 |
| Watchlist | 5 |
| Hard rejected | 0 |
| Pending technical review (coverage-limit exclusions) | 20 |

## Top-5 preview — fundamentally strongest

| # | Symbol | Sponsorship | Confidence | Headline |
|---|---|---|---|---|
| 1 | SHILCTECH | Strongly Sponsored | High | Zero debt + 28–33% OPM 7 qtrs + FY26 pipeline ₹750–800 Cr > FY25 revenue; P/E ~29x is the cleanest in the tier |
| 2 | PREMIERENE | Strongly Sponsored | High | 8+ qtrs OPM expansion (12%→33%); ~100% cell export share; three catalysts in 20 days (TOPCon + Transcon + ₹2,577 Cr order) |
| 3 | GVT&D | Strongly Sponsored | High | 6+ qtrs acceleration; OPM 12%→27%; zero net debt, ₹1,590 Cr cash; ₹14,380 Cr order backlog; Adani + Chandrapur HVDC wins |
| 4 | LLOYDSME | Strongly Sponsored | High | SEBI-filed 120% YoY iron ore production step-change; OPM 33% held 4 qtrs; TTM PAT ₹2,331 Cr; P/E ~25x (best value in tier) |
| 5 | ATLANTAELE | Strongly Sponsored | High | PGCIL 400 kV EHV approval; OPM 14%→20% over 6 qtrs; ROE 41%, ROCE 50% |

## Top-5 preview — technically strongest (reviewed names only)

All five printed **Near-Valid / Marginal — Needs Pullback**. None printed Best Aligned. Ordering is by relative stop-defendability within the reviewed set.

| # | Symbol | Technical Verdict | Stop Survivability |
|---|---|---|---|
| 1 | ATLANTAELE | Near-Valid | Marginal — only top-5 chart with a tested demand shelf (₹1,322–₹1,341) inside the 2–4% stop band |
| 2 | LLOYDSME | Near-Valid | Marginal — single-session 30m shelf at ₹1,556–₹1,568 inside band |
| 3 | GVT&D | Near-Valid | Marginal — 2% air pocket between ₹4,057 and ₹3,978 inside band |
| 4 | PREMIERENE | Near-Valid | Marginal — fresh breakout bar with no retest; ₹993–₹1,003 is 60m air pocket |
| 5 | SHILCTECH | Near-Valid | Marginal — 60m/30m EMAs above price; daily red rejection candle today |

## Top-5 preview — overall combined

Ordering after combining sponsorship (senior) with stop-defendability (junior where applied):

| # | Symbol | Reason |
|---|---|---|
| 1 | ATLANTAELE | Strong fundamentals + the only chart of the five with structural support inside the 2–4% stop band |
| 2 | LLOYDSME | Best value in the strong-sponsorship tier (P/E ~25x) + legitimate volume-confirmed breakout today |
| 3 | SHILCTECH | Cleanest absolute balance sheet and P/E, but parabolic 2-week sprint with no base — needs pullback |
| 4 | GVT&D | Elite business quality, but +21% in 14 sessions and a 2% stop-zone air pocket |
| 5 | PREMIERENE | Multiple stacked fresh catalysts, but breakout bar is unretested; ₹1,005–₹1,015 pullback required |

## How to read the fifth file (`3pct-ranked-by-stop-safety.md`)

That file has three sections:

1. **Fundamentally Strongest Top Ten** — pure sponsorship ranking from cached dossiers. Not filtered by technical status.
2. **Technically Strongest Top Ten (Reviewed Names Only)** — only the 5 names charted this run, ordered by stop-defendability. There is no top-ten set for technicals because coverage was capped at 5.
3. **Overall Combined Ranking** — the default master view covering every stock in the page-1 universe. The top row is the stock least likely to break the practical 2–4% stop zone after combining fundamental sponsorship and (where run) stop-defendability. Every row carries an explicit technical review status — `technically reviewed` vs `technical review not run in this execution`. Pending names are not hard rejects; they are excluded by the coverage limit and remain eligible for a future run.

## Files in this run

- [`README.md`](README.md) — this file
- [`screen-universe.md`](screen-universe.md) — raw normalized universe + cache freshness note
- [`3pct-selected-and-watchlist.md`](3pct-selected-and-watchlist.md) — full trade-level writeups for 5 watchlist names (0 selected)
- [`3pct-rejected.md`](3pct-rejected.md) — 0 hard rejects + 20 names labeled `technical review not run in this execution` + 3 Mixed-sponsorship watchouts
- [`3pct-ranked-by-stop-safety.md`](3pct-ranked-by-stop-safety.md) — 3-section master ranking (fundamental top-10, technical reviewed, overall combined)

## Verdict summary in one line

No current-price selection this run — every top-5 name is vertically extended and needs a pullback before the 2–4% stop is structurally defendable. Each watchlist entry has a specific retest-entry trigger and hard stop defined in `3pct-selected-and-watchlist.md`.
