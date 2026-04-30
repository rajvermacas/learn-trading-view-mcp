# Screen Universe — 2026-04-30

## Screen Details

- **URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Title:** Return over 3 months
- **Filters:** Return over 3 months > 30%, Market Capitalization > 3000 Cr
- **Pages fetched:** 5 (25 + 25 + 25 + 25 + 13 = 113 stocks)
- **Deduplication:** No duplicates found
- **Total parsed universe:** 113 stocks

## Fixed Screen Schema

**Scoring columns (contribute to PreRankScore):**
- `Qtr Profit Var %` (weight 0.35)
- `Qtr Sales Var %` (weight 0.35)
- `ROCE %` (weight 0.20)
- `3mth return %` (weight 0.10)

**Context-only columns (do NOT contribute to PreRankScore):**
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

## Pre-Rank Methodology

PreRankScore = 0.35 × rank(Qtr Profit Var %) + 0.35 × rank(Qtr Sales Var %) + 0.20 × rank(ROCE %) + 0.10 × rank(3mth return %)

Percentile ranks computed within the 113-stock universe (higher is better for all four columns). Soft penalties applied post-score: -12 for Qtr Profit Var ≤ 0, -12 for Qtr Sales Var ≤ 0, -8 for ROCE < 15%, -8 for 3m return ≤ 0, -12 for ROCE < 0 (with contribution zeroed).

## Full Universe with PreRankScore

