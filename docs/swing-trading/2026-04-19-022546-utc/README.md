# Swing Trading 3% Screen Run — 2026-04-19 UTC

## Run metadata

- **Run timestamp**: 2026-04-19 02:25:46 UTC (technical coverage extended to top 10 later in the same session)
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months/?page=1
- **Coverage mode**: Page 1 only (25 stocks) per explicit user directive; pages 2, 3, 4 intentionally not fetched
- **Technical coverage scope**: Top 10 fundamentally ranked names (originally 5, extended to 10 in a follow-up batch)
- **Main agent model**: Opus 4.7
- **Sub-agent model**: Sonnet (both fundamental and technical)

## Screen thesis (extracted this run)

`Return over 3 months > 30% AND Market Capitalization > ₹3,000 Cr` — surface Indian equities that have advanced more than 30% in the preceding 90 days while maintaining a market cap above ₹3,000 Cr. The intent is **price momentum credibly backed by business evidence**. The thesis was extracted from the screen title + visible filter clause at fetch time; it was not hardcoded.

## Universe size

- 25 stocks parsed from page 1 (total results reported by Screener: 89 across 4 pages — pages 2/3/4 not within scope)
- All 25 mapped 1-to-1 to cached dossiers; no duplicates detected
- Cache freshness: all 25 classified `fresh` on 2026-04-19 → **zero fundamental refresh workers** dispatched this run

## Counts

| Bucket | Count |
|---|---|
| Fundamentally analyzed (cache-read or fresh-refresh) | 25 |
| Technically reviewed this run | 10 |
| Selected | 0 |
| Watchlist (Near-Valid / Marginal — Needs Pullback) | 6 |
| Hard technical rejects (Likely To Break Stop) | 4 |
| Pending technical review (coverage-scope exclusions) | 15 |

## Top-10 preview — fundamentally strongest

| # | Symbol | Sponsorship | Confidence | Headline |
|---|---|---|---|---|
| 1 | SHILCTECH | Strongly Sponsored | High | Zero debt + 28–33% OPM 7 qtrs + FY26 pipeline ₹750–800 Cr > FY25 revenue; P/E ~29x |
| 2 | PREMIERENE | Strongly Sponsored | High | 8+ qtrs OPM expansion; ~100% cell export share; three catalysts in 20 days |
| 3 | GVT&D | Strongly Sponsored | High | 6+ qtrs acceleration; OPM 12%→27%; ₹14,380 Cr order backlog; Adani + Chandrapur HVDC wins |
| 4 | LLOYDSME | Strongly Sponsored | High | SEBI-filed 120% YoY iron ore production step-change; OPM 33% held 4 qtrs; P/E ~25x (best value) |
| 5 | ATLANTAELE | Strongly Sponsored | High | PGCIL 400 kV EHV approval; OPM 14%→20% over 6 qtrs; ROE 41%, ROCE 50% |
| 6 | QPOWER | Strongly Sponsored | Medium | Dec 2025 revenue +289% YoY, PAT +215% YoY on clean P&L; BESS order Mar 27 |
| 7 | BAJAJCON | Moderately Sponsored | High | PAT +49% FY26; NCLT Banjara's approval Apr 13; no imminent earnings binary |
| 8 | SHRIPISTON | Moderately Sponsored | Medium | Grupo Antolin acquisition ₹1,670 Cr closed Jan 8; 21% OPM held 8 qtrs |
| 9 | TDPOWERSYS | Moderately Sponsored | Medium | 7 consecutive qtrs of growth; confirmed US data-center order; new CEO pedigree upgrade |
| 10 | ENRIN | Moderately Sponsored | Medium | OPM 14%→24% in 6 qtrs; ₹16,205 Cr order book (+47%); recovery mostly priced in |

## Top-10 preview — technically reviewed (stop survivability)

