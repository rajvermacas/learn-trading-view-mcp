# Screen Universe — 2026-05-04

## Source

- URL: https://www.screener.in/screens/3474384/return-over-3-months
- Pages fetched: 4 (25+25+25+20 = 95 stocks)
- Deduplication: none required (no duplicates found)
- Filters: Return over 3 months > 30% AND Market Capitalization > 3000 Cr

## Fixed Screen Schema

### Scoring Columns (contribute to PreRankScore)

| Column | Weight | Direction |
|--------|--------|-----------|
| Qtr Profit Var % | 0.35 | higher-is-better |
| Qtr Sales Var % | 0.35 | higher-is-better |
| ROCE % | 0.20 | higher-is-better |
| 3mth return % | 0.10 | higher-is-better |

### Context-Only Columns (do NOT contribute to PreRankScore)

- CMP Rs.
- P/E
- Mar Cap Rs.Cr.
- Div Yld %
- NP Qtr Rs.Cr.
- Sales Qtr Rs.Cr.

## Soft Penalties

- QPV <= 0: subtract 12
- QSV <= 0: subtract 12
- ROCE < 15: subtract 8
- 3M return <= 0: subtract 8
- ROCE < 0: zero contribution + subtract 12

## Pre-Ranked Working Universe (Top 20 of 95)

| Rank | S.No | Name | QPV% | QSV% | ROCE% | 3M% | AdjScore | Penalties | In Working Universe |
|------|------|------|------|------|-------|-----|----------|-----------|---------------------|
| 1 | 20 | Quality Power El | 169.18 | 291.22 | 26.60 | 82.39 | 88.66 | none | YES |
| 2 | 8 | Lloyds Metals | 169.05 | 201.94 | 38.28 | 53.80 | 88.21 | none | YES |
| 3 | 3 | Atlanta Electric | 125.33 | 79.71 | 50.20 | 106.89 | 88.19 | none | YES |
| 4 | 2 | Websol Energy | 152.31 | 132.07 | 63.18 | 51.88 | 87.72 | none | YES |
| 5 | 47 | Indiabulls | 259.74 | 302.18 | 16.17 | 102.05 | 85.58 | none | YES |
| 6 | 7 | Fujiyama Power | 124.29 | 73.80 | 38.88 | 44.25 | 80.96 | none | YES |
| 7 | 44 | Cupid | 196.66 | 105.67 | 17.10 | 52.60 | 79.91 | none | YES |
| 8 | 22 | Engineers India | 219.30 | 58.29 | 25.01 | 51.20 | 79.43 | none | YES |
| 9 | 95 | Diamond Power | 692.98 | 54.21 | 32.21 | — | 78.30 | none | YES |
| 10 | 31 | Sky Gold & Diam. | 120.42 | 77.13 | 21.21 | 40.64 | 74.67 | none | YES |
| 11 | 63 | HFCL | 319.21 | 127.81 | 10.86 | 83.95 | 73.48 | ROCE<15 | YES |
| 12 | 69 | DEE Development | 262.27 | 76.96 | 9.39 | 109.78 | 70.14 | ROCE<15 | YES |
| 13 | 38 | Aditya Infotech | 138.82 | 37.32 | 19.49 | 60.86 | 69.92 | none | YES |
| 14 | 4 | Emmvee Photovol. | 89.43 | 62.25 | 44.83 | 30.15 | 69.63 | none | YES |
| 15 | 19 | Prec. Wires (I) | 98.94 | 37.19 | 26.78 | 72.48 | 69.24 | none | YES |
| 16 | 36 | Ram Ratna Wires | 106.33 | 43.80 | 20.17 | 55.09 | 67.73 | none | YES |
| 17 | 14 | Acutaas Chemical | 110.88 | 40.28 | 31.56 | 35.88 | 67.42 | none | YES |
| 18 | 37 | GNG Electronics | 102.78 | 40.26 | 19.84 | 61.04 | 66.15 | none | YES |
| 19 | 21 | Rubicon Research | 91.23 | 51.73 | 26.05 | 35.27 | 66.09 | none | YES |
| 20 | 39 | Hitachi Energy | 119.97 | 28.51 | 19.44 | 71.21 | 64.03 | none | YES |

## Stocks Below the Cut (Ranks 21-95)

| Rank | S.No | Name | AdjScore | Penalties | In Working Universe |
|------|------|------|----------|-----------|---------------------|
| 21 | 87 | Shadowfax Tech. | 63.67 | ROCE<15 | NO |
| 22 | 33 | KRN Heat Exchan | 63.34 | none | NO |
| 23 | 64 | MTAR Technologie | 63.32 | ROCE<15 | NO |
| 24 | 78 | Sterlite Tech. | 61.63 | ROCE<15 | NO |
| 25 | 32 | Data Pattern | 59.23 | none | NO |
| 26 | 34 | Jayaswal Neco | 58.91 | none | NO |
| 27 | 12 | Cemindia Project | 58.60 | none | NO |
| 28 | 1 | Siemens Ener.Ind | 58.18 | none | NO |
| 29 | 54 | Sambhv Steel | 57.85 | ROCE<15 | NO |
| 30 | 55 | AXISCADES Tech. | 57.22 | ROCE<15 | NO |
| 31 | 7 | Fujiyama Power | — | — | (already in as rank 6) |
| 32-95 | — | Remaining 64 stocks | <57 | various | NO |

*Full 95-stock detail omitted for brevity. Stocks 32-95 scored below 57.22 with various penalty combinations. Notable exclusions with high penalties: Shanti Educat. (QPV<=0, QSV<=0), Gallantt Ispat (QPV<=0, QSV<=0), Praj Industries (QPV<=0, QSV<=0), NOCIL (QPV<=0, QSV<=0), OneSource (QPV<=0, QSV<=0), Jindal Poly (QPV<=0, QSV<=0), Gujarat Alkalies (ROCE<0, QPV<=0), Meesho (ROCE<0, QPV<=0), Ather Energy (ROCE<0), Suven Life (ROCE<0, QPV<=0, QSV missing anomaly).*

## Missing/Distorted Data Flags

| Stock | Flag |
|-------|------|
| Diamond Power (S.No 95) | 3mth return missing — 3M contribution set to 0 |
| Jindal Poly Film (S.No 86) | Mar Cap missing — context column, no scoring impact |
| Aequs, Gujarat Alkalies, Ideaforge, Meesho, Ather, Suven Life | P/E missing — context column, no scoring impact |
| Gujarat Alkalies | ROCE -0.34 — contribution zeroed, -12 extra penalty |
| Ideaforge Tech | ROCE -2.44 — contribution zeroed, -12 extra penalty |
| Meesho | ROCE -8.71 — contribution zeroed, -12 extra penalty |
| Ather Energy | ROCE -19.77 — contribution zeroed, -12 extra penalty |
| Suven Life Scie. | ROCE -86.96 — contribution zeroed, -12 extra penalty |