| Rank | Stock | QPV% | QSV% | ROCE% | 3mRet% | Score | In Working | Penalties |
|---|---|---|---|---|---|---|---|---|
| 1 | Lloyds Metals | 169.05 | 201.94 | 38.28 | 59.85 | 88.84 | YES | - |
| 2 | Quality Power El | 169.18 | 291.22 | 26.60 | 106.99 | 88.55 | YES | - |
| 3 | Atlanta Electric | 125.33 | 79.71 | 50.20 | 131.64 | 87.70 | YES | - |
| 4 | Indiabulls | 259.74 | 302.18 | 16.17 | 85.43 | 85.22 | YES | - |
| 5 | Websol Energy | 152.31 | 132.07 | 63.18 | 35.95 | 84.72 | YES | - |
| 6 | Insolation Ener | 173.57 | 77.05 | 34.73 | 46.30 | 84.21 | YES | - |
| 7 | Oriana Power | 149.88 | 117.27 | 42.31 | 35.30 | 82.39 | YES | - |
| 8 | Fujiyama Power | 124.29 | 73.80 | 38.88 | 48.78 | 81.04 | YES | - |
| 9 | Engineers India | 219.30 | 58.29 | 25.01 | 46.08 | 79.22 | YES | - |
| 10 | Cupid | 196.66 | 105.67 | 17.10 | 49.10 | 78.86 | YES | - |
| 11 | BSE | 175.79 | 61.97 | 46.57 | 30.16 | 78.51 | YES | - |
| 12 | GE Vernova T&D | 138.53 | 58.40 | 54.74 | 38.26 | 78.15 | YES | - |
| 13 | Sky Gold & Diam. | 120.42 | 77.13 | 21.21 | 49.43 | 75.87 | YES | - |
| 14 | Emmvee Photovol. | 89.43 | 62.25 | 44.83 | 36.90 | 73.18 | YES | - |
| 15 | HFCL | 319.21 | 127.81 | 10.86 | 69.12 | 71.91 | YES | low_roce |
| 16 | Aditya Infotech | 138.82 | 37.32 | 19.49 | 68.28 | 69.62 | YES | - |
| 17 | Prec. Wires (I) | 98.94 | 37.19 | 26.78 | 72.51 | 69.52 | YES | - |
| 18 | Rubicon Research | 91.23 | 51.73 | 26.05 | 41.75 | 68.69 | YES | - |
| 19 | Acutaas Chemical | 110.88 | 40.28 | 31.56 | 35.64 | 67.60 | YES | - |
| 20 | Ram Ratna Wires | 106.33 | 43.80 | 20.17 | 51.34 | 67.20 | YES | - |
| 21 | GNG Electronics | 102.78 | 40.26 | 19.84 | 69.28 | 66.52 | no | - |
| 22 | Shreeji Ship. | 135.46 | 30.05 | 33.65 | 32.20 | 65.04 | no | - |
| 23 | KRN Heat Exchan | 65.04 | 37.46 | 20.75 | 102.92 | 64.56 | no | - |
| 24 | Shadowfax Tech | 439.63 | 65.52 | 4.38 | 55.49 | 64.04 | no | low_roce |
| 25 | Hitachi Energy | 119.97 | 28.51 | 19.44 | 77.87 | 63.73 | no | - |
| 26 | MTAR Technologie | 131.84 | 59.30 | 10.51 | 120.27 | 61.68 | no | low_roce |
| 27 | Bajaj Consumer | 105.29 | 30.41 | 30.60 | 32.72 | 61.57 | no | - |
| 28 | Hind Rectifiers | 47.85 | 44.00 | 21.60 | 50.38 | 61.43 | no | - |
| 29 | Sterlite Tech. | 744.40 | 36.98 | 7.75 | 177.20 | 60.94 | no | low_roce |
| 30 | Data Pattern | 35.76 | 47.92 | 21.00 | 52.77 | 59.48 | no | - |
| 31 | SG Finserve | 77.68 | 94.88 | 9.32 | 69.62 | 57.34 | no | low_roce |
| 32 | Volt.Transform. | 34.99 | 30.36 | 29.11 | 59.22 | 56.55 | no | - |
| 33 | Skipper | 70.33 | 29.42 | 26.58 | 32.28 | 56.19 | no | - |
| 34 | CIAN Agro | 173.51 | 62.92 | 6.82 | 36.20 | 55.84 | no | low_roce |
| 35 | Siemens Ener.Ind | 51.67 | 25.97 | 67.75 | 31.83 | 54.79 | no | - |
| 36 | Sambhv Steel | 112.79 | 59.64 | 13.92 | 30.94 | 53.19 | no | low_roce |
| 37 | TD Power Systems | 25.35 | 26.36 | 30.35 | 58.01 | 51.93 | no | - |
| 38 | Jayaswal Neco | 87.79 | 17.85 | 20.67 | 51.23 | 51.29 | no | - |
| 39 | Prime Focus | 237.06 | 32.74 | 7.95 | 37.37 | 51.02 | no | low_roce |
| 40 | Shaily Engineer. | 96.47 | 26.90 | 16.97 | 32.34 | 50.60 | no | - |
| 41 | Dynamatic Tech. | 316.15 | 34.70 | 8.96 | 31.48 | 50.46 | no | low_roce |
| 42 | GE Power | 431.62 | 21.69 | 6.09 | 102.43 | 50.42 | no | low_roce |
| 43 | Schneider Elect. | 16.65 | 20.06 | 40.90 | 79.52 | 49.62 | no | - |
| 44 | Kirl.Pneumatic | 68.58 | 21.13 | 30.36 | 31.75 | 49.59 | no | - |
| 45 | Inox India | 26.34 | 28.45 | 37.98 | 30.58 | 48.99 | no | - |
| 46 | CG Power & Ind | 18.42 | 26.22 | 37.48 | 39.26 | 48.86 | no | - |
| 47 | Natco Pharma | 13.91 | 36.33 | 32.78 | 31.09 | 48.12 | no | - |
| 48 | Premier Energies | 53.48 | 13.02 | 41.12 | 41.43 | 48.02 | no | - |
| 49 | S C I | 436.24 | 22.50 | 9.81 | 35.10 | 46.74 | no | low_roce |
| 50 | Kajaria Ceramics | 117.94 | 12.40 | 23.27 | 31.61 | 46.64 | no | - |
| 51 | AXISCADES Tech. | 110.65 | 25.01 | 13.76 | 64.12 | 46.51 | no | low_roce |
| 52 | Gokul Agro | 7.17 | 26.58 | 34.20 | 43.77 | 46.44 | no | - |
| 53 | Apar Inds. | 29.80 | 16.18 | 32.70 | 54.25 | 45.87 | no | - |
| 54 | Yatharth Hospit. | 48.74 | 46.23 | 13.99 | 39.65 | 45.65 | no | low_roce |
| 55 | Shilchar Tech. | 21.77 | 10.75 | 71.30 | 52.86 | 45.12 | no | - |
| 56 | Wheels India | 42.00 | 21.18 | 16.14 | 61.14 | 45.09 | no | - |
| 57 | Sigma Advanced | 3.15 | 667.25 | 8.74 | 68.93 | 44.65 | no | low_roce |
| 58 | Aarti Industries | 221.74 | 25.77 | 6.32 | 36.44 | 44.59 | no | low_roce |
| 59 | Kirloskar Oil | 79.61 | 28.82 | 13.68 | 44.65 | 43.78 | no | low_roce |
| 60 | Techno Elec.Engg | 24.23 | 37.12 | 16.54 | 31.68 | 43.57 | no | - |
| 61 | Finolex Cables | 11.40 | 35.23 | 17.67 | 37.15 | 42.91 | no | - |
| 62 | KSH Internationa | -4.62 | 58.52 | 21.45 | 91.38 | 42.86 | no | neg_profit |
| 63 | Man Industries | 61.31 | 13.45 | 15.98 | 61.80 | 42.76 | no | - |
| 64 | Ingersoll-Rand | 15.75 | 19.39 | 60.02 | 32.14 | 42.37 | no | - |
| 65 | Aeroflex | 8.42 | 21.13 | 22.34 | 70.99 | 42.32 | no | - |
| 66 | Rossell Techsys | 18.27 | 71.55 | 8.18 | 45.67 | 41.04 | no | low_roce |
| 67 | Deep Industries | 56.07 | 43.06 | 12.06 | 30.58 | 41.02 | no | low_roce |
| 68 | Ather Energy | 59.76 | 50.20 | -65.71 | 50.48 | 40.44 | no | neg_roce(-12) |
| 69 | Va Tech Wabag | 35.67 | 18.53 | 19.70 | 40.08 | 40.38 | no | - |
| 70 | Amber Enterp. | 26.43 | 37.94 | 14.49 | 40.38 | 40.12 | no | low_roce |
| 71 | C P C L | 202.57 | -2.50 | 35.11 | 30.29 | 39.05 | no | neg_sales |
| 72 | Azad Engineering | 40.14 | 31.38 | 12.23 | 46.88 | 38.99 | no | low_roce |
| 73 | GE Shipping Co | 142.21 | 17.59 | 13.86 | 31.14 | 38.02 | no | low_roce |
| 74 | ISGEC Heavy | 102.88 | 16.26 | 14.83 | 44.11 | 37.33 | no | low_roce |
| 75 | Park Medi World | 11.38 | 17.76 | 20.36 | 50.04 | 36.81 | no | - |
| 76 | Shilpa Medicare | 69.92 | 28.32 | 7.82 | 40.73 | 36.80 | no | low_roce |
| 77 | Shivalik Bimetal | 25.38 | 8.88 | 25.57 | 40.10 | 36.66 | no | - |
| 78 | Supreme Petroch. | 59.18 | 3.12 | 19.23 | 32.86 | 35.50 | no | - |
| 79 | B H E L | 189.83 | 16.44 | 4.87 | 34.15 | 35.47 | no | low_roce |
| 80 | Himadri Special | 29.06 | 13.50 | 22.16 | 31.90 | 35.39 | no | - |
| 81 | Avanti Feeds | 10.40 | 1.31 | 23.99 | 73.22 | 34.69 | no | - |
| 82 | Sansera Enginee. | 44.51 | 24.71 | 13.38 | 44.86 | 34.59 | no | low_roce |
| 83 | Thermax | 40.63 | 4.19 | 16.22 | 41.68 | 33.49 | no | - |
| 84 | Aequs | 17.87 | 50.77 | 1.11 | 38.76 | 32.85 | no | low_roce |
| 85 | KS Smart Tech | 186.17 | — | — | — | 30.94 | no | miss_sales, miss_roce, miss_return |
| 86 | Kennametal India | 9.91 | 16.38 | 17.55 | 39.39 | 30.35 | no | - |
| 87 | Bharat Forge | 40.77 | 24.96 | 12.18 | 30.54 | 28.49 | no | low_roce |
| 88 | Welspun Corp | -32.91 | 25.43 | 21.24 | 73.71 | 27.96 | no | neg_profit |
| 89 | Adani Power | 52.34 | -0.10 | 17.29 | 63.87 | 25.87 | no | neg_sales |
| 90 | Adani Green | 55.75 | 13.96 | 7.02 | 43.98 | 25.18 | no | low_roce |
| 91 | AGI Infra | 36.92 | -4.28 | 22.03 | 54.27 | 24.09 | no | neg_sales |
| 92 | Paisalo Digital | 7.06 | 17.82 | 13.13 | 45.68 | 21.51 | no | low_roce |
| 93 | T R I L | -2.55 | 15.70 | 23.30 | 41.52 | 20.32 | no | neg_profit |
| 94 | Adani Energy Sol | 5.66 | 16.76 | 9.71 | 50.01 | 18.92 | no | low_roce |
| 95 | Aditya AMC | -17.96 | 6.85 | 32.24 | 33.68 | 15.39 | no | neg_profit |
| 96 | Suven Life Scie. | -160.53 | 74.53 | -86.96 | 59.54 | 15.09 | no | neg_profit, neg_roce |
| 97 | E2E Networks | -52.68 | 185.66 | -0.51 | 35.88 | 14.76 | no | neg_profit, neg_roce |
| 98 | ACME Solar Hold. | -3.66 | 42.34 | 8.42 | 34.13 | 14.51 | no | neg_profit, low_roce |
| 99 | KSB | -22.87 | 0.99 | 24.52 | 38.18 | 11.98 | no | neg_profit |
| 100 | SG Mart | -61.70 | 23.21 | 11.33 | 57.50 | 8.85 | no | neg_profit, low_roce |
| 101 | Lux Industries | -46.66 | 21.59 | 12.54 | 50.07 | 8.37 | no | neg_profit, low_roce |
| 102 | Dalmia Bharat | 17.64 | -16.70 | 9.48 | 44.13 | -0.15 | no | neg_sales, low_roce |
| 103 | Gallantt Ispat | -11.67 | -4.00 | 19.20 | 65.69 | -0.22 | no | neg_profit, neg_sales |
| 104 | Electronics Mart | -3.40 | 7.46 | 10.35 | 36.41 | -1.79 | no | neg_profit, low_roce |
| 105 | Vardhman Textile | -21.02 | 1.62 | 10.83 | 41.55 | -2.85 | no | neg_profit, low_roce |
| 106 | Karnataka Bank | 2.54 | -1.02 | 6.33 | 47.55 | -3.75 | no | neg_sales, low_roce |
| 107 | Garware Hi Tech | -8.29 | -1.64 | 20.57 | 32.74 | -4.18 | no | neg_profit, neg_sales |
| 108 | Praj Industries | -77.06 | -1.35 | 17.92 | 40.74 | -6.15 | no | neg_profit, neg_sales |
| 109 | Neogen Chemicals | -63.14 | 9.23 | 8.82 | 34.61 | -6.67 | no | neg_profit, low_roce |
| 110 | Gujarat Alkalies | -77.65 | 1.46 | -0.34 | 75.67 | -9.64 | no | neg_profit, neg_roce |
| 111 | Shanti Educat. | -131.28 | -71.63 | 14.11 | 39.86 | -20.18 | no | neg_profit, neg_sales, low_roce |
| 112 | Jindal Poly Film | -453.42 | -68.66 | 5.36 | 85.00 | -21.84 | no | neg_profit, neg_sales, low_roce |
| 113 | OneSource Speci. | -417.62 | -26.04 | 5.53 | 45.51 | -24.99 | no | neg_profit, neg_sales, low_roce |
