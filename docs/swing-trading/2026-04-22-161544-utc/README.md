# Swing Trading Screen — 3 Month Return 50

**Run Date:** 2026-04-22
**Screen URL:** https://www.screener.in/screens/3615928/3-month-return-50/
**Screen Thesis:** Surface stocks with >50% 3-month return and >3000 Cr MCap. Testing whether strong recent price momentum is backed by credible fundamental sponsorship and whether the current price location can defend a practical 2–4% stop zone.

---

## Universe Summary

| Metric | Count |
|--------|-------|
| Full parsed universe | 35 stocks (2 HTML pages) |
| User-specified pre-rank cap | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 (18 cached fresh + 2 new) |
| Technically reviewed | 15 (user limited: top 15) |
| **Selected** | **3** |
| Watchlist | 8 |
| Rejected (technical) | 4 |
| Pending technical review | 5 |
| Technical dossiers written | 15 |

---

## Top 5 Fundamentally Strongest

| Rank | Symbol | Verdict | Confidence |
|------|--------|---------|------------|
| 1 | SHILCTECH | Strongly Sponsored | High |
| 2 | GVT&D | Strongly Sponsored | High |
| 3 | ATLANTAELE | Strongly Sponsored | High |
| 4 | QPOWER | Strongly Sponsored | Medium |
| 5 | POWERINDIA | Present | High |

## Top 5 Technically Strongest (Reviewed)

| Rank | Symbol | Verdict | Survivability |
|------|--------|---------|---------------|
| 1 | SHILCTECH | Best Aligned | Highly Survivable |
| 2 | TDPOWERSYS | Best Aligned | Strong |
| 3 | VOLTAMP | Best Aligned | Moderate-Strong |
| 4 | GVT&D | Near-Valid | Near-Valid |
| 5 | BAJAJCON | Near-Valid | Near-Valid |

## Top 5 Overall Combined

| Rank | Symbol | Combined Verdict |
|------|--------|-----------------|
| 1 | SHILCTECH | Selected |
| 2 | VOLTAMP | Selected |
| 3 | TDPOWERSYS | Selected |
| 4 | GVT&D | Watchlist |
| 5 | BAJAJCON | Watchlist |

---

## File Guide

| File | Purpose |
|------|---------|
| `3pct-selected-and-watchlist.md` | Full trade-level writeups for 3 selected + 8 watchlist stocks |
| `3pct-rejected.md` | Evidence-based rejection summaries for 4 technically rejected + 5 pending |
| `screen-universe.md` | Full 35-stock parsed universe with PreRankScore, penalties, working-universe status |
| `3pct-ranked-by-stop-safety.md` | Master ranking: fundamental top 10, technical top 10, combined ranking for all 20 |
| `technical-dossiers/` | 15 verbose per-stock technical audit dossiers |

---

## How to Read the Rankings File

`3pct-ranked-by-stop-safety.md` has three sections:

1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality, not chart
2. **Technically Strongest Top Ten** — ranked by stop-zone defendability among reviewed names only
3. **Overall Combined Ranking** — the master list. Top row = least likely to break the stop zone combining both fundamental and technical evidence. Bottom row = most likely to break through. Pending names are listed at the bottom with explicit "Pending Technical" status.

---

## Technical Dossiers

`technical-dossiers/` contains 15 markdown files, one per technically reviewed stock. Filenames use `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank.

Each dossier covers: core fields, 5 timeframe notes (weekly through 15-min), support inventory, resistance inventory, trade parameters, verdict fields, and a summary rationale. The 30-min note is always the most detailed as the primary execution frame.

These are user-facing audit records only — they are never reused as cache or ranking inputs.

---

## Pre-Rank Step

The pre-rank reduced 35 parsed stocks to 20 using `PreRankScore`:
- Weighted percentile ranking of 4 scoring columns (QPV 0.35, QSV 0.35, ROCE 0.20, 3mRet 0.10)
- Soft penalties for negative growth (QPV/QSV <= 0: -12 each), low ROCE (<15: -8, <0: -12 + zero contrib), negative momentum (3mRet <= 0: -8)
- Sorted descending, top 20 kept

This step is cheap (uses only Screener HTML data, no per-stock fetches) and prevents low-quality names from consuming fundamental analysis budget.
