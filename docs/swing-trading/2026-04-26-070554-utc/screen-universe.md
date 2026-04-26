# Screen Universe

## HTML Coverage

- **Screen URL:** https://www.screener.in/screens/3474384/return-over-3-months/
- **Fetched pages:** 1 through 5.
- **Screener page info:** 125 results found.
- **Rows parsed:** 125.
- **Unique symbols:** 125.
- **Deduplication:** no duplicate symbols found.
- **User pre-rank cap:** top 20.
- **Fundamental coverage requested:** top 5 from the pre-ranked universe.
- **Technical coverage requested:** top 3 from the fundamental ranking.

## Screen Thesis

The visible screen starts with price momentum and market-cap liquidity: `Return over 3months > 30 AND Market Capitalization > 3000`. This run then applies operating-sponsorship pre-rank to avoid letting raw three-month momentum dominate the universe.

## Fixed Visible Schema

| Column | Role |
|---|---|
| CMP Rs. | Context only |
| P/E | Context only |
| Mar Cap Rs.Cr. | Context only |
| Div Yld % | Context only |
| NP Qtr Rs.Cr. | Context only |
| Qtr Profit Var % | Scoring |
| Sales Qtr Rs.Cr. | Context only |
| Qtr Sales Var % | Scoring |
| ROCE % | Scoring |
| 3mth return % | Scoring |

## Scoring Method

`PreRankScore = 0.35 * rank(Qtr Profit Var %) + 0.35 * rank(Qtr Sales Var %) + 0.20 * rank(ROCE %) + 0.10 * rank(3mth return %)`.

Soft penalties were then applied for non-positive profit growth, non-positive sales growth, ROCE below 15%, non-positive 3-month return, and negative ROCE distortion.

## Top 20 Working Universe

| PreRank | Symbol | Company | CMP | Qtr Profit Var % | Qtr Sales Var % | ROCE % | 3mth return % | Adjusted PreRankScore | Flags |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | QPOWER | Quality Power El | 1396.40 | 169.18 | 291.22 | 26.60 | 133.49 | 90.67 | - |
| 2 | LLOYDSME | Lloyds Metals | 1695.60 | 169.05 | 201.94 | 38.28 | 52.00 | 90.11 | - |
| 3 | ATLANTAELE | Atlanta Electric | 1778.50 | 125.33 | 79.71 | 50.20 | 144.20 | 89.74 | - |
| 4 | GVT&D | GE Vernova T&D | 4598.30 | 138.53 | 58.40 | 54.74 | 69.51 | 86.39 | - |
| 5 | INA | Insolation Ener | 144.50 | 173.57 | 77.05 | 34.73 | 46.63 | 85.96 | - |
| 6 | UTLSOLAR | Fujiyama Power | 302.24 | 124.29 | 73.80 | 38.88 | 46.78 | 83.29 | - |
| 7 | ENGINERSIN | Engineers India | 242.89 | 219.30 | 58.29 | 25.01 | 45.31 | 81.24 | - |
| 8 | WEBELSOLAR | Websol Energy | 110.85 | 64.00 | 77.19 | 59.25 | 48.23 | 80.06 | - |
| 9 | CUPID | Cupid | 113.09 | 196.66 | 105.67 | 17.10 | 42.36 | 79.16 | - |
| 10 | GROWW | Billionbrains | 218.02 | 122.06 | 87.93 | 37.38 | 30.15 | 78.24 | - |
| 11 | KRISHANA | Krishana Phosch. | 638.15 | 152.83 | 59.76 | 27.24 | 31.71 | 77.19 | - |
| 12 | SKYGOLD | Sky Gold & Diam. | 412.55 | 120.42 | 77.13 | 21.21 | 36.83 | 74.71 | - |
| 13 | PRECWIRE | Prec. Wires (I) | 390.15 | 98.94 | 37.19 | 26.78 | 81.61 | 72.81 | - |
| 14 | RUBICON | Rubicon Research | 938.70 | 91.23 | 51.73 | 26.05 | 44.40 | 72.71 | - |
| 15 | ACUTAAS | Acutaas Chemical | 2395.00 | 140.18 | 42.98 | 19.92 | 44.85 | 72.46 | - |
| 16 | CPPLUS | Aditya Infotech | 2273.20 | 138.82 | 37.32 | 19.49 | 62.95 | 72.29 | - |
| 17 | SHARDACROP | Sharda Cropchem | 1109.65 | 365.87 | 38.68 | 16.50 | 37.61 | 70.44 | - |
| 18 | BAJAJCON | Bajaj Consumer | 453.40 | 105.29 | 30.41 | 30.60 | 48.27 | 69.78 | - |
| 19 | KRN | KRN Heat Exchan | 1247.70 | 65.04 | 37.46 | 20.75 | 108.61 | 68.32 | - |
| 20 | EBGNG | GNG Electronics | 384.25 | 102.78 | 40.26 | 19.84 | 52.48 | 68.07 | - |

