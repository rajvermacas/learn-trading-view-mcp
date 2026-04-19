# Swing Trading 3% Screen — Run Report

## Run Summary

- **Run Date**: 2026-04-18 12:24 UTC
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months/?page=1
- **Pages Fetched**: Page 1 only (user-imposed limit)

## Parsed Screen Thesis

- **Screen Title**: Return over 3 months
- **Visible Filters**:
  - Return over 3 months > 30%
  - Market Capitalization > 3,000 Cr Rs.
  - Only companies with Mar 2026 results
- **Screen Intent**: Surface stocks with strong recent price momentum (30%+ in 3 months) backed by the latest quarterly results and meaningful market size. The screen is designed to find momentum names where business evidence can credibly explain the price move.
- **Coverage Mode**: User-limited run — fundamentals for 3 stocks only (top 3 by screener rank); technical review for top 1 fundamentally ranked stock only.

## Universe Counts

| Metric | Count |
|---|---|
| Total universe (page 1) | 25 stocks |
| Fundamentally analyzed (this run) | 3 stocks (user limit) |
| Fundamentally pending (not analyzed) | 22 stocks |
| Technically reviewed | 1 stock (user limit) |
| Technical pending (not reviewed) | 24 stocks |
| Selected (immediate buy) | 0 |
| Watchlist | 1 (SHILCTECH) |
| Rejected (technical) | 0 |
| Rejected (fundamental — below limit) | 0 |

## Top 5 Fundamentally Strongest (of 3 Analyzed)

| Rank | Symbol | Company | Sponsorship Verdict | Confidence |
|---|---|---|---|---|
| #1 | SHILCTECH | Shilchar Technologies Ltd | Strongly Sponsored | High |
| #2 | GVT&D | GE Vernova T&D India Ltd | Strongly Sponsored | High |
| #3 | ATLANTAELE | Atlanta Electricals Ltd | Strongly Sponsored | High |
| — | (22 stocks) | Not analyzed — user-imposed 3-stock limit | — | — |

## Top 5 Technically Strongest (of 1 Reviewed)

| Rank | Symbol | Technical Verdict | Stop Survivability |
|---|---|---|---|
| #1 | SHILCTECH | Near-Valid | Moderate |
| — | All others | Technical review not run in this execution | — |

## Top 5 Overall Combined

| Combined Rank | Symbol | Fundamental Rank | Technical Verdict | Status |
|---|---|---|---|---|
| #1 | SHILCTECH | #1 | Near-Valid | Watchlist |
| #2 | GVT&D | #2 | Pending technical review | Pending |
| #3 | ATLANTAELE | #3 | Pending technical review | Pending |
| — | Remaining 22 | Not fundamentally analyzed | Not reviewed | Not run |

## How to Read `3pct-ranked-by-stop-safety.md`

The master ranking file contains three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality, strongest first
2. **Technically Strongest Top Ten** — ranked by stop survivability, least likely to break first
3. **Overall Combined Ranking** — the master list combining both dimensions with review status made explicit

Stocks marked **pending technical review** have not had chart work done in this execution. They are not rejects — they are unreviewed. Do not draw conclusions about their stop survivability from this run.

The combined ranking cannot pretend equal certainty for reviewed and pending names. SHILCTECH is the only stock with a full 5-timeframe technical assessment in this run.
