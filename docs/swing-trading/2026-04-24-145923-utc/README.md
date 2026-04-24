# Swing Trading 3% Screen — 2026-04-24

## Run Details

- **Run Date**: 2026-04-24
- **Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Filter**: Return over 3months > 30 AND Market Capitalization > 3000
- **Pages Fetched**: 1 of 5 (user-limited)

## Screen Thesis

**"Return over 3 months"** — This screen surfaces mid-to-large cap Indian stocks (market cap > Rs 3,000 Cr) that have delivered 30%+ price returns over the trailing 3 months. The thesis targets momentum-driven names where recent strong price appreciation may be backed by credible business sponsorship, making them candidates for 1–8 week swing trades with a practical 2–4% downside stop zone.

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe (page 1) | 15 |
| User-specified pre-rank cap | 3 |
| Working universe after pre-rank | 3 |
| Fundamentally analyzed | 3 (all cached fresh) |
| Technically reviewed | 3 |
| Selected | 1 |
| Watchlist | 2 |
| Rejected | 0 |
| Pending technical review | 0 |
| Technical dossiers written | 3 |

- **Coverage mode**: Full (all 3 working-universe stocks reviewed)
- **Technical data mode**: api_fallback (TradingView MCP disconnected)
- **Fundamental cache**: All 3 stocks were `fresh` — no refresh needed

## Top Fundamentally Strongest

| Rank | Symbol | Sponsorship | Key Reason |
|------|--------|-------------|------------|
| 1 | LLOYDSME | Strongly Sponsored | 120% YoY iron ore volume, OPM 33%, P/E ~25x TTM |
| 2 | GVT&D | Strongly Sponsored | Zero debt, Rs 14,380 Cr order backlog, HVDC catalysts |
| 3 | ATLANTAELE | Strongly Sponsored | PGCIL EHV 400 kV approval, ROCE 50% |

## Top Technically Strongest (Reviewed)

| Rank | Symbol | Stop Survivability | Verdict |
|------|--------|-------------------|---------|
| 1 | LLOYDSME | Near-Valid | Selected |
| 2 | GVT&D | Likely To Break | Watchlist |
| 3 | ATLANTAELE | Likely To Break | Watchlist |

## Top Overall Combined

| Rank | Symbol | Fund. Rank | Tech Verdict | Key Reason |
|------|--------|------------|--------------|------------|
| 1 | LLOYDSME | 1 | Selected | Best combined: volume catalyst + structural support near CMP |
| 2 | GVT&D | 2 | Watchlist | Superior business quality but ATR exceeds 3% stop framework |
| 3 | ATLANTAELE | 3 | Watchlist | Genuine catalyst but parabolic structure with empty stop zone |

## Pre-Rank Step

The pre-rank reduced 15 parsed stocks to the top 3 using `PreRankScore`:
- **Scoring columns**: Qtr Profit Var % (0.35), Qtr Sales Var % (0.35), ROCE % (0.20), 3mth return % (0.10)
- **Method**: Percentile ranking within the parsed universe, then weighted sum
- **Soft penalties**: QPV ≤ 0 (−12), QSV ≤ 0 (−12), ROCE < 15 (−8), 3mth ≤ 0 (−8)
- Only Tanfac Inds. received penalties (QPV and QSV both negative, −24 total)
- See `screen-universe.md` for the full scored universe

## File Guide

| File | Contents |
|------|----------|
| `3pct-selected-and-watchlist.md` | Full trade-level writeups for all 3 stocks |
| `3pct-rejected.md` | No hard rejects; watchlist boundary notes and 12 pre-rank excluded stocks |
| `screen-universe.md` | Full 15-stock parsed universe with PreRankScores and penalty flags |
| `3pct-ranked-by-stop-safety.md` | Three ranking views: fundamental, technical, and combined master ranking |
| `technical-dossiers/` | One crisp dossier per technically reviewed stock (3 dossiers) |

## Technical Dossier Directory

The `technical-dossiers/` folder contains one markdown file per reviewed stock:
- `1-LLOYDSME.md` — Selected, Near-Valid
- `2-GVT-D.md` — Watchlist, Likely To Break
- `3-ATLANTAELE.md` — Watchlist, Likely To Break

Each dossier covers: core fields, 5-timeframe notes (weekly/daily/60/30/15), support and resistance inventories, trade parameters, verdict fields, and summary rationale. Filename prefix is the fundamental rank.