## Full Parsed Universe

| PreRank | Page | Symbol | Company | Adj Score | Status | Flags |
|---:|---:|---|---|---:|---|---|
| 1 | 2 | QPOWER | Quality Power El | 90.67 | Top 20 | - |
| 2 | 1 | LLOYDSME | Lloyds Metals | 90.11 | Top 20 | - |
| 3 | 1 | ATLANTAELE | Atlanta Electric | 89.74 | Top 20 | - |
| 4 | 1 | GVT&D | GE Vernova T&D | 86.39 | Top 20 | - |
| 5 | 1 | INA | Insolation Ener | 85.96 | Top 20 | - |
| 6 | 1 | UTLSOLAR | Fujiyama Power | 83.29 | Top 20 | - |
| 7 | 2 | ENGINERSIN | Engineers India | 81.24 | Top 20 | - |
| 8 | 1 | WEBELSOLAR | Websol Energy | 80.06 | Top 20 | - |
| 9 | 3 | CUPID | Cupid | 79.16 | Top 20 | - |
| 10 | 1 | GROWW | Billionbrains | 78.24 | Top 20 | - |
| 11 | 2 | KRISHANA | Krishana Phosch. | 77.19 | Top 20 | - |
| 12 | 2 | SKYGOLD | Sky Gold & Diam. | 74.71 | Top 20 | - |
| 13 | 2 | PRECWIRE | Prec. Wires (I) | 72.81 | Top 20 | - |
| 14 | 2 | RUBICON | Rubicon Research | 72.71 | Top 20 | - |
| 15 | 3 | ACUTAAS | Acutaas Chemical | 72.46 | Top 20 | - |
| 16 | 3 | CPPLUS | Aditya Infotech | 72.29 | Top 20 | - |
| 17 | 3 | SHARDACROP | Sharda Cropchem | 70.44 | Top 20 | - |
| 18 | 1 | BAJAJCON | Bajaj Consumer | 69.78 | Top 20 | - |
| 19 | 2 | KRN | KRN Heat Exchan | 68.32 | Top 20 | - |
| 20 | 3 | EBGNG | GNG Electronics | 68.07 | Top 20 | - |
| 21 | 3 | POWERINDIA | Hitachi Energy | 67.81 | Outside cap | - |
| 22 | 2 | HIRECT | Hind Rectifiers | 65.95 | Outside cap | - |
| 23 | 5 | SEAMECLTD | SEAMEC Ltd | 65.66 | Outside cap | roce<15 |
| 24 | 2 | DATAPATTNS | Data Pattern | 65.54 | Outside cap | - |
| 25 | 1 | ENRIN | Siemens Ener.Ind | 65.33 | Outside cap | - |
| 26 | 4 | MTARTECH | MTAR Technologie | 65.23 | Outside cap | roce<15 |
| 27 | 3 | RAMRAT | Ram Ratna Wires | 64.74 | Outside cap | - |
| 28 | 5 | DIACABS | Diamond Power | 63.79 | Outside cap | ROCE:zero |
| 29 | 1 | VOLTAMP | Volt.Transform. | 60.48 | Outside cap | - |
| 30 | 4 | SAMBHV | Sambhv Steel | 58.47 | Outside cap | roce<15 |
| 31 | 1 | TDPOWERSYS | TD Power Systems | 57.81 | Outside cap | - |
| 32 | 4 | DYNAMATECH | Dynamatic Tech. | 57.30 | Outside cap | roce<15 |
| 33 | 3 | RPTECH | Rashi Peripheral | 56.32 | Outside cap | roce<15 |
| 34 | 1 | INOXINDIA | Inox India | 56.24 | Outside cap | - |
| 35 | 4 | SGFIN | SG Finserve | 56.13 | Outside cap | roce<15 |
| 36 | 1 | CGPOWER | CG Power & Ind | 56.05 | Outside cap | - |
| 37 | 4 | SYRMA | Syrma SGS Tech. | 55.67 | Outside cap | roce<15 |
| 38 | 1 | PREMIERENE | Premier Energies | 55.01 | Outside cap | - |
| 39 | 3 | SHAILY | Shaily Engineer. | 54.84 | Outside cap | - |
| 40 | 1 | SCHNEIDER | Schneider Elect. | 54.10 | Outside cap | - |
| 41 | 5 | PFOCUS | Prime Focus | 53.15 | Outside cap | roce<15 |
| 42 | 5 | GVPIL | GE Power | 52.53 | Outside cap | roce<15 |
| 43 | 1 | GOKULAGRO | Gokul Agro | 52.04 | Outside cap | - |
| 44 | 4 | SCI | S C I | 51.66 | Outside cap | roce<15 |
| 45 | 1 | NATCOPHARM | Natco Pharma | 51.50 | Outside cap | - |
| 46 | 1 | APARINDS | Apar Inds. | 51.02 | Outside cap | - |
| 47 | 4 | AXISCADES | AXISCADES Tech. | 50.88 | Outside cap | roce<15 |
| 48 | 2 | JAYNECOIND | Jayaswal Neco | 50.86 | Outside cap | - |
| 49 | 1 | SHILCTECH | Shilchar Tech. | 50.83 | Outside cap | - |
| 50 | 2 | SKIPPER | Skipper | 49.34 | Outside cap | - |
| 51 | 4 | DEEPINDS | Deep Industries | 49.27 | Outside cap | roce<15 |
| 52 | 3 | MANINDS | Man Industries | 49.12 | Outside cap | - |
| 53 | 4 | KIRLOSENG | Kirloskar Oil | 48.50 | Outside cap | roce<15 |
| 54 | 3 | TECHNOE | Techno Elec.Engg | 48.48 | Outside cap | - |
| 55 | 2 | AEROFLEX | Aeroflex | 47.61 | Outside cap | - |
| 56 | 1 | ZENTEC | Zen Technologies | 47.51 | Outside cap | - |
| 57 | 1 | INGERRAND | Ingersoll-Rand | 46.65 | Outside cap | - |
| 58 | 2 | KSHINTL | KSH Internationa | 46.06 | Outside cap | profit<=0 |
| 59 | 3 | MARINE | Marine Electric. | 46.01 | Outside cap | - |
| 60 | 4 | YATHARTH | Yatharth Hospit. | 45.91 | Outside cap | roce<15 |
| 61 | 5 | AARTIIND | Aarti Industries | 45.51 | Outside cap | roce<15 |
| 62 | 3 | SPLPETRO | Supreme Petroch. | 45.16 | Outside cap | - |
| 63 | 3 | FINCABLES | Finolex Cables | 44.99 | Outside cap | - |
| 64 | 3 | WABAG | Va Tech Wabag | 44.85 | Outside cap | - |
| 65 | 5 | SHILPAMED | Shilpa Medicare | 44.37 | Outside cap | roce<15 |
| 66 | 4 | AZAD | Azad Engineering | 44.07 | Outside cap | roce<15 |
| 67 | 5 | ROSSTECH | Rossell Techsys | 43.25 | Outside cap | roce<15 |
| 68 | 2 | IMFA | Indian Metals | 43.11 | Outside cap | - |
| 69 | 3 | AMBER | Amber Enterp. | 42.28 | Outside cap | roce<15 |
| 70 | 5 | MAHLOG | Mahindra Logis. | 42.14 | Outside cap | roce<15 |
| 71 | 2 | SBCL | Shivalik Bimetal | 41.93 | Outside cap | - |
| 72 | 3 | ISGEC | ISGEC Heavy | 41.78 | Outside cap | roce<15 |
| 73 | 2 | KSB | KSB | 41.42 | Outside cap | - |
| 74 | 4 | SANSERA | Sansera Enginee. | 41.33 | Outside cap | roce<15 |
| 75 | 2 | PARKHOSPS | Park Medi World | 41.04 | Outside cap | - |
| 76 | 5 | STLTECH | Sterlite Tech. | 40.84 | Outside cap | roce<15 |
| 77 | 4 | SIGMAADV | Sigma Advanced System | 40.27 | Outside cap | roce<15 |
| 78 | 5 | BHEL | B H E L | 39.47 | Outside cap | roce<15 |
| 79 | 2 | AVANTIFEED | Avanti Feeds | 38.06 | Outside cap | - |
| 80 | 3 | THERMAX | Thermax | 36.44 | Outside cap | - |
| 81 | 3 | STAR | Strides Pharma | 36.26 | Outside cap | roce<15 |
| 82 | 5 | AEQUS | Aequs | 35.58 | Outside cap | roce<15 |
| 83 | 4 | BHARATFORG | Bharat Forge | 34.37 | Outside cap | roce<15 |
| 84 | 5 | ATHERENERG | Ather Energy | 33.70 | Outside cap | ROCE:zero-negative, roce<15 |
| 85 | 3 | TORNTPOWER | Torrent Power | 32.40 | Outside cap | - |
| 86 | 5 | ADANIGREEN | Adani Green | 32.32 | Outside cap | roce<15 |
| 87 | 5 | HFCL | HFCL | 31.38 | Outside cap | roce<15 |
| 88 | 4 | TRUALT | TruAlt Bioenergy | 31.20 | Outside cap | profit<=0, roce<15 |
| 89 | 2 | WELCORP | Welspun Corp | 30.70 | Outside cap | profit<=0 |
| 90 | 4 | SMSPHARMA | SMS Pharma. | 30.22 | Outside cap | roce<15 |
| 91 | 5 | LLOYDSENGG | Lloyds Engineeri | 29.97 | Outside cap | ROCE:zero |
| 92 | 5 | IBULLSLTD | Indiabulls | 29.41 | Outside cap | ROCE:zero, sales<=0 |
| 93 | 2 | AGIIL | AGI Infra | 25.37 | Outside cap | sales<=0 |
| 94 | 4 | ADANIENSOL | Adani Energy Sol | 25.30 | Outside cap | roce<15 |
| 95 | 2 | TIINDIA | Tube Investments | 24.53 | Outside cap | profit<=0 |
| 96 | 4 | PAISALO | Paisalo Digital | 24.44 | Outside cap | roce<15 |
| 97 | 2 | TARIL | T R I L | 24.06 | Outside cap | profit<=0 |
| 98 | 1 | ABB | A B B | 23.17 | Outside cap | profit<=0 |
| 99 | 3 | BELRISE | Belrise Industri | 22.45 | Outside cap | roce<15 |
| 100 | 5 | ACMESOLAR | ACME Solar Hold. | 22.00 | Outside cap | profit<=0, roce<15 |
| 101 | 1 | ABSLAMC | Aditya AMC | 19.45 | Outside cap | profit<=0 |
| 102 | 1 | CUMMINSIND | Cummins India | 18.65 | Outside cap | sales<=0 |
| 103 | 5 | SINDHUTRAD | Sindhu Trade | 14.77 | Outside cap | sales<=0, roce<15 |
| 104 | 4 | LUXIND | Lux Industries | 14.52 | Outside cap | profit<=0, roce<15 |
| 105 | 4 | PFC | Power Fin.Corpn. | 14.15 | Outside cap | roce<15 |
| 106 | 3 | SIEMENS | Siemens | 12.84 | Outside cap | profit<=0 |
| 107 | 4 | SGMART | SG Mart | 11.22 | Outside cap | profit<=0, roce<15 |
| 108 | 5 | E2E | E2E Networks | 9.49 | Outside cap | ROCE:zero-negative, profit<=0, roce<15 |
| 109 | 5 | SUVEN | Suven Life Scie. | 6.93 | Outside cap | ROCE:zero-negative, profit<=0, roce<15 |
| 110 | 2 | ADANIPOWER | Adani Power | 3.13 | Outside cap | profit<=0, sales<=0 |
| 111 | 3 | GALLANTT | Gallantt Ispat L | 0.94 | Outside cap | profit<=0, sales<=0 |
| 112 | 1 | 506854 | Tanfac Inds. | 0.53 | Outside cap | profit<=0, sales<=0 |
| 113 | 4 | VTL | Vardhman Textile | -0.34 | Outside cap | profit<=0, roce<15 |
| 114 | 2 | GRWRHITECH | Garware Hi Tech | -0.36 | Outside cap | profit<=0, sales<=0 |
| 115 | 4 | DALMIASUG | Dalmia Bharat | -0.71 | Outside cap | sales<=0, roce<15 |
| 116 | 4 | NEOGEN | Neogen Chemicals | -1.05 | Outside cap | profit<=0, roce<15 |
| 117 | 2 | ELECON | Elecon Engg.Co | -4.39 | Outside cap | profit<=0, sales<=0 |
| 118 | 5 | KTKBANK | Karnataka Bank | -4.94 | Outside cap | sales<=0, roce<15 |
| 119 | 3 | PRAJIND | Praj Industries | -5.39 | Outside cap | profit<=0, sales<=0 |
| 120 | 3 | JINDALSAW | Jindal Saw | -6.38 | Outside cap | profit<=0, sales<=0 |
| 121 | 4 | JPPOWER | JP Power Ven. | -9.72 | Outside cap | profit<=0, roce<15 |
| 122 | 5 | NOCIL | NOCIL | -13.84 | Outside cap | profit<=0, sales<=0, roce<15 |
| 123 | 5 | GUJALKALI | Gujarat Alkalies | -17.34 | Outside cap | ROCE:zero-negative, profit<=0, roce<15 |
| 124 | 5 | JINDALPOLY | Jindal Poly Film | -21.98 | Outside cap | profit<=0, sales<=0, roce<15 |
| 125 | 5 | TEJASNET | Tejas Networks | -41.36 | Outside cap | ROCE:zero-negative, profit<=0, sales<=0, roce<15 |
