# Screen Universe — 2026-04-21

## Screen

- **URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Title:** "Return over 3 months" by Mrinal
- **Filters:** Return over 3months > 30% AND Market Capitalization > 3000 Cr
- **Pages fetched:** 5 (25 stocks per page)
- **Total parsed:** 118 stocks
- **Deduplication:** None needed (no duplicates found)
- **Pre-rank cap:** 20 (user-specified)

## Fixed Visible Screen Schema

### Scoring Columns (contribute to PreRankScore)

| Column | Weight | Direction |
|--------|--------|-----------|
| Qtr Profit Var % | 0.35 | Higher-is-better |
| Qtr Sales Var % | 0.35 | Higher-is-better |
| ROCE % | 0.20 | Higher-is-better |
| 3mth return % | 0.10 | Higher-is-better |

### Context-Only Columns (do not contribute to PreRankScore)

| Column |
|--------|
| CMP Rs. |
| P/E |
| Mar Cap Rs.Cr. |
| Div Yld % |
| NP Qtr Rs.Cr. |
| Sales Qtr Rs.Cr. |

## Soft Penalties

| Condition | Deduction |
|-----------|-----------|
| Qtr Profit Var % ≤ 0 | -12 |
| Qtr Sales Var % ≤ 0 | -12 |
| ROCE % < 15 | -8 |
| ROCE % < 0 | -12 (additional) |
| 3mth return % ≤ 0 | -8 |

## Full Universe with PreRankScore

| PreRank | Symbol | Name | Score | QPV% | QSV% | ROCE% | 3mR% | In Working Universe | Penalty Flags |
|---------|--------|------|-------|------|------|-------|------|-------------------|---------------|
| 1 | QPOWER | Quality Power El | 89.86 | 169.18 | 291.22 | 26.60 | 91.84 | Yes | — |
| 2 | LLOYDSME | Lloyds Metals | 88.67 | 169.05 | 201.94 | 38.28 | 44.45 | Yes | — |
| 3 | ATLANTAELE | Atlanta Electric | 86.24 | 125.33 | 79.71 | 50.20 | 83.21 | Yes | — |
| 4 | WAAREEENER | Waaree Energies | 86.01 | 158.06 | 118.81 | 34.94 | 43.56 | Yes | — |
| 5 | INSOLATION | Insolation Ener | 84.20 | 173.57 | 77.05 | 34.73 | 41.13 | Yes | — |
| 6 | GVT&D | GE Vernova T&D | 83.56 | 138.53 | 58.40 | 54.74 | 66.24 | Yes | — |
| 7 | SAATVIKGL | Saatvik Green | 82.40 | 144.05 | 142.58 | 52.33 | 31.36 | Yes | — |
| 8 | BSE | BSE | 81.74 | 175.79 | 61.97 | 46.57 | 33.74 | Yes | — |
| 9 | ORIANA | Oriana Power | 81.30 | 149.88 | 117.27 | 42.31 | 30.53 | Yes | — |
| 10 | EMMVEE | Emmvee Photovol. | 80.79 | 165.77 | 118.11 | 28.01 | 33.77 | Yes | — |
| 11 | CUPID | Cupid | 79.39 | 196.66 | 105.67 | 17.10 | 45.94 | Yes | — |
| 12 | ENGINERSIN | Engineers India | 77.27 | 219.30 | 58.29 | 25.01 | 36.23 | Yes | — |
| 13 | GROWW | Billionbrains | 76.59 | 122.06 | 87.93 | 37.38 | 32.70 | Yes | — |
| 14 | KRISHANA | Krishana Phosch. | 75.09 | 152.83 | 59.76 | 27.24 | 32.56 | Yes | — |
| 15 | MANORAMA | Manorama Indust. | 72.22 | 131.09 | 73.30 | 23.03 | 32.74 | Yes | — |
| 16 | ACUTAAS | Acutaas Chemical | 70.46 | 140.18 | 42.98 | 19.92 | 48.17 | Yes | — |
| 17 | BAJAJCON | Bajaj Consumer | 70.28 | 105.29 | 30.41 | 30.60 | 85.45 | Yes | — |
| 18 | PRECWIRE | Prec. Wires (I) | 69.78 | 98.94 | 37.19 | 26.78 | 76.65 | Yes | — |
| 19 | SHARDACROP | Sharda Cropchem | 69.58 | 365.87 | 38.68 | 16.50 | 37.98 | Yes | — |
| 20 | RUBICON | Rubicon Research | 69.42 | 91.23 | 51.73 | 26.05 | 39.73 | Yes | — |
| 21 | CPPLUS | Aditya Infotech | 68.85 | 138.82 | 37.32 | 19.49 | 64.05 | No | — |
| 22 | EBGNG | GNG Electronics | 66.35 | 102.78 | 40.26 | 19.84 | 62.52 | No | — |
| 23 | KRN | KRN Heat Exchan | 65.88 | 65.04 | 37.46 | 20.75 | 95.39 | No | — |
| 24 | SEAMECLTD | SEAMEC Ltd | 65.84 | 3100.60 | 112.30 | 8.60 | 39.14 | No | low_roce |
| 25 | RRWL | Ram Ratna Wires | 64.91 | 106.33 | 43.80 | 20.17 | 38.35 | No | — |
| 26 | POWERINDIA | Hitachi Energy | 64.31 | 119.97 | 28.51 | 19.44 | 79.10 | No | — |
| 27 | HIRECT | Hind Rectifiers | 63.11 | 47.85 | 44.00 | 21.60 | 43.41 | No | — |
| 28 | ENRIN | Siemens Ener.Ind | 62.43 | 51.67 | 25.97 | 67.75 | 42.53 | No | — |
| 29 | DATAPATTNS | Data Pattern | 62.17 | 35.76 | 47.92 | 21.00 | 59.23 | No | — |
| 30 | MTARTECH | MTAR Technologie | 61.82 | 131.84 | 59.30 | 10.51 | 108.06 | No | low_roce |
| 31 | SAMBHV | Sambhv Steel | 58.77 | 112.79 | 59.64 | 13.92 | 42.80 | No | low_roce |
| 32 | VOLTAMP | Volt.Transform. | 58.71 | 34.99 | 30.36 | 29.11 | 55.26 | No | — |
| 33 | SGFIN | SG Finserve | 56.43 | 77.68 | 94.88 | 9.32 | 49.52 | No | low_roce |
| 34 | TDPOWERSYS | TD Power Systems | 55.40 | 25.35 | 26.36 | 30.35 | 60.20 | No | — |
| 35 | SYRMA | Syrma SGS Tech. | 55.28 | 108.80 | 45.36 | 11.67 | 54.02 | No | low_roce |
| 36 | PFOCUS | Prime Focus | 54.96 | 237.06 | 32.74 | 7.95 | 49.77 | No | low_roce |
| 37 | TRIL | T R I L | 54.76 | 34.89 | 31.71 | 27.97 | 36.94 | No | — |
| 38 | RASHI | Rashi Peripheral | 53.15 | 131.00 | 42.60 | 14.19 | 34.68 | No | low_roce |
| 39 | INOXINDIA | Inox India | 52.98 | 26.34 | 28.45 | 37.98 | 34.12 | No | — |
| 40 | CGPOWER | CG Power & Ind | 52.20 | 18.42 | 26.22 | 37.48 | 39.97 | No | — |
| — | *(78 more stocks below rank 40 — not shown for brevity)* | | | | | | | No | Various |

**Note:** Full 118-stock PreRankScore data was computed and used for selection. Stocks ranked 41–118 are omitted from this table for readability. The complete data is preserved in `scripts/full_universe.json`.
