# Screen Universe

Fetched both HTML pages from the supplied Screener URL. Parsed rows: `49`.
Deduplicated rows: `49`. The top `20` adjusted pre-rank scores became the
working universe before any stock-level fundamental dispatch.

Visible schema: `CMP Rs.`, `P/E`, `Mar Cap Rs.Cr.`, `Div Yld %`,
`NP Qtr Rs.Cr.`, `Qtr Profit Var %`, `Sales Qtr Rs.Cr.`,
`Qtr Sales Var %`, `ROCE %`, `3mth return %`.

Scoring columns: `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`,
`3mth return %`. The other six visible numeric columns were context-only.

| Rank | Symbol | Company | Profit Var | Sales Var | ROCE | 3m Return | Adjusted PreRank | Top 20 | Flags |
|---:|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | SIGMAADV | Sigma Advanced System | 1400.69 | 469.05 | 60.82 | 165.73 | 95.79 | yes | - |
| 2 | SPARC | SPARC | 2987.34 | 6715.81 | 165.00 | 66.91 | 94.58 | yes | - |
| 3 | WEBELSOLAR | Websol Energy | 152.31 | 132.07 | 63.18 | 97.51 | 80.51 | yes | - |
| 4 | IBULLSLTD | Indiabulls | 259.74 | 302.18 | 16.17 | 101.24 | 78.31 | yes | - |
| 5 | VMARCIND | V-Marc India | 157.30 | 97.52 | 41.38 | 97.32 | 75.84 | yes | - |
| 6 | CUPID | Cupid | 213.94 | 116.07 | 33.46 | 58.71 | 74.86 | yes | - |
| 7 | ATLANTAELE | Atlanta Electric | 129.07 | 81.69 | 45.26 | 110.59 | 72.38 | yes | - |
| 8 | TIMEX | Timex Group | 212.12 | 73.69 | 92.77 | 57.75 | 72.36 | yes | - |
| 9 | GVPIL | GE Power | 418.10 | 18.78 | 79.96 | 81.62 | 68.78 | yes | - |
| 10 | KSHINTL | KSH Internationa | 87.16 | 100.52 | 21.36 | 112.10 | 65.95 | yes | - |
| 11 | UTLSOLAR | Fujiyama Power | 107.49 | 87.52 | 34.95 | 70.30 | 65.66 | yes | - |
| 12 | MTARTECH | MTAR Technologie | 212.25 | 67.14 | 15.20 | 106.98 | 65.36 | yes | - |
| 13 | HFCL | HFCL | 319.21 | 127.81 | 10.86 | 162.65 | 65.29 | yes | ROCE below 15 |
| 14 | CPPLUS | Aditya Infotech | 207.73 | 45.49 | 29.61 | 71.91 | 64.47 | yes | - |
| 15 | LLOYDSENGG | Lloyds Engineeri | 156.60 | 113.41 | 17.08 | 54.00 | 62.80 | yes | - |
| 16 | EMMVEE | Emmvee Photovol. | 89.43 | 62.25 | 44.83 | 66.66 | 60.36 | yes | - |
| 17 | FCL | Fineotex Chem | 58.29 | 161.90 | 18.30 | 69.38 | 60.27 | yes | - |
| 18 | BSE | BSE | 61.47 | 84.67 | 58.03 | 53.16 | 58.87 | yes | - |
| 19 | IDEAFORGE | Ideaforge Tech | 333.33 | 594.44 | -2.44 | 104.60 | 54.38 | yes | negative ROCE |
| 20 | SASKEN | Sasken Technol. | 144.70 | 125.67 | 10.18 | 97.24 | 54.00 | yes | ROCE below 15 |
| 21 | STLTECH | Sterlite Tech. | 744.40 | 36.98 | 7.75 | 236.82 | 53.22 | no | ROCE below 15 |
| 22 | APOLLO | Apollo Micro Sys | 168.71 | 81.28 | 14.47 | 71.99 | 52.87 | no | ROCE below 15 |
| 23 | BLISSGVS | Bliss GVS Pharma | 128.90 | 29.80 | 16.77 | 100.57 | 52.77 | no | - |
| 24 | CEMPRO | Cemindia Project | 113.63 | 17.42 | 33.83 | 85.93 | 52.50 | no | - |
| 25 | SHADOWFAX | Shadowfax Technologies | 648.31 | 73.62 | 9.66 | 59.31 | 51.88 | no | ROCE below 15 |
| 26 | POWERINDIA | Hitachi Energy | 79.71 | 46.21 | 29.02 | 50.40 | 49.64 | no | - |
| 27 | AEROFLEX | Aeroflex | 57.08 | 37.25 | 18.77 | 70.86 | 46.50 | no | - |
| 28 | WHEELS | Wheels India | 51.91 | 22.46 | 18.83 | 74.74 | 39.76 | no | - |
| 29 | SBCL | Shivalik Bimetal | 23.75 | 22.80 | 26.79 | 64.90 | 38.56 | no | - |
| 30 | TRITURBINE | Triveni Turbine | 8.52 | 26.32 | 35.86 | 51.57 | 37.47 | no | - |
| 31 | SHAILY | Shaily Engineer. | 64.85 | 10.23 | 30.17 | 53.30 | 36.70 | no | - |
| 32 | BHEL | B H E L | 155.82 | 36.88 | 8.51 | 57.29 | 36.21 | no | ROCE below 15 |
| 33 | WELCORP | Welspun Corp | 19.76 | 9.87 | 22.91 | 66.85 | 29.77 | no | - |
| 34 | IOLCP | IOL Chemicals | 68.18 | 17.37 | 11.25 | 76.56 | 29.25 | no | ROCE below 15 |
| 35 | BBOX | Black Box | 1.93 | 9.48 | 22.20 | 94.40 | 27.86 | no | - |
| 36 | ATGL | Adani Total Gas | 4.32 | 15.92 | 15.16 | 51.04 | 21.16 | no | - |
| 37 | UNIVCABLES | Universal Cables | 11.33 | 24.66 | 11.68 | 63.50 | 20.96 | no | ROCE below 15 |
| 38 | HIRECT | Hind Rectifiers | -129.43 | 51.21 | 18.57 | 57.08 | 19.77 | no | non-positive profit growth |
| 39 | BALAMINES | Balaji Amines | 57.79 | 11.92 | 11.03 | 63.29 | 19.11 | no | ROCE below 15 |
| 40 | THERMAX | Thermax | 17.86 | 12.53 | 14.88 | 59.81 | 15.62 | no | ROCE below 15 |
| 41 | ADANIPOWER | Adani Power | 52.34 | -0.10 | 17.29 | 73.70 | 15.53 | no | non-positive sales growth |
| 42 | ADANIGREEN | Adani Green | 55.75 | 13.96 | 7.02 | 55.74 | 14.75 | no | ROCE below 15 |
| 43 | DEEDEV | DEE Development | -16.38 | 26.26 | 10.92 | 101.60 | 8.22 | no | profit penalty; ROCE below 15 |
| 44 | NOVARTIND | Novartis India | -13.82 | 7.95 | 16.25 | 70.83 | 7.50 | no | profit penalty |
| 45 | E2E | E2E Networks | -52.68 | 185.66 | -0.51 | 52.52 | 1.65 | no | profit penalty; negative ROCE |
| 46 | SUNFLAG | Sunflag Iron | -20.74 | 13.31 | 4.06 | 51.91 | -10.62 | no | profit penalty; ROCE below 15 |
| 47 | LUXIND | Lux Industries | -16.19 | 7.58 | 7.84 | 53.24 | -12.28 | no | profit penalty; ROCE below 15 |
| 48 | OLAELEC | Ola Electric | 42.53 | -56.63 | -19.56 | 64.51 | -18.04 | no | sales penalty; negative ROCE |
| 49 | SUVEN | Suven Life Scie. | -3.78 | 3.40 | -76.92 | 91.24 | -19.08 | no | profit penalty; negative ROCE |
