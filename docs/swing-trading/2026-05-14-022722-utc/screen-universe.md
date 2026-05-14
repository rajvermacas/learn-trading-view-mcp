# Screen Universe

Screen thesis: high-momentum Indian stocks with recent operating sponsorship; screen title `3 month Return 30` with visible filters `Return over 3 months` and `Market Capitalization > 3000`

Full HTML coverage: 4 pages fetched, 84 rows parsed, 84 unique symbols retained after deduplication.
Pre-rank cap: top 20 names by adjusted `PreRankScore`.
Working-universe cache state: 19 fresh dossiers and 1 missing dossier at dispatch start; `RAMRAT` required the fresh fundamental refresh.

Fixed visible schema:
- `CMP Rs.`
- `P/E`
- `Mar Cap Rs.Cr.`
- `Div Yld %`
- `NP Qtr Rs.Cr.`
- `Qtr Profit Var %`
- `Sales Qtr Rs.Cr.`
- `Qtr Sales Var %`
- `ROCE %`
- `3mth return %`

Pre-rank inputs:
- scoring columns: `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, `3mth return %`
- context-only columns: `CMP Rs.`, `P/E`, `Mar Cap Rs.Cr.`, `Div Yld %`, `NP Qtr Rs.Cr.`, `Sales Qtr Rs.Cr.`

Penalty flags used in the adjusted `PreRankScore` cut:
- `Qtr Profit Var % <= 0`
- `Qtr Sales Var % <= 0`
- `ROCE % < 15`
- `3mth return % <= 0`

Zero-contribution handling:
- blank, missing, `-`, `--`, `NaN`, or otherwise non-numeric scoring cells were assigned zero contribution
- no stock-specific repair fetches were used to rebuild the pre-rank table

Top 20 working universe after the pre-rank cut:

| Rank | Symbol | Working universe status | Notes |
|---:|---|---|---|
| 1 | LLOYDSME | included | strongest sponsor profile in the capped set |
| 2 | MCX | included | large-cap momentum with clean operating follow-through |
| 3 | WEBELSOLAR | included | strong pre-rank, weaker lower-timeframe stop quality |
| 4 | ATLANTAELE | included | high sponsorship and strong repair structure |
| 5 | QPOWER | included | strong fundamentals, fragile intraday repair |
| 6 | IBULLSLTD | included | pre-rank survivor, not advanced to technical review |
| 7 | JAINREC | included | breakout-and-retest profile |
| 8 | CUPID | included | strong sponsorship, but chart is extended and volatile |
| 9 | MTARTECH | included | powerful trend, but extension risk is elevated |
| 10 | HFCL | included | pre-rank survivor, not advanced to technical review |
| 11 | LLOYDSENGG | included | constructive trend with defendable stop path |
| 12 | KRISHANA | included | strong technical alignment and clean support stack |
| 13 | GVPIL | included | momentum plus repair pattern |
| 14 | CPPLUS | included | bullish but stretched, better on pullback |
| 15 | DEEDEV | included | pre-rank survivor, not advanced to technical review |
| 16 | ACUTAAS | included | best-aligned continuation setup |
| 17 | PRECWIRE | included | defensive hold / reclaim structure |
| 18 | KENNAMET | included | constructive but paused |
| 19 | KRN | included | pre-rank survivor, not advanced to technical review |
| 20 | RAMRAT | included | missing at cache start, refreshed in this run |

Excluded by the coverage cap: every name ranked below 20 in the full 84-row screen universe.

