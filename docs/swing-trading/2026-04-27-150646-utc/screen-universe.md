# Screen Universe — 2026-04-27

**Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months
**Filter:** Return over 3 months > 30 AND Market Capitalization > 3000
**Total Parsed:** 151 stocks across 7 pages (25 per page, 1 on page 7)
**Deduplication:** No duplicates found
**Pre-Rank Cap:** 20 (user-specified)

## Fixed Visible Screen Schema

### Scoring Columns (contribute to PreRankScore)
- `Qtr Profit Var %` (weight 0.35)
- `Qtr Sales Var %` (weight 0.35)
- `ROCE %` (weight 0.20)
- `3mth return %` (weight 0.10)

### Context-Only Columns (no PreRankScore contribution)
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

## Top 20 Working Universe (sorted by Adjusted PreRankScore)

| Rank | Symbol | Company | AdjScore | QPV% | QSV% | ROCE% | 3mRet% | Penalties | In Working Universe |
|------|--------|---------|----------|------|------|-------|--------|-----------|-------------------|
| 1 | LLOYDSME | Lloyds Metals | 91.28 | 169.05 | 201.94 | 38.28 | 57.21 | none | Yes |
| 2 | QPOWER | Quality Power El | 91.17 | 169.18 | 291.22 | 26.60 | 135.04 | none | Yes |
| 3 | ATLANTAELE | Atlanta Electric | 90.33 | 125.33 | 79.71 | 50.20 | 149.98 | none | Yes |
| 4 | INA | Insolation Ener | 87.43 | 173.57 | 77.05 | 34.73 | 49.49 | none | Yes |
| 5 | GVT&D | GE Vernova T&D | 86.64 | 138.53 | 58.40 | 54.74 | 66.86 | none | Yes |
| 6 | ORIANA | Oriana Power | 86.12 | 149.88 | 117.27 | 42.31 | 36.89 | none | Yes |
| 7 | SAATVIKGL | Saatvik Green | 85.41 | 144.05 | 142.58 | 52.33 | 33.83 | none | Yes |
| 8 | UTLSOLAR | Fujiyama Power | 84.57 | 124.29 | 73.80 | 38.88 | 51.94 | none | Yes |
| 9 | ENGINERSIN | Engineers India | 83.46 | 219.30 | 58.29 | 25.01 | 56.50 | none | Yes |
| 10 | EMMVEE | Emmvee Photovol. | 82.93 | 165.77 | 118.11 | 28.01 | 35.34 | none | Yes |
| 11 | WEBELSOLAR | Websol Energy | 81.91 | 64.00 | 77.19 | 59.25 | 49.52 | none | Yes |
| 12 | KRISHANA | Krishana Phosch. | 81.61 | 152.83 | 59.76 | 27.24 | 46.33 | none | Yes |
| 13 | DIACABS | Diamond Power | 80.57 | 692.98 | 54.21 | 34.46 | — | RET_MISSING | Yes |
| 14 | CUPID | Cupid | 79.58 | 196.66 | 105.67 | 17.10 | 41.56 | none | Yes |
| 15 | PRECWIRE | Prec. Wires (I) | 74.85 | 98.94 | 37.19 | 26.78 | 80.23 | none | Yes |
| 16 | SKYGOLD | Sky Gold & Diam. | 74.82 | 120.42 | 77.13 | 21.21 | 34.03 | none | Yes |
| 17 | RUBICON | Rubicon Research | 74.27 | 91.23 | 51.73 | 26.05 | 46.50 | none | Yes |
| 18 | CPPLUS | Aditya Infotech | 74.07 | 138.82 | 37.32 | 19.49 | 69.88 | none | Yes |
| 19 | ACUTAAS | Acutaas Chemical | 72.40 | 140.18 | 42.98 | 19.92 | 44.36 | none | Yes |
| 20 | RAMRAT | Ram Ratna Wires | 71.40 | 106.33 | 43.80 | 20.17 | 49.46 | none | Yes |

## Stocks 21–30 (did not make working universe)

| Rank | Symbol | AdjScore | QPV% | QSV% | ROCE% | 3mRet% | Penalties |
|------|--------|----------|------|------|-------|--------|-----------|
| 21 | SHARDACROP | 70.86 | 365.87 | 38.68 | 16.50 | 35.47 | none |
| 22 | EBGNG | 70.82 | 102.78 | 40.26 | 19.84 | 58.81 | none |
| 23 | KRN | 70.42 | 65.04 | 37.46 | 20.75 | 121.47 | none |
| 24 | POWERINDIA | 69.84 | 119.97 | 28.51 | 19.44 | 91.90 | none |
| 25 | BAJAJCON | 69.69 | 105.29 | 30.41 | 30.60 | 41.06 | none |
| 26 | IBULLSLTD | 69.48 | 2250.95 | −8.90 | 54.94 | — | QSV<=0, RET_MISSING |
| 27 | SHILCTECH | 68.47 | 21.77 | 10.75 | 71.30 | 81.69 | none |
| 28 | ENRIN | 66.59 | 51.67 | 25.97 | 67.75 | 46.17 | none |
| 29 | KIRLPNU | 66.29 | 68.58 | 21.13 | 30.36 | 31.37 | none |
| 30 | PREMIERENE | 65.31 | 53.48 | 13.02 | 41.12 | 44.52 | none |

## Penalty Flag Legend

- **QPV<=0:** Qtr Profit Var % is zero or negative (−12 penalty)
- **QSV<=0:** Qtr Sales Var % is zero or negative (−12 penalty)
- **ROCE<15:** ROCE % below 15 (−8 penalty)
- **ROCE<0:** ROCE % negative (−12 penalty + zero contribution)
- **RET<=0:** 3-month return % zero or negative (−8 penalty)
- **RET_MISSING:** 3-month return % not available (zero contribution, no penalty)

## Notes

- All 20 working-universe stocks had zero penalty flags except DIACABS (RET_MISSING — 3mth return not displayed on screener page)
- PreRankScore uses percentile ranking within the full 151-stock universe for each scoring column
- Higher-is-better for all four scoring columns
- Percentile ranks computed only from valid numeric values; missing values get zero contribution
