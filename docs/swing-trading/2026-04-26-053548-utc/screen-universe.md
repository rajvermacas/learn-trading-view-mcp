# Screen Universe — 2026-04-26

## Screen Details

- **URL:** https://www.screener.in/screens/3474384/return-over-3-months
- **Query:** `Return over 3months > 30 AND Market Capitalization > 3000`
- **Additional filter:** Only companies with Mar 2026 results
- **Total parsed:** 125 stocks across 5 pages
- **Deduplication:** None required (no duplicates found)
- **Pre-rank cap:** 20 (user-specified)

## Fixed Visible Screen Schema

### Scoring Columns (contribute to PreRankScore)

| Column | Weight | Direction |
|---|---|---|
| Qtr Profit Var % | 0.35 | Higher is better |
| Qtr Sales Var % | 0.35 | Higher is better |
| ROCE % | 0.20 | Higher is better |
| 3mth return % | 0.10 | Higher is better |

### Context-Only Columns (do not contribute to PreRankScore)

CMP Rs., P/E, Mar Cap Rs.Cr., Div Yld %, NP Qtr Rs.Cr., Sales Qtr Rs.Cr.

## Soft Penalties Applied

- QPV <= 0: −12
- QSV <= 0: −12
- ROCE < 15: −8
- ROCE < 0: −12 (ROCE contribution also zeroed)
- 3mth return <= 0: −8

## Top 20 Working Universe (sorted by AdjPreRankScore)

| # | Symbol | Name | QPV% | QSV% | ROCE% | 3mR% | RawScore | AdjScore | In Working Universe | Penalties |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | QPOWER | Quality Power El | 169.2 | 291.2 | 26.6 | 133.5 | 90.1 | 90.1 | Yes | — |
| 2 | LLOYDSME | Lloyds Metals | 169.1 | 201.9 | 38.3 | 52.0 | 89.6 | 89.6 | Yes | — |
| 3 | ATLANTAELE | Atlanta Electric | 125.3 | 79.7 | 50.2 | 144.2 | 89.5 | 89.5 | Yes | — |
| 4 | GVT&D | GE Vernova T&D | 138.5 | 58.4 | 54.7 | 69.5 | 86.2 | 86.2 | Yes | — |
| 5 | INSOLATION | Insolation Ener | 173.6 | 77.0 | 34.7 | 46.6 | 85.6 | 85.6 | Yes | — |
| 6 | UTLSOLAR | Fujiyama Power | 124.3 | 73.8 | 38.9 | 46.8 | 82.9 | 82.9 | Yes | — |
| 7 | ENGINERSIN | Engineers India | 219.3 | 58.3 | 25.0 | 45.3 | 80.7 | 80.7 | Yes | — |
| 8 | WEBELSOLAR | Websol Energy | 64.0 | 77.2 | 59.2 | 48.2 | 79.8 | 79.8 | Yes | — |
| 9 | DIACABS | Diamond Power | 693.0 | 54.2 | 31.1 | N/A | 79.2 | 79.2 | Yes | 3mth missing |
| 10 | CUPID | Cupid | 196.7 | 105.7 | 17.1 | 42.4 | 79.1 | 79.1 | Yes | — |
| 11 | GROWW | Billionbrains | 122.1 | 87.9 | 37.4 | 30.1 | 78.0 | 78.0 | Yes | — |
| 12 | KRISHANA | Krishana Phosch. | 152.8 | 59.8 | 27.2 | 31.7 | 76.8 | 76.8 | Yes | — |
| 13 | SKYGOLD | Sky Gold & Diam. | 120.4 | 77.1 | 21.2 | 36.8 | 74.5 | 74.5 | Yes | — |
| 14 | PRECWIRE | Prec. Wires (I) | 98.9 | 37.2 | 26.8 | 81.6 | 72.3 | 72.3 | Yes | — |
| 15 | RUBICON | Rubicon Research | 91.2 | 51.7 | 26.1 | 44.4 | 72.3 | 72.3 | Yes | — |
| 16 | ACUTAAS | Acutaas Chemical | 140.2 | 43.0 | 19.9 | 44.9 | 72.2 | 72.2 | Yes | — |
| 17 | CPPLUS | Aditya Infotech | 138.8 | 37.3 | 19.5 | 63.0 | 72.2 | 72.2 | Yes | — |
| 18 | SHARDACROP | Sharda Cropchem | 365.9 | 38.7 | 16.5 | 37.6 | 70.5 | 70.5 | Yes | — |
| 19 | BAJAJCON | Bajaj Consumer | 105.3 | 30.4 | 30.6 | 48.3 | 69.3 | 69.3 | Yes | — |
| 20 | KRN | KRN Heat Exchan | 65.0 | 37.5 | 20.8 | 108.6 | 68.2 | 68.2 | Yes | — |

## Below Pre-Rank Cut (ranks 21–30, next tier)

| # | Symbol | Name | AdjScore | Penalties |
|---|---|---|---|---|
| 21 | EBGNG | GNG Electronics | 67.9 | — |
| 22 | POWERINDIA | Hitachi Energy | 67.8 | — |
| 23 | SEAMECLTD | SEAMEC Ltd | 66.1 | ROCE<15 |
| 24 | HIRECT | Hind Rectifiers | 65.7 | — |
| 25 | MTARTECH | MTAR Technologies | 65.5 | ROCE<15 |
| 26 | SYRMA | Syrma SGS Tech | 65.3 | ROCE<15 |
| 27 | SAMBHV | Sambhv Steel | 64.6 | ROCE<15 |
| 28 | ENRIN | Siemens Ener.Ind | 64.6 | — |
| 29 | AXISCADES | AXISCADES Tech | 64.1 | ROCE<15 |
| 30 | DATAPATTNS | Data Pattern | 63.0 | — |

## Stocks with Scoring Issues (page 5, rows 113–125)

Stocks 113–125 from page 5 had missing 3-month return data (shown as "—" on Screener). Their 3mth return percentile contribution was set to 0 per the methodology. Stocks with shifted/garbled column data had values parsed as-is where numeric; non-numeric values received zero percentile contribution.

Notable: **Diamond Power** (DIACABS) ranked #9 in pre-rank despite missing 3mth return because its QPV of 693% and QSV of 54.2% scored very high on the two heaviest-weighted columns.

## Full Universe Size Breakdown

| Page | Stocks | Range |
|---|---|---|
| Page 1 | 25 | S.No. 1–25 |
| Page 2 | 25 | S.No. 26–50 |
| Page 3 | 25 | S.No. 51–75 |
| Page 4 | 25 | S.No. 76–100 |
| Page 5 | 25 | S.No. 101–125 |
| **Total** | **125** | All parsed, deduplicated |
