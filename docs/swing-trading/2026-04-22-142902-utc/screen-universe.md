# Screen Universe — Swing Trading 3% Screen

*Run Date: 2026-04-22 | Screen: Return over 3 months (>30%, MCap >₹3,000 Cr)*
*Source: https://www.screener.in/screens/3474384/return-over-3-months*

## Pagination & Deduplication

- **Total pages fetched**: 5 (25 stocks per page, 15 on page 5)
- **Total rows parsed**: 115
- **Duplicates found**: 0
- **Final universe size**: 115

## Fixed Visible Screen Schema

### Scoring Columns (used for PreRankScore)
1. `Qtr Profit Var %` — weight 0.35
2. `Qtr Sales Var %` — weight 0.35
3. `ROCE %` — weight 0.20
4. `3mth return %` — weight 0.10

### Context-Only Columns (not used for PreRankScore)
1. `CMP Rs.`
2. `P/E`
3. `Mar Cap Rs.Cr.`
4. `Div Yld %`
5. `NP Qtr Rs.Cr.`
6. `Sales Qtr Rs.Cr.`

## PreRankScore Formula

`PreRankScore = 0.35 × rank(QPV) + 0.35 × rank(QSV) + 0.20 × rank(ROCE) + 0.10 × rank(3mRet)`

Soft Penalties: QPV≤0: -12 | QSV≤0: -12 | ROCE<15: -8 | ROCE<0: -12 | 3mRet≤0: -8

## Working Universe (Top 20 by Adjusted PreRankScore)

| PreRank | Symbol | Company | Adj Score | QPV% | QSV% | ROCE% | 3mRet% | Penalties | In Universe |
|---------|--------|---------|-----------|------|------|-------|--------|-----------|-------------|
| 1 | QPOWER | Quality Power El | 91.02 | 169.18 | 291.22 | 26.60 | 90.97 | — | YES |
| 2 | ATLANTAELE | Atlanta Electric | 89.66 | 125.33 | 79.71 | 50.20 | 97.54 | — | YES |
| 3 | LLOYDSME | Lloyds Metals | 89.63 | 169.05 | 201.94 | 38.28 | 45.78 | — | YES |
| 4 | INSOLATION | Insolation Energy | 87.33 | 173.57 | 77.05 | 34.73 | 48.43 | — | YES |
| 5 | GVT&D | GE Vernova T&D | 85.78 | 138.53 | 58.40 | 54.74 | 59.95 | — | YES |
| 6 | ENGINERSIN | Engineers India | 80.74 | 219.30 | 58.29 | 25.01 | 39.27 | — | YES |
| 7 | GROWW | Billionbrains | 79.35 | 122.06 | 87.93 | 37.38 | 31.08 | — | YES |
| 8 | CUPID | Cupid Ltd | 78.75 | 196.66 | 105.67 | 17.10 | 37.66 | — | YES |
| 9 | KRISHANA | Krishana Phosch. | 77.57 | 152.83 | 59.76 | 27.24 | 30.47 | — | YES |
| 10 | MANORAMA | Manorama Indust. | 77.39 | 131.09 | 73.30 | 23.03 | 35.29 | — | YES |
| 11 | SKYGOLD | Sky Gold & Diam. | 74.74 | 120.42 | 77.13 | 21.21 | 34.53 | — | YES |
| 12 | ACUTAAS | Acutaas Chemical | 73.55 | 140.18 | 42.98 | 19.92 | 47.36 | — | YES |
| 13 | PRECWIRE | Precision Wires | 73.20 | 98.94 | 37.19 | 26.78 | 79.16 | — | YES |
| 14 | RUBICON | Rubicon Research | 73.06 | 91.23 | 51.73 | 26.05 | 40.53 | — | YES |
| 15 | BAJAJCON | Bajaj Consumer | 71.62 | 105.29 | 30.41 | 30.60 | 58.13 | — | YES |
| 16 | CPPLUS | Aditya Infotech | 71.27 | 138.82 | 37.32 | 19.49 | 52.68 | — | YES |
| 17 | SHARDACROP | Sharda Cropchem | 71.16 | 365.87 | 38.68 | 16.50 | 38.74 | — | YES |
| 18 | KRN | KRN Heat Exchan | 68.91 | 65.04 | 37.46 | 20.75 | 96.05 | — | YES |
| 19 | POWERINDIA | Hitachi Energy | 67.71 | 119.97 | 28.51 | 19.44 | 80.06 | — | YES |
| 20 | HIRECT | Hind Rectifiers | 67.29 | 47.85 | 44.00 | 21.60 | 49.16 | — | YES |

## Stocks Below Pre-Rank Cut (21–115)

| PreRank | Symbol | Adj Score | In Universe | Key Penalties |
|---------|--------|-----------|-------------|---------------|
| 21 | EBGNG | 66.18 | NO | — |
| 22 | ENRIN | 65.65 | NO | — |
| 23 | SEAMECLTD | 65.47 | NO | ROCE<15:-8 |
| 24 | DATAPATTNS | 65.43 | NO | — |
| 25 | MTARTECH | 65.02 | NO | ROCE<15:-8 |
| 26 | RRWL | 64.24 | NO | — |
| 27 | VOLTAMP | 61.90 | NO | — |
| 28 | SAMBHV | 60.39 | NO | ROCE<15:-8 |
| 29 | TDPOWERSYS | 58.92 | NO | — |
| 30 | INOXINDIA | 58.84 | NO | — |
| 31 | SYRMA | 57.10 | NO | ROCE<15:-8 |
| 32 | SGFIN | 56.92 | NO | ROCE<15:-8 |
| 33 | RASHI | 56.31 | NO | ROCE<15:-8 |
| 34 | CGPOWER | 55.87 | NO | — |
| 35 | DYNAMATECH | 55.35 | NO | ROCE<15:-8 |
| 36 | PFOCUS | 54.69 | NO | ROCE<15:-8 |
| 37 | MAHLOG | 54.52 | NO | — |
| 38 | SCHNEIDER | 53.63 | NO | — |
| 39 | GOKULAGRO | 53.15 | NO | — |
| 40 | SCI | 51.86 | NO | ROCE<15:-8 |
| 41 | AXISCADES | 51.72 | NO | ROCE<15:-8 |
| 42 | PREMIERENE | 51.66 | NO | — |
| 43 | APARINDS | 51.63 | NO | — |
| 44 | GEPOWER | 51.55 | NO | ROCE<15:-8 |
| 45 | ZENTECH | 50.92 | NO | — |
| 46 | SHILCTECH | 50.90 | NO | — |
| 47 | KIRLOSENG | 50.08 | NO | ROCE<15:-8 |
| 48 | TECHNOE | 49.91 | NO | — |
| 49 | MANINDS | 49.58 | NO | — |
| 50 | SKIPPER | 49.57 | NO | — |
| 51–60 | *various* | 48.60–43.57 | NO | Mixed penalties |
| 61–70 | *various* | 43.43–41.39 | NO | Mixed penalties |
| 71–80 | *various* | 39.63–36.33 | NO | Mixed penalties |
| 81–90 | *various* | 34.23–21.06 | NO | QPV/QSV/ROCE penalties |
| 91–100 | *various* | 17.83–3.77 | NO | Multiple penalties |
| 101–115 | *various* | 3.76 to -21.54 | NO | Heavy penalties (QPV+QSV+ROCE) |

*Full 115-stock detail was computed programmatically. The complete ranked list with individual penalty flags is available in the pre-rank computation log.*