| # | Symbol | Technical Verdict | Stop Survivability |
|---|---|---|---|
| 1 | ATLANTAELE | Near-Valid | Marginal — tested demand shelf ₹1,322–₹1,341 inside 2–4% band (only reviewed name with real structural support in-band) |
| 2 | LLOYDSME | Near-Valid | Marginal — single-session 30m shelf at ₹1,556–₹1,568 inside band |
| 3 | TDPOWERSYS | Near-Valid | Marginal — thin 30m shelf at ₹975–₹978; air below ₹983 |
| 4 | GVT&D | Near-Valid | Marginal — 2% air pocket between ₹4,057 and ₹3,978 in the stop band |
| 5 | PREMIERENE | Near-Valid | Marginal — fresh breakout bar with no retest; ₹993–₹1,003 sub-band is 60m air pocket |
| 6 | SHILCTECH | Near-Valid | Marginal — 60m/30m EMAs above price; daily red rejection candle today |
| 7 | QPOWER | Likely To Break | Likely To Break Stop — stop zone is pure air; nearest real support at −6.3% |
| 8 | BAJAJCON | Likely To Break | Likely To Break Stop — stop zone is inside today's single spike candle body |
| 9 | SHRIPISTON | Likely To Break | Likely To Break Stop — 4-day-old +24% weekly breakout at ATH; air pocket in band |
| 10 | ENRIN | Likely To Break | Likely To Break Stop — 8-session recovery spike; first resistance only +0.9% away |

## Top-5 preview — overall combined (master view)

Ordering: sponsorship is the senior dimension, stop-defendability refines order within each sponsorship tier. Full list in `3pct-ranked-by-stop-safety.md`.

| # | Symbol | Reason |
|---|---|---|
| 1 | ATLANTAELE | Strong/High + the only chart with tested structural support inside the 2–4% stop band |
| 2 | LLOYDSME | Strong/High + legitimate volume-confirmed breakout today + best P/E value (~25x) in the tier |
| 3 | SHILCTECH | Strong/High + cleanest absolute balance sheet and P/E, but parabolic 2-week sprint with no base |
| 4 | GVT&D | Strong/High + elite business quality; +21% in 14 sessions and 2% stop-zone air pocket |
| 5 | PREMIERENE | Strong/High + breakout from a real 7-session base, but final 2 intraday bars surged 4.1% with no retest |

## How to read the fifth file (`3pct-ranked-by-stop-safety.md`)

That file has three sections:

1. **Fundamentally Strongest Top Ten** — pure sponsorship ranking from cached dossiers. Not filtered by technical status.
2. **Technically Strongest (Reviewed Names Only — 10 of 25)** — only the 10 names charted this run, ordered by stop-defendability (Near-Valid first, then Likely To Break).
3. **Overall Combined Ranking** — the default master view covering every stock in the page-1 universe. The top row is the stock least likely to break the practical 2–4% stop zone after combining fundamental sponsorship and (where run) stop-defendability. Every row carries an explicit technical review status — `technically reviewed` vs `technical review not run in this execution`. Pending names are not hard rejects; they are excluded by the coverage scope and remain eligible for a future run.

## Files in this run

- [`README.md`](README.md) — this file
- [`screen-universe.md`](screen-universe.md) — raw normalized universe + cache freshness note
- [`3pct-selected-and-watchlist.md`](3pct-selected-and-watchlist.md) — full trade-level writeups for 6 watchlist names (0 selected)
- [`3pct-rejected.md`](3pct-rejected.md) — 4 hard technical rejects + 15 names labeled `technical review not run in this execution` (including 3 Mixed-sponsorship watchouts)
- [`3pct-ranked-by-stop-safety.md`](3pct-ranked-by-stop-safety.md) — 3-section master ranking (fundamental top-10, technical reviewed, overall combined)

## Verdict summary in one line

No current-price selection this run — every one of the top 10 is either in a parabolic late-stage impulse (4 hard-rejects with stop-zone air pockets) or a still-credible setup that needs a pullback first (6 watchlist). Each watchlist entry has a specific retest-entry trigger and hard stop defined in `3pct-selected-and-watchlist.md`; each reject has a named re-check zone in `3pct-rejected.md`.
