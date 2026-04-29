# Screen Universe — Return over 3 Months

**Run Date:** 2026-04-29
**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
**Parsed Universe Size:** 132 stocks across 6 pages
**Pre-Rank Cap (user-specified):** 20
**Working Universe After Pre-Rank:** 20 stocks

## Screen Schema

**Scoring Columns (contribute to PreRankScore):**
- `Qtr Profit Var %` (weight 0.35)
- `Qtr Sales Var %` (weight 0.35)
- `ROCE %` (weight 0.20)
- `3mth return %` (weight 0.10)

**Context-Only Columns (do not contribute to PreRankScore):**
- `CMP Rs.`, `P/E`, `Mar Cap Rs.Cr.`, `Div Yld %`, `NP Qtr Rs.Cr.`, `Sales Qtr Rs.Cr.`

## Pre-Rank Methodology

PreRankScore = 0.35 × rank(QPV) + 0.35 × rank(QSV) + 0.20 × rank(ROCE) + 0.10 × rank(3m return)

**Soft Penalties:**
- QPV ≤ 0: −12 | QSV ≤ 0: −12 | ROCE < 15: −8 | 3m return ≤ 0: −8
- ROCE < 0: contribution = 0 and additional −12

## Full Universe with PreRankScore

| # | Symbol | Name | QPV% | QSV% | ROCE% | 3m% | Base | Pen | Adj | In Top 20 | Flags |
|---|--------|------|------|------|-------|-----|------|-----|-----|-----------|-------|
| 1 | LLOYDSME | Lloyds Metals | 169.05 | 201.94 | 38.28 | 56.36 | 90.22 | 0 | 90.22 | Yes | — |
| 2 | QPOWER | Quality Power El | 169.18 | 291.22 | 26.60 | 126.78 | 89.81 | 0 | 89.81 | Yes | — |
| 3 | ATLANTAELE | Atlanta Electric | 125.33 | 79.71 | 50.20 | 140.81 | 88.71 | 0 | 88.71 | Yes | — |
| 4 | INSOLATION | Insolation Ener | 173.57 | 77.05 | 34.73 | 53.21 | 87.26 | 0 | 87.26 | Yes | — |
| 5 | WEBELSOLAR | Websol Energy | 152.31 | 132.07 | 63.18 | 34.01 | 85.53 | 0 | 85.53 | Yes | — |
| 6 | INDIABULLS | Indiabulls | 259.74 | 302.18 | 16.17 | 60.18 | 84.62 | 0 | 84.62 | Yes | — |
| 7 | ORIANA | Oriana Power | 149.88 | 117.27 | 42.31 | 33.69 | 84.16 | 0 | 84.16 | Yes | — |
| 8 | UTLSOLAR | Fujiyama Power | 124.29 | 73.80 | 38.88 | 53.93 | 83.55 | 0 | 83.55 | Yes | — |
| 9 | GVT&D | GE Vernova T&D | 138.53 | 58.40 | 54.74 | 41.85 | 81.66 | 0 | 81.66 | Yes | — |
| 10 | ENGINERSIN | Engineers India | 219.30 | 58.29 | 25.01 | 47.64 | 81.22 | 0 | 81.22 | Yes | — |
| 11 | NETWEB | Netweb Technol | 146.67 | 141.00 | 32.45 | 31.39 | 81.00 | 0 | 81.00 | Yes | — |
| 12 | CUPID | Cupid | 196.66 | 105.67 | 17.10 | 48.44 | 80.36 | 0 | 80.36 | Yes | — |
| 13 | EMMVEE | Emmvee Photovol | 89.43 | 62.25 | 44.83 | 53.43 | 79.57 | 0 | 79.57 | Yes | — |
| 14 | SKYGOLD | Sky Gold & Diam | 120.42 | 77.13 | 21.21 | 48.11 | 77.02 | 0 | 77.02 | Yes | — |
| 15 | CPPLUS | Aditya Infotech | 138.82 | 37.32 | 19.49 | 66.79 | 73.28 | 0 | 73.28 | Yes | — |
| 16 | PRECWIRE | Prec. Wires | 98.94 | 37.19 | 26.78 | 65.82 | 71.95 | 0 | 71.95 | Yes | — |
| 17 | RUBICON | Rubicon Research | 91.23 | 51.73 | 26.05 | 43.98 | 71.59 | 0 | 71.59 | Yes | — |
| 18 | DIACABS | Diamond Power | 692.98 | 54.21 | 30.38 | — | 79.09 | -8 | 71.09 | Yes | 3m_missing |
| 19 | EBGNG | GNG Electronics | 102.78 | 40.26 | 19.84 | 68.18 | 70.02 | 0 | 70.02 | Yes | — |
| 20 | RRWL | Ram Ratna Wires | 106.33 | 43.80 | 20.17 | 48.83 | 69.34 | 0 | 69.34 | Yes | — |
| 21 | BAJAJCON | Bajaj Consumer | 105.29 | 30.41 | 30.60 | 42.90 | 67.76 | 0 | 67.76 | No | — |
| 22 | SHREEJISHIP | Shreeji Ship | 135.46 | 30.05 | 33.65 | 30.48 | 67.66 | 0 | 67.66 | No | — |
| 23 | KRN | KRN Heat Exchan | 65.04 | 37.46 | 20.75 | 110.38 | 67.50 | 0 | 67.50 | No | — |
| 24 | POWERINDIA | Hitachi Energy | 119.97 | 28.51 | 19.44 | 79.48 | 67.38 | 0 | 67.38 | No | — |
| 25 | SHADOWFAX | Shadowfax | 439.63 | 65.52 | 4.38 | 64.64 | 74.14 | -8 | 66.14 | No | ROCE<15 |

*Remaining 107 stocks omitted for brevity — all scored below 66.14 adjusted PreRankScore*
