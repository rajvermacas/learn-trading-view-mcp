# Swing Trading 3% Screen Run — 2026-04-21

## Run Metadata

- **Run Date:** 2026-04-21
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Title:** "Return over 3 months" by Mrinal
- **Screen Filters:** Return over 3months > 30% AND Market Capitalization > 3000 Cr

## Screen Thesis

This screen surfaces mid-to-large-cap Indian stocks with strong recent 3-month price momentum (>30%), indicating possible institutional sponsorship or catalyst-driven moves. The screen seeks stocks where momentum is backed by recent operating improvement — companies where strong recent returns may be justified by improving business fundamentals, not just relative momentum.

## Universe & Coverage

| Metric | Count |
|--------|-------|
| Full parsed universe (all pages) | 118 |
| User-specified pre-rank cap | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 |
| Technically reviewed | 15 |
| Technical review not run (user-imposed limit) | 5 |
| **Selected (Best Aligned)** | **8** |
| **Watchlist (Near-Valid)** | **7** |
| Rejected (Likely To Break) | 0 |
| Technical dossiers written | 15 |

## Pre-Rank Step

The full 118-stock universe was reduced to 20 using `PreRankScore`:
- **Scoring columns:** Qtr Profit Var % (0.35), Qtr Sales Var % (0.35), ROCE % (0.20), 3mth return % (0.10)
- **Context-only columns:** CMP, P/E, Mar Cap, Div Yld %, NP Qtr, Sales Qtr
- **Soft penalties:** QPV ≤ 0 (-12), QSV ≤ 0 (-12), ROCE < 15 (-8), ROCE < 0 (-12 additional), 3mR ≤ 0 (-8)
- Percentile ranks computed from valid values only; missing/invalid metrics contribute 0

## Top 5 Fundamentally Strongest

| Rank | Symbol | Verdict | Key Reason |
|------|--------|---------|------------|
| 1 | LLOYDSME | Strongly Sponsored | SEBI-filed 120% volume inflection, 4Q OPM 33%, TTM doubled |
| 2 | BSE | Strongly Sponsored | 174% profit growth, zero debt, ROCE 46.6%, ATH |
| 3 | GVT&D | Strongly Sponsored | Zero debt + 1590 Cr cash + 14380 Cr order backlog |
| 4 | SHARDACROP | Strongly Sponsored | 3 beats, zero debt, 826 Cr cash, P/E 17.7x |
| 5 | ATLANTAELE | Strongly Sponsored | PGCIL EHV 400kV approval, ROCE 50% |

## Top 5 Technically Strongest (Among Reviewed)

| Rank | Symbol | Verdict | Stop Survivability | Key Reason |
|------|--------|---------|-------------------|------------|
| 1 | LLOYDSME | Best Aligned | Strong | 5 support layers in stop zone, bull flag, weekly impulse |
| 2 | BSE | Best Aligned | Strong | ATH breakout on 5x volume, layered EMA defense |
| 3 | SHARDACROP | Best Aligned | Strong | Post-breakout with tested 1067 support, intact HL structure |
| 4 | GROWW | Best Aligned | Moderate | Pristine uptrend, ATH on 5.3x volume, 1:5+ R:R |
| 5 | BAJAJCON | Best Aligned | Moderate | 38.2% Fib pullback on 13x volume breakout, 1:3 R:R |

## Top 5 Overall Combined

| Rank | Symbol | Fund Rank | Tech Verdict | Combined Reason |
|------|--------|-----------|--------------|-----------------|
| 1 | LLOYDSME | #1 | Best Aligned (Strong) | Top fundamental + top technical alignment |
| 2 | BSE | #2 | Best Aligned (Strong) | Elite fundamentals + ATH breakout confirmation |
| 3 | SHARDACROP | #4 | Best Aligned (Strong) | Value P/E + tested stop + zero debt cash floor |
| 4 | GVT&D | #3 | Best Aligned (Moderate) | Best business quality, parabolic extension only caveat |
| 5 | GROWW | #9 | Best Aligned (Moderate) | Institutional demand signal + 1:5 R:R |

## How to Read the Ranked File (3pct-ranked-by-stop-safety.md)

The ranked file has three sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names
3. **Overall Combined Ranking** — the default master ranking with technical status explicit

Reviewed names show technical verdicts and labels. Pending names show only fundamental ranking. The combined ranking treats "Best Aligned + Strong" as highest, then "Best Aligned + Moderate", then "Near-Valid", then pending technical names at their fundamental rank position.

## Technical Dossier Directory

`technical-dossiers/` contains one verbose markdown dossier for every technically reviewed stock (15 files). Each dossier includes: core fields, 5 timeframe notes (30-min most detailed), support/resistance inventories, trade parameters, verdict fields, and summary rationale. Filenames use format `<RANK>-<SYMBOL>.md` where rank is the fundamental rank.

These dossiers are user-facing audit records only and must not be reused as cache input.
