# Screen Universe — 3 Month Return 50

**Run Date:** 2026-04-22
**Screen URL:** https://www.screener.in/screens/3615928/3-month-return-50/
**Filter Query:** Return over 3months > 50 AND Market Capitalization > 3000

---

## Visible Screen Schema

### Scoring Columns (used for PreRankScore)
- `Qtr Profit Var %` — weight 0.35
- `Qtr Sales Var %` — weight 0.35
- `ROCE %` — weight 0.20
- `3mth return %` — weight 0.10

### Context-Only Columns (not used for PreRankScore)
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

---

## Pre-Rank Methodology

- Percentile ranking within the full parsed universe for each scoring column (higher = better)
- `PreRankScore = 0.35 × rank(QPV) + 0.35 × rank(QSV) + 0.20 × rank(ROCE) + 0.10 × rank(3mRet)`
- Soft penalties: QPV <= 0 (-12), QSV <= 0 (-12), ROCE < 15 (-8), 3mRet <= 0 (-8)
- Distortion: ROCE < 0 → contribution = 0, penalty = -12

---

## Full Parsed Universe (35 stocks, 2 pages)

| PreRank | Symbol | Name | CMP | P/E | MCap Cr | QPV% | QSV% | ROCE% | 3mRet% | Score | Working Universe | Penalty Flags |
|---------|--------|------|-----|-----|---------|------|------|-------|--------|-------|-----------------|---------------|
| 1 | ATLANTAELE | Atlanta Electric | 1470.20 | 72.59 | 11337 | 125.33 | 79.71 | 50.20 | 97.54 | 91.99 | YES | — |
| 2 | QPOWER | Quality Power El | 1272.70 | 92.07 | 9853 | 169.18 | 291.22 | 26.60 | 90.97 | 91.54 | YES | — |
| 3 | GVT&D | GE Vernova T&D | 4239.40 | 97.14 | 108556 | 138.53 | 58.40 | 54.74 | 59.95 | 84.08 | YES | — |
| 4 | PRECWIRE | Prec. Wires (I) | 395.65 | 55.71 | 7241 | 98.94 | 37.19 | 26.78 | 79.16 | 73.49 | YES | — |
| 5 | BAJAJCON | Bajaj Consumer | 469.50 | 32.24 | 6132 | 105.29 | 30.41 | 30.60 | 58.13 | 70.70 | YES | — |
| 6 | KRN | KRN Heat Exchan | 1202.10 | 110.04 | 7480 | 65.04 | 37.46 | 20.75 | 96.05 | 69.34 | YES | — |
| 7 | CPPLUS | Aditya Infotech | 2183.90 | 101.50 | 25760 | 138.82 | 37.32 | 19.49 | 52.68 | 68.71 | YES | — |
| 8 | MTARTECH | MTAR Tech | 5279.60 | 239.12 | 16232 | 131.84 | 59.30 | 10.51 | 115.00 | 67.62 | YES | ROCE<15(-8) |
| 9 | POWERINDIA | Hitachi Energy | 30335.00 | 153.30 | 135219 | 119.97 | 28.51 | 19.44 | 80.06 | 66.91 | YES | — |
| 10 | DATAPATTNS | Data Pattern | 3828.30 | 85.94 | 21434 | 35.76 | 47.92 | 21.00 | 66.93 | 62.76 | YES | — |
| 11 | VOLTAMP | Volt.Transform. | 11051.00 | 31.56 | 11182 | 34.99 | 30.36 | 29.11 | 60.21 | 60.44 | YES | — |
| 12 | TDPOWERSYS | TD Power Systems | 1062.70 | 75.73 | 16631 | 25.35 | 26.36 | 30.35 | 68.34 | 57.57 | YES | — |
| 13 | SCHNEIDER | Schneider Elect. | 1111.70 | 101.07 | 26447 | 16.65 | 20.06 | 40.90 | 78.50 | 50.18 | YES | — |
| 14 | GEPOWERINF | GE Power | 502.65 | 20.19 | 3390 | 431.62 | 21.69 | 6.09 | 76.46 | 49.43 | YES | ROCE<15(-8) |
| 15 | AXISCADES | AXISCADES Tech. | 1925.90 | 74.61 | 8186 | 110.65 | 25.01 | 13.76 | 74.89 | 49.10 | YES | ROCE<15(-8) |
| 16 | APARINDS | Apar Inds. | 11789.00 | 47.76 | 47358 | 29.80 | 16.18 | 32.70 | 63.41 | 47.35 | YES | — |
| 17 | SHILCTECH | Shilchar Tech. | 5142.90 | 31.71 | 5871 | 21.77 | 10.75 | 71.30 | 69.09 | 47.21 | YES | — |
| 18 | KSHINTL | KSH Internationa | 596.65 | 60.58 | 4047 | -4.62 | 58.52 | 21.45 | 64.71 | 44.21 | YES | QPV<=0(-12) |
| 19 | STLTECH | Sterlite Tech. | 290.99 | 1183.77 | 14205 | 53.33 | 25.95 | 2.86 | 211.85 | 43.18 | YES | ROCE<15(-8) |
| 20 | AEROFLEX | Aeroflex | 304.52 | 82.06 | 4031 | 8.42 | 21.13 | 22.34 | 83.87 | 43.16 | YES | — |
| 21 | MANINDS | Man Industries | 555.65 | 22.18 | 4166 | 61.31 | 13.45 | 15.98 | 70.94 | 43.01 | no | — |
| 22 | SHILPAMED | Shilpa Medicare | 408.35 | 45.18 | 7993 | 69.92 | 28.32 | 7.82 | 51.18 | 41.41 | no | ROCE<15(-8) |
| 23 | AVANTIFEED | Avanti Feeds | 1442.70 | 31.04 | 19631 | 10.40 | 1.31 | 23.99 | 85.41 | 38.12 | no | — |
| 24 | SANSERA | Sansera Enginee. | 2547.00 | 58.02 | 15879 | 44.51 | 24.71 | 13.38 | 50.19 | 34.35 | no | ROCE<15(-8) |
| 25 | HFCL | HFCL | 100.37 | 296.43 | 15358 | 32.55 | 19.65 | 7.55 | 60.93 | 25.49 | no | ROCE<15(-8) |
| 26 | WELCORP | Welspun Corp | 1139.20 | 19.36 | 30047 | -32.91 | 25.43 | 21.24 | 50.07 | 22.71 | no | QPV<=0(-12) |
| 27 | ABB | A B B | 7587.00 | 96.29 | 160779 | -18.35 | 5.71 | 29.93 | 59.54 | 20.68 | no | QPV<=0(-12) |
| 28 | SUVENLIFE | Suven Life Scie. | 212.62 | N/A | 5638 | -160.53 | 74.53 | -86.96 | 54.22 | 10.71 | no | ROCE<0(-12), QPV<=0(-12) |
| 29 | LUXIND | Lux Industries | 1588.25 | 42.18 | 4781 | -46.66 | 21.59 | 12.54 | 75.15 | 9.38 | no | QPV<=0(-12), ROCE<15(-8) |
| 30 | SGMART | SG Mart | 543.90 | 66.65 | 6847 | -61.70 | 23.21 | 11.33 | 65.29 | 6.99 | no | QPV<=0(-12), ROCE<15(-8) |
| 31 | GALLANTT | Gallantt Ispat | 870.55 | 43.78 | 20988 | -11.67 | -4.00 | 19.20 | 60.22 | -1.24 | no | QPV<=0(-12), QSV<=0(-12) |
| 32 | ADANIPOWER | Adani Power | 215.65 | 36.30 | 415731 | -18.89 | -8.92 | 22.54 | 53.03 | -1.68 | no | QPV<=0(-12), QSV<=0(-12) |
| 33 | SUPPETRO | Supreme Petroch. | 804.15 | 55.66 | 15113 | -50.25 | -10.01 | 22.76 | 54.17 | -4.88 | no | QPV<=0(-12), QSV<=0(-12) |
| 34 | GUJALKALI | Gujarat Alkalies | 712.25 | N/A | 5208 | -77.65 | 1.46 | -0.34 | 55.60 | -14.74 | no | ROCE<0(-12), QPV<=0(-12) |
| 35 | JPFL | Jindal Poly Film | 710.85 | N/A | 3113 | -96.92 | -68.66 | 5.36 | 77.31 | -23.29 | no | QPV<=0(-12), QSV<=0(-12), ROCE<15(-8) |

---

## Summary

- **Full parsed universe:** 35 stocks across 2 HTML pages
- **User-specified pre-rank cap:** 20
- **Working universe after pre-rank:** 20 stocks
- **Stocks excluded by pre-rank:** 15 (ranks 21–35)
