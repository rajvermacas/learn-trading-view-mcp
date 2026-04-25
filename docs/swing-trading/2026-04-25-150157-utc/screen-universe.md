# Screen Universe — 2026-04-25

## Screen Details

- **URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Title**: Return over 3 months
- **Filter**: Return over 3 months > 30 AND Market Capitalization > 3000
- **Pages fetched**: 5 (25 stocks per page)
- **Total parsed**: 125 stocks
- **Deduplication**: None needed (sequential S.No. 1–125)

## Fixed Visible Screen Schema

### Scoring Columns (used for PreRankScore)

| Column | Weight | Direction |
|--------|--------|-----------|
| Qtr Profit Var % | 0.35 | Higher is better |
| Qtr Sales Var % | 0.35 | Higher is better |
| ROCE % | 0.20 | Higher is better |
| 3mth return % | 0.10 | Higher is better |

### Context-Only Columns (not used for PreRankScore)

- CMP Rs.
- P/E
- Mar Cap Rs.Cr.
- Div Yld %
- NP Qtr Rs.Cr.
- Sales Qtr Rs.Cr.

## Pre-Rank Soft Penalties

- Qtr Profit Var % <= 0: subtract 12
- Qtr Sales Var % <= 0: subtract 12
- ROCE % < 15: subtract 8
- 3mth return % <= 0: subtract 8
- ROCE % < 0: contribution = 0, subtract 12

## Working Universe (Top 20 by Adjusted PreRankScore)

| PreRank | Name | QPV% | QSV% | ROCE% | 3M% | AdjScore | Penalties | In Working Universe |
|---------|------|------|------|-------|-----|----------|-----------|---------------------|
| 1 | Quality Power El | 169.18 | 291.22 | 26.60 | 133.49 | 89.69 | none | Yes |
| 2 | Atlanta Electric | 125.33 | 79.71 | 50.20 | 144.20 | 89.43 | none | Yes |
| 3 | Lloyds Metals | 169.05 | 201.94 | 38.28 | 52.00 | 89.31 | none | Yes |
| 4 | GE Vernova T&D | 138.53 | 58.40 | 54.74 | 69.51 | 86.30 | none | Yes |
| 5 | Insolation Ener | 173.57 | 77.05 | 34.73 | 46.63 | 85.48 | none | Yes |
| 6 | Fujiyama Power | 124.29 | 73.80 | 38.88 | 46.78 | 83.06 | none | Yes |
| 7 | Engineers India | 219.30 | 58.29 | 25.01 | 45.31 | 80.49 | none | Yes |
| 8 | Websol Energy | 64.00 | 77.19 | 59.25 | 48.23 | 79.86 | none | Yes |
| 9 | Diamond Power | 692.98 | 54.21 | 31.05 | — | 79.06 | none | Yes (3M missing) |
| 10 | Cupid | 196.66 | 105.67 | 17.10 | 42.36 | 78.68 | none | Yes |
| 11 | Billionbrains | 122.06 | 87.93 | 37.38 | 30.15 | 77.82 | none | Yes |
| 12 | Krishana Phosch. | 152.83 | 59.76 | 27.24 | 31.71 | 76.62 | none | Yes |
| 13 | Sky Gold & Diam. | 120.42 | 77.13 | 21.21 | 36.83 | 74.17 | none | Yes |
| 14 | Prec. Wires (I) | 98.94 | 37.19 | 26.78 | 81.61 | 72.61 | none | Yes |
| 15 | Acutaas Chemical | 140.18 | 42.98 | 19.92 | 44.85 | 72.38 | none | Yes |
| 16 | Aditya Infotech | 138.82 | 37.32 | 19.49 | 62.95 | 72.34 | none | Yes |
| 17 | Rubicon Research | 91.23 | 51.73 | 26.05 | 44.40 | 72.00 | none | Yes |
| 18 | Sharda Cropchem | 365.87 | 38.68 | 16.50 | 37.61 | 70.63 | none | Yes |
| 19 | Bajaj Consumer | 105.29 | 30.41 | 30.60 | 48.27 | 69.60 | none | Yes |
| 20 | KRN Heat Exchan | 65.04 | 37.46 | 20.75 | 108.61 | 68.29 | none | Yes |

## Excluded from Working Universe (Ranks 21–125)

| PreRank | Name | AdjScore | Penalties | Flags |
|---------|------|----------|-----------|-------|
| 21 | GNG Electronics | 68.04 | none | — |
| 22 | Hitachi Energy | 67.83 | none | — |
| 23 | Hind Rectifiers | 66.19 | none | — |
| 24 | Siemens Ener.Ind | 65.94 | none | — |
| 25 | Data Pattern | 65.76 | none | — |
| 26 | Shilchar Tech. | 65.53 | none | — |
| 27 | Sambhv Steel | 64.58 | none | — |
| 28 | AXISCADES Tech. | 63.96 | none | — |
| 29 | Ram Ratna Wires | 63.66 | none | — |
| 30 | Kirloskar Oil | 62.85 | none | — |
| — | _(95 more stocks below rank 30)_ | — | — | — |

Note: Stocks 113–125 from page 5 had partially garbled data extraction. Stocks 114, 117–122 had ROCE values > 200% which were treated as column-shifted/distorted and zeroed. Stocks 113–125 had missing 3-month return values, scored as zero contribution.
