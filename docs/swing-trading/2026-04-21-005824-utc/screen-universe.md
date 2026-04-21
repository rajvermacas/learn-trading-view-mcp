# Screen Universe — 2026-04-21

## Screen Details

- **URL**: https://www.screener.in/screens/3474384/return-over-3-months
- **Filter**: `Return over 3months > 30 AND Market Capitalization > 3000`
- **Total Parsed**: 110 stocks across 5 pages
- **Pre-Rank Cap**: 15 (user-specified)
- **Working Universe**: Top 15 by adjusted PreRankScore

## Visible Screen Schema

### Scoring Columns (contribute to PreRankScore)
- `Qtr Profit Var %` — weight 0.35
- `Qtr Sales Var %` — weight 0.35
- `ROCE %` — weight 0.20
- `3mth return %` — weight 0.10

### Context-Only Columns (do not affect PreRankScore)
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Sales Qtr Rs.Cr.`

## Working Universe (Top 15 by Adjusted PreRankScore)

| PreRank | Symbol | Name | ProfitVar% | SalesVar% | ROCE% | 3mRet% | Base | Penalty | Adjusted | Flags |
|---------|--------|------|-----------|----------|-------|--------|------|---------|----------|-------|
| 1 | QPOWER | Quality Power El | 169.2 | 291.2 | 26.6 | 93.6 | 88.83 | 0 | 88.83 | |
| 2 | LLOYDSME | Lloyds Metals | 169.1 | 201.9 | 38.3 | 42.6 | 87.06 | 0 | 87.06 | |
| 3 | ATLANTAELE | Atlanta Electric | 125.3 | 79.7 | 50.2 | 84.4 | 86.63 | 0 | 86.63 | |
| 4 | WAAREEENER | Waaree Energies | 158.1 | 118.8 | 34.9 | 44.2 | 85.45 | 0 | 85.45 | |
| 5 | GVT&D | GE Vernova T&D | 138.5 | 58.4 | 54.7 | 65.5 | 83.53 | 0 | 83.53 | |
| 6 | INSOLATION | Insolation Ener | 173.6 | 77.0 | 34.7 | 40.4 | 83.52 | 0 | 83.52 | |
| 7 | SAATVIK | Saatvik Green | 144.1 | 142.6 | 52.3 | 32.0 | 82.49 | 0 | 82.49 | |
| 8 | BSE | BSE | 175.8 | 62.0 | 46.6 | 32.0 | 80.66 | 0 | 80.66 | |
| 9 | EMMVEE | Emmvee Photovol. | 165.8 | 118.1 | 28.0 | 33.7 | 79.95 | 0 | 79.95 | |
| 10 | CUPID | Cupid | 196.7 | 105.7 | 17.1 | 40.0 | 76.77 | 0 | 76.77 | |
| 11 | KRISHANA | Krishana Phosch. | 152.8 | 59.8 | 27.2 | 35.8 | 76.27 | 0 | 76.27 | |
| 12 | ENGINERSIN | Engineers India | 219.3 | 58.3 | 25.0 | 35.6 | 76.10 | 0 | 76.10 | |
| 13 | ACUTAAS | Acutaas Chemical | 140.2 | 43.0 | 19.9 | 50.4 | 70.73 | 0 | 70.73 | |
| 14 | BAJAJCON | Bajaj Consumer | 105.3 | 30.4 | 30.6 | 91.7 | 70.52 | 0 | 70.52 | |
| 15 | RUBICON | Rubicon Research | 91.2 | 51.7 | 26.1 | 40.7 | 70.15 | 0 | 70.15 | |

## Excluded from Working Universe (Ranks 16-110, selected samples)

| PreRank | Symbol | Adjusted | Key Penalty |
|---------|--------|----------|-------------|
| 16 | PRECWIRE | 69.55 | — |
| 17 | CPPLUS | 69.11 | — |
| 18 | SHARDACROP | 68.50 | — |
| 19 | SEAMECLTD | 66.54 | low_roce |
| 20 | KRN | 66.40 | — |
| 27 | ENRIN | 61.61 | — |
| 44 | SHILCTECH | 49.79 | — |
| 52 | DHENU | 45.08 | neg_sales, ret3m_missing |
| 82 | TRUALT | 26.04 | neg_profit, low_roce |
| 95 | JAYNECOIND | 11.03 | low_roce |
| 105 | SUPPETRO | -1.41 | neg_profit, neg_sales |
| 109 | GUJALKALI | -18.63 | roce_negative, neg_profit |
| 110 | JPFL | -21.31 | neg_profit, neg_sales, low_roce |

## Pagination & Deduplication

- Page 1: stocks 1-25
- Page 2: stocks 26-50
- Page 3: stocks 51-75
- Page 4: stocks 76-100
- Page 5: stocks 101-110

All 110 stocks parsed. No duplicates found across pages. Stocks with all-None scoring values (JINDALSAW, SONACOMS, SKYGOLD) were excluded from ranking as they had no extractable data.

## Penalty Legend

- `neg_profit`: Qtr Profit Var % ≤ 0, subtract 12
- `neg_sales`: Qtr Sales Var % ≤ 0, subtract 12
- `low_roce`: ROCE % < 15, subtract 8
- `neg_roce_extra`: ROCE % < 0, additional subtract 12 (contribution zeroed)
- `neg_ret3m`: 3mth return % ≤ 0, subtract 8
- `profitvar_missing` / `salesvar_missing` / `roce_missing` / `ret3m_missing`: metric contribution set to 0
