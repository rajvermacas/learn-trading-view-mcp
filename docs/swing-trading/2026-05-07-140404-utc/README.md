# Swing Trading Analysis — 2026-05-07

## Run Metadata

- **Run Date:** 2026-05-07
- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Screen Thesis:** Mid-to-large-cap stocks (MCap >₹3,000 Cr) with >30% three-month returns, screened for credible business sponsorship behind the price momentum
- **Filters:** Return over 3months > 30 AND Market Capitalization > 3000

## Universe Summary

| Metric | Count |
|--------|-------|
| Parsed universe (all pages) | 123 stocks |
| User-specified pre-rank cap | 20 |
| Working universe after pre-rank | 20 |
| Fundamentally analyzed | 20 |
| Technically reviewed | 15 |
| Technical coverage limit | Top 15 by fundamental rank |
| Selected (Best Aligned) | 1 |
| Watchlist (Near-Valid) | 14 |
| Rejected (Likely To Break) | 0 |
| Pending technical review | 5 |
| Technical dossiers written | 15 |
| Technical data mode | api_fallback |

## Top 5 Fundamentally Strongest

| Rank | Symbol | Sponsorship | Key Strength |
|------|--------|-------------|--------------|
| 1 | ENGINERSIN | Strongly Sponsored | Two 29% OPM quarters, ₹1,400 Cr net cash, 25% ROCE, 18x P/E |
| 2 | EMMVEE | Strongly Sponsored | Q4 PAT +89%, OPM 33%, P/E 17x vs sector 47x, ALMM catalyst |
| 3 | GVT&D | Strongly Sponsored | QPV 138%, ROCE 55%, debt-free, HVDC order visibility |
| 4 | BSE | Strongly Sponsored | 174% profit growth, zero debt, ROCE 47%, market share expanding |
| 5 | NETWEB | Strongly Sponsored | Revenue doubled, AI/HPC monopoly, zero debt, ROCE 32% |

## Top 5 Technically Strongest (Reviewed Names)

| Rank | Symbol | Verdict | Stop Survivability |
|------|--------|---------|--------------------|
| 1 | SKYGOLD | Best Aligned | Strong — ATH breakout with multi-TF confluence |
| 2 | EMMVEE | Near-Valid | Survivable — 3 independent supports in stop zone |
| 3 | ENGINERSIN | Near-Valid | Adequate — D-EMA10/VWMA converge in zone |
| 4 | GVT&D | Near-Valid | Moderate — breakout confluence at 3% floor |
| 5 | LLOYDSME | Near-Valid | Moderate — pullback from ATH to EMA support |

## Top 5 Overall Combined

| Rank | Symbol | Fund Rank | Tech Verdict | Combined Reason |
|------|--------|-----------|--------------|-----------------|
| 1 | EMMVEE | #2 | Near-Valid (Survivable) | Strongest fundamentals + defensible stop + value discount |
| 2 | ENGINERSIN | #1 | Near-Valid (Adequate) | Top fundamental + multi-TF support convergence |
| 3 | SKYGOLD | #12 | Best Aligned | Best technical setup; moderate fundamentals |
| 4 | GVT&D | #3 | Near-Valid (Moderate) | Elite fundamentals + structural support at floor |
| 5 | BSE | #4 | Near-Valid (Vulnerable) | Clean earnings + zero debt; stop inside 1x ATR |

## How to Read 3pct-ranked-by-stop-safety.md

The fifth file contains three ranking sections:
1. **Fundamentally Strongest Top Ten** — ranked by sponsorship quality from dossiers
2. **Technically Strongest Top Ten** — ranked by stop survivability among reviewed names
3. **Overall Combined Ranking** — master ranking blending fundamental and technical evidence

Every row shows technical review status. Reviewed and pending names are clearly distinguishable.

## Technical Dossier Directory

`technical-dossiers/` contains one crisp markdown dossier per technically reviewed stock (15 files). Each dossier includes core fields, five timeframe notes, support/resistance inventories, trade parameters, verdict, and summary rationale. Filename format: `<RANK>-<SYMBOL>.md` where RANK is the fundamental rank.

## Pre-Rank Methodology

PreRankScore uses percentile ranks of 4 scoring columns with weights: QPV (0.35), QSV (0.35), ROCE (0.20), 3M Return (0.10). Soft penalties: QPV≤0 (-12), QSV≤0 (-12), ROCE<15 (-8), 3M Return≤0 (-8). ROCE<0 gets additional -12 and zero contribution. Top 20 by adjusted score form the working universe.
