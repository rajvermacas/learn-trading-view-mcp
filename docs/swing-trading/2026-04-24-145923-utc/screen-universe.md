# Screen Universe — Return over 3 months

**Screen URL**: https://www.screener.in/screens/3474384/return-over-3-months
**Filter**: Return over 3months > 30 AND Market Capitalization > 3000
**Run Date**: 2026-04-24
**Pages Fetched**: 1 of 5 (user-limited to page 1)
**Total Results**: 125 across 5 pages; 15 parsed from page 1

## Fixed Screen Schema

### Scoring Columns (contribute to PreRankScore)
- `Qtr Profit Var %` (weight 0.35)
- `Qtr Sales Var %` (weight 0.35)
- `ROCE %` (weight 0.20)
- `3mth return %` (weight 0.10)

### Context-Only Columns (do not contribute to PreRankScore)
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

## PreRankScore Formula

`PreRankScore = 0.35 × rank(Qtr Profit Var %) + 0.35 × rank(Qtr Sales Var %) + 0.20 × rank(ROCE %) + 0.10 × rank(3mth return %)`

### Soft Penalties Applied After Score
- Qtr Profit Var % ≤ 0 → subtract 12
- Qtr Sales Var % ≤ 0 → subtract 12
- ROCE % < 15 → subtract 8
- 3mth return % ≤ 0 → subtract 8

## Full Parsed Universe (15 stocks, page 1)

| Rank | Name | Symbol | CMP | P/E | MarCap Cr | DivYld% | NPQtr Cr | QPV% | SQtr Cr | QSV% | ROCE% | 3mth% | PreRankScore | Penalties | Adjusted | In Working Universe |
|------|------|--------|-----|-----|-----------|---------|----------|------|---------|------|-------|-------|-------------|-----------|----------|---------------------|
| 1 | Lloyds Metals | LLOYDSME | 1695.60 | 38.73 | 95397 | 0.06 | 1089.56 | 169.05 | 5058.08 | 201.94 | 38.28 | 52.00 | 84.00 | 0 | **84.00** | Yes |
| 2 | Atlanta Electric | ATLANTAELE | 1778.50 | 87.39 | 13647 | 0.00 | 49.42 | 125.33 | 471.82 | 79.71 | 50.20 | 144.20 | 83.99 | 0 | **83.99** | Yes |
| 3 | GE Vernova T&D | GVT&D | 4598.30 | 105.34 | 117722 | 0.11 | 290.80 | 138.53 | 1700.64 | 58.40 | 54.74 | 69.51 | 78.67 | 0 | **78.67** | Yes |
| 4 | Websol Energy | WEBELSOLAR | 110.85 | 20.98 | 4824 | 0.00 | 64.98 | 64.00 | 261.02 | 77.19 | 59.25 | 48.23 | 72.66 | 0 | 72.66 | No |
| 5 | Fujiyama Power | UTLSOLAR | 302.24 | 47.80 | 9256 | 0.00 | 67.31 | 124.29 | 588.48 | 73.80 | 38.88 | 46.78 | 65.67 | 0 | 65.67 | No |
| 6 | Billionbrains | GROWW | 218.02 | 65.69 | 136827 | 0.00 | 686.35 | 122.06 | 1505.37 | 87.93 | 37.38 | 30.15 | 62.34 | 0 | 62.34 | No |
| 7 | Siemens Ener.Ind | ENRIN | 3205.10 | 93.54 | 114106 | 0.12 | 312.90 | 51.67 | 1910.90 | 25.97 | 67.75 | 50.80 | 60.34 | 0 | 60.34 | No |
| 8 | Shilchar Tech. | SHILCTECH | 5016.30 | 30.95 | 5729 | 0.25 | 42.34 | 21.77 | 170.26 | 10.75 | 71.30 | 69.57 | 45.01 | 0 | 45.01 | No |
| 9 | Inox India | INOXINDIA | 1508.60 | 54.19 | 13703 | 0.13 | 60.70 | 26.34 | 428.56 | 28.45 | 37.98 | 37.81 | 43.66 | 0 | 43.66 | No |
| 10 | Premier Energies | PREMIERENE | 1007.55 | 34.36 | 45728 | 0.10 | 391.62 | 53.48 | 1936.46 | 13.02 | 41.12 | 47.50 | 43.34 | 0 | 43.34 | No |
| 11 | Schneider Elect. | SCHNEIDER | 1180.10 | 107.10 | 28025 | 0.00 | 97.03 | 16.65 | 1029.17 | 20.06 | 40.90 | 94.51 | 39.66 | 0 | 39.66 | No |
| 12 | CG Power & Ind | CGPOWER | 823.15 | 116.55 | 129687 | 0.16 | 283.91 | 18.42 | 3175.35 | 26.22 | 37.48 | 49.91 | 38.00 | 0 | 38.00 | No |
| 13 | Ingersoll-Rand | INGERSOLL | 4216.00 | 48.03 | 13299 | 1.90 | 71.89 | 15.75 | 455.48 | 19.39 | 60.02 | 33.94 | 36.34 | 0 | 36.34 | No |
| 14 | Zen Technologies | ZENTEC | 1674.40 | 57.66 | 15123 | 0.12 | 55.71 | 37.89 | 177.82 | 16.83 | 37.22 | 30.04 | 27.66 | 0 | 27.66 | No |
| 15 | Tanfac Inds. | TANFAC | 2486.55 | 66.28 | 4960 | 0.18 | 15.57 | -55.26 | 173.30 | -2.74 | 41.76 | 30.88 | 18.66 | −24 (QPV≤0, QSV≤0) | **−5.34** | No |

## Key Flags

- **Tanfac Inds.**: QPV% negative (−55.26) and QSV% negative (−2.74) — both soft penalties applied (−12 each = −24 total)
- All other stocks had positive scoring column values — no penalties applied
- No missing or non-numeric values detected in any scoring column
- User-specified pre-rank cap: **3**
- Working universe: LLOYDSME, ATLANTAELE, GVT&D
