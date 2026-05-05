# Screen Universe — 2026-05-05

## Source

- URL: https://www.screener.in/screens/3474384/return-over-3-months
- Pages fetched: 4 (25+25+25+17 = 92 stocks)
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

## Pre-Ranked Working Universe (Top 20 of 92)

| Rank | Name | AdjScore | Penalties | In Working Universe |
|------|------|----------|-----------|---------------------|
| 1 | Websol Energy | 88.41 | none | YES |
| 2 | Quality Power El | 86.81 | none | YES |
| 3 | Atlanta Electric | 86.13 | none | YES |
| 4 | Lloyds Metals | 84.98 | none | YES |
| 5 | Indiabulls | 84.29 | none | YES |
| 6 | Cupid | 79.53 | none | YES |
| 7 | Insolation Ener | 79.18 | none | YES |
| 8 | Engineers India | 78.50 | none | YES |
| 9 | Fujiyama Power | 76.59 | none | YES |
| 10 | Billionbrains | 75.02 | none | YES |
| 11 | Sky Gold & Diam. | 73.41 | none | YES |
| 12 | GNG Electronics | 73.20 | none | YES |
| 13 | GE Vernova T&D | 72.96 | none | YES |
| 14 | Krishana Phosch. | 72.60 | none | YES |
| 15 | HFCL | 72.23 | ROCE<15 | YES |
| 16 | Aditya Infotech | 68.34 | none | YES |
| 17 | DEE Development | 67.72 | ROCE<15 | YES |
| 18 | Prec. Wires (I) | 66.77 | none | YES |
| 19 | Timex Group | 65.35 | none | YES |
| 20 | Acutaas Chemical | 64.96 | none | YES |

## Full Universe (All 92 Stocks)

### Page 1 (Stocks 1-25)

| S.No | Name | In Working Universe |
|------|------|---------------------|
| 1 | Websol Energy | YES (Rank 1) |
| 2 | GE Vernova T&D | YES (Rank 13) |
| 3 | Atlanta Electric | YES (Rank 3) |
| 4 | Timex Group | YES (Rank 19) |
| 5 | Premier Energies | NO |
| 6 | Schneider Elect. | NO |
| 7 | Fujiyama Power | YES (Rank 9) |
| 8 | Lloyds Metals | YES (Rank 4) |
| 9 | Inox India | NO |
| 10 | Billionbrains | YES (Rank 10) |
| 11 | Insolation Ener | YES (Rank 7) |
| 12 | Gokul Agro | NO |
| 13 | Cemindia Project | NO |
| 14 | Natco Pharma | NO |
| 15 | Apar Inds. | NO |
| 16 | Acutaas Chemical | YES (Rank 20) |
| 17 | Bajaj Consumer | NO |
| 18 | Kirl.Pneumatic | NO |
| 19 | TD Power Systems | NO |
| 20 | Black Box | NO |
| 21 | Krishana Phosch. | YES (Rank 14) |
| 22 | Prec. Wires | YES (Rank 18) |
| 23 | Quality Power El | YES (Rank 2) |
| 24 | Engineers India | YES (Rank 8) |
| 25 | Volt.Transform. | NO |

### Page 2 (Stocks 26-50)

| S.No | Name | In Working Universe |
|------|------|---------------------|
| 26 | Aeroflex | NO |
| 27 | Himadri Special | NO |
| 28 | AGI Infra | NO |
| 29 | Hind Rectifiers | NO |
| 30 | Ratnamani Metals | NO |
| 31 | KSH Internationa | NO |
| 32 | Welspun Corp | NO |
| 33 | Sky Gold & Diam. | YES (Rank 11) |
| 34 | Data Pattern | NO |
| 35 | KRN Heat Exchan | NO |
| 36 | Jayaswal Neco | NO |
| 37 | Park Medi World | NO |
| 38 | GNG Electronics | YES (Rank 12) |
| 39 | Ram Ratna Wires | NO |
| 40 | Aditya Infotech | YES (Rank 16) |
| 41 | Hitachi Energy | NO |
| 42 | M B Agro Prod. | NO |
| 43 | Gallantt Ispat | NO |
| 44 | Praj Industries | NO |
| 45 | Finolex Cables | NO |
| 46 | Kennametal India | NO |
| 47 | Adani Power | NO |
| 48 | Cupid | YES (Rank 6) |
| 49 | Thermax | NO |
| 50 | Indiabulls | YES (Rank 5) |

### Page 3 (Stocks 51-75)

| S.No | Name | In Working Universe |
|------|------|---------------------|
| 51 | Wheels India | NO |
| 52 | Man Industries | NO |
| 53 | Epigral | NO |
| 54 | ISGEC Heavy | NO |
| 55 | Sai Life | NO |
| 56 | Yatharth Hospit. | NO |
| 57 | Sambhv Steel | NO |
| 58 | AXISCADES Tech. | NO |
| 59 | Kirloskar Oil | NO |
| 60 | Sansera Enginee. | NO |
| 61 | Paisalo Digital | NO |
| 62 | Lux Industries | NO |
| 63 | Azad Engineering | NO |
| 64 | Aster DM Health. | NO |
| 65 | HFCL | YES (Rank 15) |
| 66 | MTAR Technologie | NO |
| 67 | SG Mart | NO |
| 68 | S C I | NO |
| 69 | Adani Energy Sol | NO |
| 70 | Dalmia Bharat | NO |
| 71 | DEE Development | YES (Rank 17) |
| 72 | SG Finserve | NO |
| 73 | Dynamatic Tech. | NO |
| 74 | Sigma Advanced | NO |
| 75 | Universal Cables | NO |

### Page 4 (Stocks 76-92)

| S.No | Name | In Working Universe |
|------|------|---------------------|
| 76 | B H E L | NO |
| 77 | Shilpa Medicare | NO |
| 78 | Sterlite Tech. | NO |
| 79 | Adani Green | NO |
| 80 | CIAN Agro | NO |
| 81 | Bandhan Bank | NO |
| 82 | Karnataka Bank | NO |
| 83 | GE Power | NO |
| 84 | OneSource Speci. | NO |
| 85 | Jindal Poly Film | NO |
| 86 | Shadowfax Tech | NO |
| 87 | Sunflag Iron | NO |
| 88 | Aequs | NO |
| 89 | Gujarat Alkalies | NO |
| 90 | Ideaforge Tech | NO |
| 91 | Meesho | NO |
| 92 | Ather Energy | NO |

## Stocks Below the Cut (Ranks 21-92)

72 stocks did NOT make the working universe. They scored below the rank-20 cutoff (64.96 AdjScore) or carried penalties that pushed them below the top-20 threshold. Notable exclusions include:

- **Premier Energies, Schneider Elect., Inox India** — strong companies but lower QPV/QSV percentile in this universe
- **Hitachi Energy, Ratnamani Metals, Thermax** — quality names but insufficient recent-quarter growth acceleration
- **Adani Power, Adani Green, Adani Energy Sol** — large caps but lower ROCE/QPV scores
- **Gujarat Alkalies, Ideaforge Tech, Meesho, Ather Energy** — ROCE<0 penalties applied
- **Gallantt Ispat, Praj Industries** — QPV<=0 or QSV<=0 penalties

## Missing/Distorted Data Flags

| Stock | Flag |
|-------|------|
| Gujarat Alkalies | ROCE negative — contribution zeroed, -12 extra penalty |
| Ideaforge Tech | ROCE negative — contribution zeroed, -12 extra penalty |
| Meesho | ROCE negative — contribution zeroed, -12 extra penalty |
| Ather Energy | ROCE negative — contribution zeroed, -12 extra penalty |
