#!/usr/bin/env python3
"""Compute PreRankScore for the screener universe - 2026-04-23 run."""
import json

# Full 136-stock universe from https://www.screener.in/screens/3474384/return-over-3-months
# Columns: name, symbol, cmp, pe, mcap, divyld, npqtr, qpv, salesqtr, qsv, roce, ret3m
stocks = [
    {"name": "Shilchar Tech.", "symbol": "SHILCTECH", "cmp": 5307.80, "pe": 32.71, "mcap": 6055.69, "divyld": 0.24, "npqtr": 42.34, "qpv": 21.77, "salesqtr": 170.26, "qsv": 10.75, "roce": 71.30, "ret3m": 79.43},
    {"name": "Siemens Ener.Ind", "symbol": "ENRIN", "cmp": 3221.60, "pe": 94.04, "mcap": 114711.59, "divyld": 0.12, "npqtr": 312.90, "qpv": 51.67, "salesqtr": 1910.90, "qsv": 25.97, "roce": 67.75, "ret3m": 51.58},
    {"name": "Ingersoll-Rand", "symbol": "INGERRAND", "cmp": 4188.20, "pe": 47.81, "mcap": 13238.84, "divyld": 1.91, "npqtr": 71.89, "qpv": 15.75, "salesqtr": 455.48, "qsv": 19.39, "roce": 60.02, "ret3m": 33.06},
    {"name": "Websol Energy", "symbol": "WEBSOLENER", "cmp": 106.79, "pe": 20.21, "mcap": 4647.92, "divyld": 0.00, "npqtr": 64.98, "qpv": 64.00, "salesqtr": 261.02, "qsv": 77.19, "roce": 59.25, "ret3m": 42.81},
    {"name": "GE Vernova T&D", "symbol": "GVT&D", "cmp": 4496.40, "pe": 103.00, "mcap": 115103.17, "divyld": 0.11, "npqtr": 290.80, "qpv": 138.53, "salesqtr": 1700.64, "qsv": 58.40, "roce": 54.74, "ret3m": 65.75},
    {"name": "Atlanta Electric", "symbol": "ATLANTAELE", "cmp": 1617.20, "pe": 79.46, "mcap": 12409.98, "divyld": 0.00, "npqtr": 49.42, "qpv": 125.33, "salesqtr": 471.82, "qsv": 79.71, "roce": 50.20, "ret3m": 122.05},
    {"name": "Premier Energies", "symbol": "PREMIERENE", "cmp": 1000.70, "pe": 34.14, "mcap": 45433.81, "divyld": 0.10, "npqtr": 391.62, "qpv": 53.48, "salesqtr": 1936.46, "qsv": 13.02, "roce": 41.12, "ret3m": 46.49},
    {"name": "Schneider Elect.", "symbol": "SCHNEIDER", "cmp": 1127.00, "pe": 102.49, "mcap": 26818.72, "divyld": 0.00, "npqtr": 97.03, "qpv": 16.65, "salesqtr": 1029.17, "qsv": 20.06, "roce": 40.90, "ret3m": 85.76},
    {"name": "Fujiyama Power", "symbol": "FUJIYAMA", "cmp": 285.75, "pe": 45.19, "mcap": 8749.96, "divyld": 0.00, "npqtr": 67.31, "qpv": 124.29, "salesqtr": 588.48, "qsv": 73.80, "roce": 38.88, "ret3m": 38.77},
    {"name": "Lloyds Metals", "symbol": "LLOYDSME", "cmp": 1697.80, "pe": 38.81, "mcap": 95598.04, "divyld": 0.06, "npqtr": 1089.56, "qpv": 169.05, "salesqtr": 5058.08, "qsv": 201.94, "roce": 38.28, "ret3m": 52.20},
    {"name": "Inox India", "symbol": "INOXINDIA", "cmp": 1570.10, "pe": 56.35, "mcap": 14250.78, "divyld": 0.13, "npqtr": 60.70, "qpv": 26.34, "salesqtr": 428.56, "qsv": 28.45, "roce": 37.98, "ret3m": 43.43},
    {"name": "CG Power & Ind", "symbol": "CGPOWER", "cmp": 837.80, "pe": 118.50, "mcap": 131860.22, "divyld": 0.16, "npqtr": 283.91, "qpv": 18.42, "salesqtr": 3175.35, "qsv": 26.22, "roce": 37.48, "ret3m": 52.58},
    {"name": "Zen Technologies", "symbol": "ZENTEC", "cmp": 1721.20, "pe": 59.27, "mcap": 15547.39, "divyld": 0.12, "npqtr": 55.71, "qpv": 37.89, "salesqtr": 177.82, "qsv": 16.83, "roce": 37.22, "ret3m": 33.68},
    {"name": "Cummins India", "symbol": "CUMMINSIND", "cmp": 5176.90, "pe": 61.62, "mcap": 143529.83, "divyld": 0.99, "npqtr": 486.06, "qpv": 4.41, "salesqtr": 3054.92, "qsv": -1.33, "roce": 36.32, "ret3m": 31.71},
    {"name": "Waaree Energies", "symbol": "WAAREEENER", "cmp": 3413.00, "pe": 28.20, "mcap": 98179.69, "divyld": 0.06, "npqtr": 1106.79, "qpv": 158.06, "salesqtr": 7565.05, "qsv": 118.81, "roce": 34.94, "ret3m": 31.30},
    {"name": "Insolation Ener", "symbol": "INSOLATION", "cmp": 154.77, "pe": 19.25, "mcap": 3411.27, "divyld": 0.06, "npqtr": 50.72, "qpv": 173.57, "salesqtr": 575.34, "qsv": 77.05, "roce": 34.73, "ret3m": 57.05},
    {"name": "Gokul Agro", "symbol": "GOKULAGRO", "cmp": 225.72, "pe": 22.23, "mcap": 6650.53, "divyld": 0.00, "npqtr": 77.70, "qpv": 7.17, "salesqtr": 6314.25, "qsv": 26.58, "roce": 34.20, "ret3m": 47.70},
    {"name": "Apar Inds.", "symbol": "APARINDS", "cmp": 11838.00, "pe": 47.96, "mcap": 47562.15, "divyld": 0.43, "npqtr": 208.93, "qpv": 29.80, "salesqtr": 5479.73, "qsv": 16.18, "roce": 32.70, "ret3m": 68.32},
    {"name": "Aditya AMC", "symbol": "ABSLAMC", "cmp": 1047.45, "pe": 30.98, "mcap": 30277.72, "divyld": 2.29, "npqtr": 187.11, "qpv": -17.96, "salesqtr": 458.23, "qsv": 6.85, "roce": 32.24, "ret3m": 34.20},
    {"name": "Bajaj Consumer", "symbol": "BAJAJCON", "cmp": 463.95, "pe": 31.87, "mcap": 6061.33, "divyld": 0.00, "npqtr": 63.60, "qpv": 105.29, "salesqtr": 326.66, "qsv": 30.41, "roce": 30.60, "ret3m": 51.72},
    {"name": "TD Power Systems", "symbol": "TDPOWERSYS", "cmp": 1070.45, "pe": 76.10, "mcap": 16711.79, "divyld": 0.12, "npqtr": 56.32, "qpv": 25.35, "salesqtr": 442.68, "qsv": 26.36, "roce": 30.35, "ret3m": 71.46},
    {"name": "A B B", "symbol": "ABB", "cmp": 7575.50, "pe": 96.15, "mcap": 160532.24, "divyld": 0.52, "npqtr": 432.85, "qpv": -18.35, "salesqtr": 3557.01, "qsv": 5.71, "roce": 29.93, "ret3m": 61.37},
    {"name": "Volt.Transform.", "symbol": "VOLTAMP", "cmp": 10884.50, "pe": 31.08, "mcap": 11013.18, "divyld": 0.92, "npqtr": 99.08, "qpv": 34.99, "salesqtr": 630.32, "qsv": 30.36, "roce": 29.11, "ret3m": 59.46},
    {"name": "Emmvee Photovol.", "symbol": "EMMVEE", "cmp": 273.95, "pe": 35.54, "mcap": 18958.20, "divyld": 0.00, "npqtr": 263.64, "qpv": 165.77, "salesqtr": 1152.25, "qsv": 118.11, "roce": 28.01, "ret3m": 38.04},
    {"name": "Krishana Phosch.", "symbol": "KRISHANA", "cmp": 635.15, "pe": 21.35, "mcap": 3845.99, "divyld": 0.08, "npqtr": 83.08, "qpv": 152.83, "salesqtr": 755.49, "qsv": 59.76, "roce": 27.24, "ret3m": 31.09},
    {"name": "Prec. Wires (I)", "symbol": "PRECWIRE", "cmp": 392.25, "pe": 55.19, "mcap": 7173.36, "divyld": 0.29, "npqtr": 37.70, "qpv": 98.94, "salesqtr": 1347.61, "qsv": 37.19, "roce": 26.78, "ret3m": 82.59},
    {"name": "Quality Power El", "symbol": "QPOWER", "cmp": 1373.85, "pe": 99.43, "mcap": 10640.08, "divyld": 0.07, "npqtr": 62.76, "qpv": 169.18, "salesqtr": 283.99, "qsv": 291.22, "roce": 26.60, "ret3m": 129.72},
    {"name": "Rubicon Research", "symbol": "RUBICON", "cmp": 927.50, "pe": 90.78, "mcap": 15290.42, "divyld": 0.00, "npqtr": 72.80, "qpv": 91.23, "salesqtr": 475.53, "qsv": 51.73, "roce": 26.05, "ret3m": 42.68},
    {"name": "Shriram Pistons", "symbol": "SHRIPISTON", "cmp": 3584.60, "pe": 28.15, "mcap": 15802.63, "divyld": 0.28, "npqtr": 125.70, "qpv": 17.91, "salesqtr": 1023.20, "qsv": 20.67, "roce": 25.70, "ret3m": 32.75},
    {"name": "Engineers India", "symbol": "ENGINERSIN", "cmp": 243.68, "pe": 17.66, "mcap": 13700.31, "divyld": 1.64, "npqtr": 347.17, "qpv": 219.30, "salesqtr": 1210.24, "qsv": 58.29, "roce": 25.01, "ret3m": 45.79},
    {"name": "Goldiam Intl.", "symbol": "GOLDIAM", "cmp": 395.45, "pe": 28.59, "mcap": 4475.31, "divyld": 0.76, "npqtr": 68.39, "qpv": 37.52, "salesqtr": 319.71, "qsv": 14.33, "roce": 24.59, "ret3m": 33.17},
    {"name": "KSB", "symbol": "KSB", "cmp": 977.65, "pe": 58.90, "mcap": 17015.80, "divyld": 0.45, "npqtr": 81.00, "qpv": 33.43, "salesqtr": 784.00, "qsv": 7.93, "roce": 24.52, "ret3m": 40.98},
    {"name": "Skipper", "symbol": "SKIPPER", "cmp": 469.65, "pe": 28.86, "mcap": 5302.41, "divyld": 0.02, "npqtr": 50.17, "qpv": 39.71, "salesqtr": 1370.59, "qsv": 20.73, "roce": 24.42, "ret3m": 39.40},
    {"name": "Avanti Feeds", "symbol": "AVANTIFEED", "cmp": 1460.20, "pe": 31.46, "mcap": 19900.80, "divyld": 0.62, "npqtr": 163.47, "qpv": 10.40, "salesqtr": 1383.52, "qsv": 1.31, "roce": 23.99, "ret3m": 93.38},
    {"name": "T R I L", "symbol": "TRIL", "cmp": 319.90, "pe": 36.32, "mcap": 9603.85, "divyld": 0.06, "npqtr": 91.39, "qpv": -2.55, "salesqtr": 782.67, "qsv": 15.70, "roce": 23.30, "ret3m": 37.59},
    {"name": "Manorama Indust.", "symbol": "MANORAMA", "cmp": 1429.90, "pe": 39.54, "mcap": 8539.19, "divyld": 0.04, "npqtr": 68.24, "qpv": 131.09, "salesqtr": 362.54, "qsv": 73.30, "roce": 23.03, "ret3m": 30.82},
    {"name": "Rolex Rings", "symbol": "ROLEXRINGS", "cmp": 156.08, "pe": 21.54, "mcap": 4260.27, "divyld": 0.00, "npqtr": 47.75, "qpv": 57.61, "salesqtr": 274.84, "qsv": 5.76, "roce": 22.81, "ret3m": 30.15},
    {"name": "Supreme Petroch.", "symbol": "SUPPETRO", "cmp": 820.05, "pe": 56.59, "mcap": 15365.87, "divyld": 1.22, "npqtr": 30.15, "qpv": -50.25, "salesqtr": 1264.69, "qsv": -10.01, "roce": 22.76, "ret3m": 63.54},
    {"name": "Adani Power", "symbol": "ADANIPOWER", "cmp": 214.18, "pe": 36.09, "mcap": 413423.01, "divyld": 0.00, "npqtr": 2488.09, "qpv": -18.89, "salesqtr": 12451.44, "qsv": -8.92, "roce": 22.54, "ret3m": 61.09},
    {"name": "Aeroflex", "symbol": "AEROFLEX", "cmp": 295.68, "pe": 79.66, "mcap": 3913.02, "divyld": 0.10, "npqtr": 16.49, "qpv": 8.42, "salesqtr": 120.89, "qsv": 21.13, "roce": 22.34, "ret3m": 86.20},
    {"name": "AGI Infra", "symbol": "AGIIL", "cmp": 367.00, "pe": 54.72, "mcap": 4591.88, "divyld": 0.03, "npqtr": 26.11, "qpv": 36.92, "salesqtr": 87.50, "qsv": -4.28, "roce": 22.03, "ret3m": 46.27},
    {"name": "Elgi Equipments", "symbol": "ELGIEQUIP", "cmp": 559.40, "pe": 42.74, "mcap": 17732.68, "divyld": 0.39, "npqtr": 95.20, "qpv": 31.40, "salesqtr": 1003.40, "qsv": 18.38, "roce": 21.91, "ret3m": 31.62},
    {"name": "Tube Investments", "symbol": "TIINDIA", "cmp": 3086.80, "pe": 96.69, "mcap": 59762.70, "divyld": 0.11, "npqtr": 278.97, "qpv": -4.48, "salesqtr": 5800.99, "qsv": 20.55, "roce": 21.83, "ret3m": 39.08},
    {"name": "Hind Rectifiers", "symbol": "HIRECT", "cmp": 917.50, "pe": 60.06, "mcap": 3153.74, "divyld": 0.11, "npqtr": 13.73, "qpv": 47.85, "salesqtr": 243.27, "qsv": 44.00, "roce": 21.60, "ret3m": 51.94},
    {"name": "KSH Internationa", "symbol": "KSHINTL", "cmp": 624.60, "pe": 63.28, "mcap": 4227.41, "divyld": 0.00, "npqtr": 23.33, "qpv": -4.62, "salesqtr": 817.77, "qsv": 58.52, "roce": 21.45, "ret3m": 79.02},
    {"name": "Indian Metals", "symbol": "IMFA", "cmp": 1551.60, "pe": 22.73, "mcap": 8375.10, "divyld": 1.29, "npqtr": 131.46, "qpv": 40.69, "salesqtr": 702.83, "qsv": 9.27, "roce": 21.29, "ret3m": 40.14},
    {"name": "Welspun Corp", "symbol": "WELCORP", "cmp": 1204.10, "pe": 20.48, "mcap": 31776.98, "divyld": 0.42, "npqtr": 456.36, "qpv": -32.91, "salesqtr": 4532.48, "qsv": 25.43, "roce": 21.24, "ret3m": 64.81},
    {"name": "Sky Gold & Diam.", "symbol": "SKYGOLD", "cmp": 411.65, "pe": 27.78, "mcap": 6369.34, "divyld": 0.00, "npqtr": 80.54, "qpv": 120.42, "salesqtr": 1767.68, "qsv": 77.13, "roce": 21.21, "ret3m": 36.53},
    {"name": "Elecon Engg.Co", "symbol": "ELECON", "cmp": 512.75, "pe": 32.20, "mcap": 11500.40, "divyld": 0.39, "npqtr": 6.00, "qpv": -50.66, "salesqtr": 745.61, "qsv": -6.51, "roce": 21.04, "ret3m": 36.73},
    {"name": "Data Pattern", "symbol": "DATAPATTNS", "cmp": 4135.10, "pe": 92.86, "mcap": 23158.70, "divyld": 0.19, "npqtr": 58.30, "qpv": 35.76, "salesqtr": 173.13, "qsv": 47.92, "roce": 21.00, "ret3m": 89.47},
    {"name": "KRN Heat Exchan", "symbol": "KRN", "cmp": 1284.10, "pe": 117.43, "mcap": 7981.52, "divyld": 0.00, "npqtr": 22.66, "qpv": 65.04, "salesqtr": 153.23, "qsv": 37.46, "roce": 20.75, "ret3m": 114.70},
    {"name": "Garware Hi Tech", "symbol": "GARFIBRES", "cmp": 4195.70, "pe": 31.65, "mcap": 9742.80, "divyld": 0.29, "npqtr": 55.77, "qpv": -8.29, "salesqtr": 458.74, "qsv": -1.64, "roce": 20.57, "ret3m": 42.92},
    {"name": "Park Medi World", "symbol": "PARKHOSPS", "cmp": 228.84, "pe": 46.72, "mcap": 9889.85, "divyld": 0.00, "npqtr": 52.85, "qpv": 11.38, "salesqtr": 409.97, "qsv": 17.76, "roce": 20.36, "ret3m": 46.56},
    {"name": "Ram Ratna Wires", "symbol": "RRWL", "cmp": 387.15, "pe": 40.79, "mcap": 3616.81, "divyld": 0.32, "npqtr": 31.64, "qpv": 106.33, "salesqtr": 1277.94, "qsv": 43.80, "roce": 20.17, "ret3m": 33.16},
    {"name": "Acutaas Chemical", "symbol": "ACUTAAS", "cmp": 2386.70, "pe": 68.11, "mcap": 19545.83, "divyld": 0.06, "npqtr": 106.22, "qpv": 140.18, "salesqtr": 393.18, "qsv": 42.98, "roce": 19.92, "ret3m": 44.35},
    {"name": "GNG Electronics", "symbol": "EBGNG", "cmp": 370.10, "pe": 40.37, "mcap": 4223.52, "divyld": 0.00, "npqtr": 38.69, "qpv": 102.78, "salesqtr": 487.22, "qsv": 40.26, "roce": 19.84, "ret3m": 46.87},
    {"name": "Va Tech Wabag", "symbol": "WABAG", "cmp": 1464.80, "pe": 26.41, "mcap": 9121.59, "divyld": 0.27, "npqtr": 91.30, "qpv": 35.67, "salesqtr": 961.30, "qsv": 18.53, "roce": 19.70, "ret3m": 38.05},
    {"name": "Aditya Infotech", "symbol": "CPPLUS", "cmp": 2268.30, "pe": 105.00, "mcap": 26648.75, "divyld": 0.00, "npqtr": 95.98, "qpv": 138.82, "salesqtr": 1139.11, "qsv": 37.32, "roce": 19.49, "ret3m": 62.60},
    {"name": "Hitachi Energy", "symbol": "POWERINDIA", "cmp": 31720.00, "pe": 160.30, "mcap": 141389.60, "divyld": 0.02, "npqtr": 261.42, "qpv": 119.97, "salesqtr": 2082.21, "qsv": 28.51, "roce": 19.44, "ret3m": 92.23},
    {"name": "Jindal Saw", "symbol": "JINDALSAW", "cmp": 245.28, "pe": 13.94, "mcap": 15687.14, "divyld": 0.82, "npqtr": 247.62, "qpv": -49.06, "salesqtr": 4943.41, "qsv": -6.22, "roce": 19.37, "ret3m": 38.01},
    {"name": "Gallantt Ispat L", "symbol": "GALLANTT", "cmp": 842.50, "pe": 42.34, "mcap": 20297.61, "divyld": 0.15, "npqtr": 100.41, "qpv": -11.67, "salesqtr": 1073.58, "qsv": -4.00, "roce": 19.20, "ret3m": 57.27},
    {"name": "Happy Forgings", "symbol": "HAPPYFORGNG", "cmp": 1349.50, "pe": 44.53, "mcap": 12728.29, "divyld": 0.22, "npqtr": 78.95, "qpv": 22.37, "salesqtr": 391.31, "qsv": 10.44, "roce": 19.17, "ret3m": 32.02},
    {"name": "Praj Industries", "symbol": "PRAJIND", "cmp": 410.05, "pe": 102.13, "mcap": 7543.17, "divyld": 1.46, "npqtr": -12.39, "qpv": -77.06, "salesqtr": 841.49, "qsv": -1.35, "roce": 17.92, "ret3m": 44.61},
    {"name": "Finolex Cables", "symbol": "FINCABLES", "cmp": 968.40, "pe": 21.76, "mcap": 14816.72, "divyld": 0.83, "npqtr": 164.03, "qpv": 11.40, "salesqtr": 1598.62, "qsv": 35.23, "roce": 17.67, "ret3m": 34.17},
    {"name": "Cupid", "symbol": "CUPID", "cmp": 113.13, "pe": 182.03, "mcap": 15210.80, "divyld": 0.00, "npqtr": 32.87, "qpv": 196.66, "salesqtr": 104.40, "qsv": 105.67, "roce": 17.10, "ret3m": 42.41},
    {"name": "Techno Elec.Engg", "symbol": "TECHNOE", "cmp": 1249.25, "pe": 30.92, "mcap": 14497.41, "divyld": 0.72, "npqtr": 119.25, "qpv": 24.23, "salesqtr": 872.20, "qsv": 37.12, "roce": 16.54, "ret3m": 39.83},
    {"name": "Sharda Cropchem", "symbol": "SHARDACROP", "cmp": 1111.05, "pe": 17.74, "mcap": 10036.07, "divyld": 0.81, "npqtr": 145.11, "qpv": 365.87, "salesqtr": 1288.76, "qsv": 38.68, "roce": 16.50, "ret3m": 37.79},
    {"name": "Thermax", "symbol": "THERMAX", "cmp": 4059.70, "pe": 75.49, "mcap": 48371.50, "divyld": 0.34, "npqtr": 205.01, "qpv": 40.63, "salesqtr": 2634.68, "qsv": 4.19, "roce": 16.22, "ret3m": 39.00},
    {"name": "Marine Electric.", "symbol": "MARINEELEC", "cmp": 236.47, "pe": 62.13, "mcap": 3309.26, "divyld": 0.13, "npqtr": 11.83, "qpv": 126.97, "salesqtr": 210.23, "qsv": 8.48, "roce": 16.06, "ret3m": 38.70},
    {"name": "Man Industries", "symbol": "MANINDS", "cmp": 542.85, "pe": 21.68, "mcap": 4070.80, "divyld": 0.00, "npqtr": 55.04, "qpv": 61.31, "salesqtr": 830.38, "qsv": 13.45, "roce": 15.98, "ret3m": 73.05},
    {"name": "Torrent Power", "symbol": "TORNTPOWER", "cmp": 1737.00, "pe": 27.72, "mcap": 87538.61, "divyld": 1.09, "npqtr": 654.74, "qpv": 35.20, "salesqtr": 6777.87, "qsv": 4.28, "roce": 15.95, "ret3m": 36.70},
    {"name": "Siemens", "symbol": "SIEMENS", "cmp": 3864.40, "pe": 84.13, "mcap": 137590.58, "divyld": 0.00, "npqtr": 277.80, "qpv": -10.62, "salesqtr": 3830.70, "qsv": 14.01, "roce": 15.83, "ret3m": 33.24},
    {"name": "Paras Defence", "symbol": "PARAS", "cmp": 829.60, "pe": 90.96, "mcap": 6679.80, "divyld": 0.03, "npqtr": 16.85, "qpv": 21.08, "salesqtr": 106.35, "qsv": 23.99, "roce": 15.61, "ret3m": 33.17},
    {"name": "ISGEC Heavy", "symbol": "ISGEC", "cmp": 1069.55, "pe": 24.00, "mcap": 7859.18, "divyld": 0.47, "npqtr": 84.44, "qpv": 102.88, "salesqtr": 1738.56, "qsv": 16.26, "roce": 14.83, "ret3m": 45.13},
    {"name": "Strides Pharma", "symbol": "STAR", "cmp": 1069.00, "pe": 17.94, "mcap": 9855.73, "divyld": 0.37, "npqtr": 208.13, "qpv": 128.03, "salesqtr": 1194.65, "qsv": 3.55, "roce": 14.68, "ret3m": 34.25},
    {"name": "Amber Enterp.", "symbol": "AMBER", "cmp": 7795.00, "pe": 118.13, "mcap": 27457.77, "divyld": 0.00, "npqtr": -9.34, "qpv": 26.43, "salesqtr": 2942.82, "qsv": 37.94, "roce": 14.49, "ret3m": 40.06},
    {"name": "Belrise Industri", "symbol": "BELRISE", "cmp": 217.60, "pe": 40.24, "mcap": 19366.39, "divyld": 0.25, "npqtr": 121.97, "qpv": 25.79, "salesqtr": 2340.52, "qsv": 8.02, "roce": 14.30, "ret3m": 36.10},
    {"name": "Rashi Peripheral", "symbol": "RASHI", "cmp": 475.90, "pe": 12.96, "mcap": 3146.42, "divyld": 0.42, "npqtr": 74.60, "qpv": 131.00, "salesqtr": 4030.41, "qsv": 42.60, "roce": 14.19, "ret3m": 40.86},
    {"name": "TruAlt Bioenergy", "symbol": "TRUALT", "cmp": 488.40, "pe": 28.34, "mcap": 4188.61, "divyld": 0.00, "npqtr": 69.19, "qpv": -7.79, "salesqtr": 713.24, "qsv": 71.82, "roce": 14.18, "ret3m": 52.79},
    {"name": "G M D C", "symbol": "GMDCLTD", "cmp": 682.85, "pe": 33.92, "mcap": 21697.37, "divyld": 1.48, "npqtr": 133.06, "qpv": -9.89, "salesqtr": 579.15, "qsv": -11.37, "roce": 14.06, "ret3m": 31.62},
    {"name": "Sai Life", "symbol": "SAILIFE", "cmp": 1041.60, "pe": 64.99, "mcap": 22042.49, "divyld": 0.00, "npqtr": 100.38, "qpv": 97.92, "salesqtr": 556.46, "qsv": 26.53, "roce": 14.05, "ret3m": 31.02},
    {"name": "Yatharth Hospit.", "symbol": "YATHARTH", "cmp": 756.65, "pe": 43.55, "mcap": 7287.70, "divyld": 0.00, "npqtr": 43.08, "qpv": 48.74, "salesqtr": 320.47, "qsv": 46.23, "roce": 13.99, "ret3m": 37.37},
    {"name": "Apollo Micro Sys", "symbol": "APOLLOMICRO", "cmp": 290.96, "pe": 116.39, "mcap": 10393.98, "divyld": 0.09, "npqtr": 22.88, "qpv": 40.64, "salesqtr": 252.22, "qsv": 69.97, "roce": 13.98, "ret3m": 30.83},
    {"name": "Sambhv Steel", "symbol": "SAMBHV", "cmp": 119.27, "pe": 33.82, "mcap": 3516.29, "divyld": 0.00, "npqtr": 24.13, "qpv": 112.79, "salesqtr": 589.14, "qsv": 59.64, "roce": 13.92, "ret3m": 38.32},
    {"name": "AXISCADES Tech.", "symbol": "AXISCADES", "cmp": 1992.70, "pe": 77.17, "mcap": 8466.72, "divyld": 0.00, "npqtr": 27.66, "qpv": 110.65, "salesqtr": 343.18, "qsv": 25.01, "roce": 13.76, "ret3m": 72.92},
    {"name": "Kirloskar Oil", "symbol": "KIRLOSENG", "cmp": 1610.30, "pe": 43.07, "mcap": 23408.62, "divyld": 0.40, "npqtr": 109.13, "qpv": 79.61, "salesqtr": 1872.60, "qsv": 28.82, "roce": 13.68, "ret3m": 47.17},
    {"name": "Sansera Enginee.", "symbol": "SANSERA", "cmp": 2525.50, "pe": 57.55, "mcap": 15749.69, "divyld": 0.13, "npqtr": 69.42, "qpv": 44.51, "salesqtr": 907.67, "qsv": 24.71, "roce": 13.38, "ret3m": 52.05},
    {"name": "Paisalo Digital", "symbol": "PAISALO", "cmp": 44.62, "pe": 19.15, "mcap": 4045.11, "divyld": 0.22, "npqtr": 66.26, "qpv": 7.06, "salesqtr": 240.05, "qsv": 17.82, "roce": 13.13, "ret3m": 36.66},
    {"name": "Arvind Ltd", "symbol": "ARVIND", "cmp": 388.80, "pe": 24.24, "mcap": 10198.82, "divyld": 0.96, "npqtr": 100.97, "qpv": 9.29, "salesqtr": 2372.64, "qsv": 13.57, "roce": 13.04, "ret3m": 30.40},
    {"name": "Avalon Tech", "symbol": "AVALONTECH", "cmp": 1088.50, "pe": 75.59, "mcap": 7262.11, "divyld": 0.00, "npqtr": 32.60, "qpv": 35.89, "salesqtr": 417.54, "qsv": 48.67, "roce": 12.76, "ret3m": 35.50},
    {"name": "Jayaswal Neco", "symbol": "JAYNECOIND", "cmp": 97.23, "pe": 24.72, "mcap": 9428.42, "divyld": 0.00, "npqtr": 74.09, "qpv": 6.08, "salesqtr": 1727.23, "qsv": 4.25, "roce": 12.59, "ret3m": 35.87},
    {"name": "Lux Industries", "symbol": "LUXIND", "cmp": 1747.05, "pe": 46.11, "mcap": 5225.70, "divyld": 0.11, "npqtr": 13.32, "qpv": -46.66, "salesqtr": 672.53, "qsv": 21.59, "roce": 12.54, "ret3m": 95.38},
    {"name": "Azad Engineering", "symbol": "AZAD", "cmp": 2111.00, "pe": 110.93, "mcap": 13651.05, "divyld": 0.00, "npqtr": 34.04, "qpv": 40.14, "salesqtr": 155.80, "qsv": 31.38, "roce": 12.23, "ret3m": 51.74},
    {"name": "SMS Pharma.", "symbol": "SMSPHARMA", "cmp": 415.55, "pe": 44.65, "mcap": 3898.21, "divyld": 0.10, "npqtr": 23.34, "qpv": 35.93, "salesqtr": 210.45, "qsv": 21.40, "roce": 12.19, "ret3m": 36.69},
    {"name": "Bharat Forge", "symbol": "BHARATFORG", "cmp": 1874.10, "pe": 76.77, "mcap": 89643.34, "divyld": 0.45, "npqtr": 272.80, "qpv": 40.77, "salesqtr": 4342.93, "qsv": 24.96, "roce": 12.18, "ret3m": 33.03},
    {"name": "Deep Industries", "symbol": "DEEPINDS", "cmp": 488.00, "pe": 13.47, "mcap": 3121.90, "divyld": 0.62, "npqtr": 71.35, "qpv": 56.07, "salesqtr": 221.50, "qsv": 43.06, "roce": 12.06, "ret3m": 41.65},
    {"name": "Centum Electron", "symbol": "CENTUM", "cmp": 2888.70, "pe": 76.48, "mcap": 4254.52, "divyld": 0.21, "npqtr": -61.75, "qpv": 423.59, "salesqtr": 331.44, "qsv": 21.39, "roce": 12.03, "ret3m": 31.13},
    {"name": "Syrma SGS Tech.", "symbol": "SYRMA", "cmp": 983.50, "pe": 66.64, "mcap": 18961.08, "divyld": 0.15, "npqtr": 110.32, "qpv": 108.80, "salesqtr": 1264.18, "qsv": 45.36, "roce": 11.67, "ret3m": 47.82},
    {"name": "SG Mart", "symbol": "SGMART", "cmp": 544.70, "pe": 66.77, "mcap": 6859.44, "divyld": 0.00, "npqtr": 10.74, "qpv": -61.70, "salesqtr": 1644.43, "qsv": 23.21, "roce": 11.33, "ret3m": 55.94},
    {"name": "Vardhman Textile", "symbol": "VTL", "cmp": 569.40, "pe": 20.66, "mcap": 16486.27, "divyld": 0.88, "npqtr": 168.50, "qpv": -21.02, "salesqtr": 2505.31, "qsv": 1.62, "roce": 10.83, "ret3m": 41.13},
    {"name": "Gokaldas Exports", "symbol": "GOKEX", "cmp": 725.80, "pe": 45.39, "mcap": 5310.97, "divyld": 0.00, "npqtr": 14.61, "qpv": -70.98, "salesqtr": 978.65, "qsv": -0.92, "roce": 10.62, "ret3m": 30.20},
    {"name": "MTAR Technologies", "symbol": "MTARTECH", "cmp": 5347.50, "pe": 242.43, "mcap": 16456.48, "divyld": 0.00, "npqtr": 35.17, "qpv": 131.84, "salesqtr": 277.90, "qsv": 59.30, "roce": 10.51, "ret3m": 122.79},
    {"name": "JP Power Ven.", "symbol": "JPPOWER", "cmp": 19.88, "pe": 22.02, "mcap": 13645.01, "divyld": 0.00, "npqtr": 3.77, "qpv": -97.02, "salesqtr": 1155.57, "qsv": 1.35, "roce": 10.26, "ret3m": 34.78},
    {"name": "Balrampur Chini", "symbol": "BALRAMCHIN", "cmp": 540.30, "pe": 24.35, "mcap": 10910.38, "divyld": 0.65, "npqtr": 113.43, "qpv": 60.96, "salesqtr": 1454.12, "qsv": 21.97, "roce": 10.16, "ret3m": 30.82},
    {"name": "S C I", "symbol": "SCI", "cmp": 292.60, "pe": 12.03, "mcap": 13638.01, "divyld": 2.25, "npqtr": 404.97, "qpv": 436.24, "salesqtr": 1611.67, "qsv": 22.50, "roce": 9.81, "ret3m": 45.04},
    {"name": "Power Fin.Corpn.", "symbol": "PFC", "cmp": 469.80, "pe": 6.15, "mcap": 155088.25, "divyld": 3.36, "npqtr": 8211.90, "qpv": 8.14, "salesqtr": 29094.81, "qsv": 8.57, "roce": 9.73, "ret3m": 30.99},
    {"name": "Adani Energy Sol", "symbol": "ADANIENSOL", "cmp": 1361.25, "pe": 71.53, "mcap": 163268.02, "divyld": 0.00, "npqtr": 722.65, "qpv": 5.66, "salesqtr": 7443.27, "qsv": 16.76, "roce": 9.71, "ret3m": 67.50},
    {"name": "Dalmia Bharat", "symbol": "DALMIASUG", "cmp": 399.20, "pe": 9.56, "mcap": 3235.92, "divyld": 1.50, "npqtr": 69.77, "qpv": 17.64, "salesqtr": 697.75, "qsv": -16.70, "roce": 9.48, "ret3m": 45.53},
    {"name": "SG Finserve", "symbol": "SGFIN", "cmp": 543.00, "pe": 28.03, "mcap": 3577.76, "divyld": 0.00, "npqtr": 42.27, "qpv": 77.68, "salesqtr": 105.41, "qsv": 94.88, "roce": 9.32, "ret3m": 44.51},
    {"name": "Dynamatic Tech.", "symbol": "DYNAMATECH", "cmp": 11677.50, "pe": 168.54, "mcap": 7890.98, "divyld": 0.04, "npqtr": 5.77, "qpv": 316.15, "salesqtr": 424.87, "qsv": 34.70, "roce": 8.96, "ret3m": 47.83},
    {"name": "Neogen Chemicals", "symbol": "NEOGEN", "cmp": 1660.00, "pe": 171.50, "mcap": 4550.02, "divyld": 0.06, "npqtr": 3.69, "qpv": -63.14, "salesqtr": 220.02, "qsv": 9.23, "roce": 8.82, "ret3m": 46.68},
    {"name": "Sigma Advanced", "symbol": "SIGMAADV", "cmp": 238.33, "pe": 29.37, "mcap": 4206.63, "divyld": 0.00, "npqtr": -1.03, "qpv": 3.15, "salesqtr": 145.70, "qsv": 667.25, "roce": 8.74, "ret3m": 36.54},
    {"name": "Adani Green", "symbol": "ADANIGREEN", "cmp": 1214.15, "pe": 121.40, "mcap": 200167.20, "divyld": 0.00, "npqtr": 5.00, "qpv": -106.78, "salesqtr": 2618.00, "qsv": 11.88, "roce": 8.70, "ret3m": 57.11},
    {"name": "SEAMEC Ltd", "symbol": "SEAMECLTD", "cmp": 1544.00, "pe": 20.58, "mcap": 3927.82, "divyld": 0.00, "npqtr": 99.76, "qpv": 3100.60, "salesqtr": 317.05, "qsv": 112.30, "roce": 8.60, "ret3m": 36.46},
    {"name": "ACME Solar Hold.", "symbol": "ACMESOLAR", "cmp": 309.20, "pe": 37.34, "mcap": 18736.64, "divyld": 0.06, "npqtr": 113.70, "qpv": -3.66, "salesqtr": 496.79, "qsv": 42.34, "roce": 8.42, "ret3m": 55.41},
    {"name": "Rossell Techsys", "symbol": "ROSSELLIND", "cmp": 930.65, "pe": 159.35, "mcap": 3500.98, "divyld": 0.02, "npqtr": 5.41, "qpv": 18.27, "salesqtr": 129.93, "qsv": 71.55, "roce": 8.18, "ret3m": 50.09},
    {"name": "Prime Focus", "symbol": "PFOCUS", "cmp": 324.00, "pe": 95.58, "mcap": 25142.10, "divyld": 0.00, "npqtr": 69.20, "qpv": 237.06, "salesqtr": 1207.24, "qsv": 32.74, "roce": 7.95, "ret3m": 48.95},
    {"name": "Shilpa Medicare", "symbol": "SHILPAMED", "cmp": 427.60, "pe": 47.34, "mcap": 8375.38, "divyld": 0.12, "npqtr": 44.58, "qpv": 69.92, "salesqtr": 409.73, "qsv": 28.32, "roce": 7.82, "ret3m": 60.15},
    {"name": "HFCL", "symbol": "HFCL", "cmp": 97.75, "pe": 288.92, "mcap": 14969.10, "divyld": 0.10, "npqtr": 102.37, "qpv": 32.55, "salesqtr": 1210.79, "qsv": 19.65, "roce": 7.55, "ret3m": 59.98},
    {"name": "Mahindra Logis.", "symbol": "MAHLOG", "cmp": 442.70, "pe": 1748.96, "mcap": 4406.77, "divyld": 0.56, "npqtr": 22.36, "qpv": 399.11, "salesqtr": 1791.41, "qsv": 14.14, "roce": 7.28, "ret3m": 52.50},
    {"name": "NOCIL", "symbol": "NOCIL", "cmp": 182.60, "pe": 48.51, "mcap": 3049.53, "divyld": 1.10, "npqtr": 9.25, "qpv": -1.63, "salesqtr": 315.84, "qsv": -0.72, "roce": 6.65, "ret3m": 42.40},
    {"name": "Karnataka Bank", "symbol": "KTKBANK", "cmp": 244.97, "pe": 8.02, "mcap": 9262.09, "divyld": 2.04, "npqtr": 290.79, "qpv": 2.54, "salesqtr": 2220.05, "qsv": -1.02, "roce": 6.33, "ret3m": 36.81},
    {"name": "Aarti Industries", "symbol": "AARTIIND", "cmp": 465.90, "pe": 45.56, "mcap": 16904.05, "divyld": 0.21, "npqtr": 133.00, "qpv": 221.74, "salesqtr": 2318.00, "qsv": 25.77, "roce": 6.32, "ret3m": 32.06},
    {"name": "GE Power", "symbol": "GEPOWERINF", "cmp": 527.75, "pe": 21.25, "mcap": 3567.81, "divyld": 0.00, "npqtr": 72.32, "qpv": 431.62, "salesqtr": 385.62, "qsv": 21.69, "roce": 6.09, "ret3m": 87.21},
    {"name": "Sindhu Trade", "symbol": "SINDHUTR", "cmp": 23.64, "pe": 3658.85, "mcap": None, "divyld": 0.00, "npqtr": 13.87, "qpv": 285.68, "salesqtr": 119.15, "qsv": -76.68, "roce": 5.45, "ret3m": 31.92},
    {"name": "Jindal Poly Film", "symbol": "JINDALPOLY", "cmp": 709.90, "pe": None, "mcap": None, "divyld": 0.83, "npqtr": -96.92, "qpv": -453.42, "salesqtr": 371.66, "qsv": -68.66, "roce": 5.36, "ret3m": 84.27},
    {"name": "B H E L", "symbol": "BHEL", "cmp": 337.60, "pe": 144.41, "mcap": 117586.18, "divyld": 0.15, "npqtr": 390.40, "qpv": 189.83, "salesqtr": 8473.10, "qsv": 16.44, "roce": 4.87, "ret3m": 39.22},
    {"name": "Sterlite Tech.", "symbol": "STLTECH", "cmp": 276.45, "pe": None, "mcap": 13489.33, "divyld": 0.00, "npqtr": -17.00, "qpv": 53.33, "salesqtr": 1257.00, "qsv": 25.95, "roce": 2.86, "ret3m": 212.76},
    {"name": "Aequs", "symbol": "AEQUS", "cmp": 184.60, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": -42.68, "qpv": 17.87, "salesqtr": 326.17, "qsv": 50.77, "roce": 1.11, "ret3m": 37.22},
    {"name": "Gujarat Alkalies", "symbol": "GUJALKALI", "cmp": 721.10, "pe": None, "mcap": None, "divyld": 2.19, "npqtr": -19.95, "qpv": -77.65, "salesqtr": 1044.46, "qsv": 1.46, "roce": -0.34, "ret3m": 58.90},
    {"name": "E2E Networks", "symbol": "E2E", "cmp": 2906.50, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": 6.44, "qpv": -52.68, "salesqtr": 95.64, "qsv": 185.66, "roce": -0.51, "ret3m": 43.14},
    {"name": "Tejas Networks", "symbol": "TEJASNET", "cmp": 402.15, "pe": None, "mcap": None, "divyld": 0.62, "npqtr": -211.34, "qpv": -194.35, "salesqtr": 332.69, "qsv": -82.55, "roce": -14.64, "ret3m": 32.26},
    {"name": "Ather Energy", "symbol": "ATHERENRGY", "cmp": 898.45, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": -84.60, "qpv": 59.76, "salesqtr": 953.60, "qsv": 50.20, "roce": -65.71, "ret3m": 44.63},
    {"name": "Suven Life Scie.", "symbol": "SUVENLIFE", "cmp": 207.66, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": -101.92, "qpv": -160.53, "salesqtr": 2.81, "qsv": 74.53, "roce": -86.96, "ret3m": 54.89},
    {"name": "Indiabulls", "symbol": "IBULHSGFIN", "cmp": 17.12, "pe": 138.49, "mcap": 3974.72, "divyld": 0.00, "npqtr": 78.37, "qpv": 2250.95, "salesqtr": 96.96, "qsv": -8.90, "roce": 49.65, "ret3m": None},
    {"name": "Lloyds Engineeri", "symbol": "LLOYDSENG", "cmp": 57.41, "pe": 49.73, "mcap": 8021.35, "divyld": 0.44, "npqtr": 66.70, "qpv": 70.86, "salesqtr": 272.45, "qsv": 2.34, "roce": 33.14, "ret3m": None},
]

def percentile_rank(values_with_idx):
    valid = [(idx, v) for idx, v in values_with_idx if v is not None]
    if not valid:
        return {}
    n = len(valid)
    if n == 1:
        return {valid[0][0]: 50.0}
    sorted_vals = sorted(set(v for _, v in valid))
    val_to_rank = {}
    for sv in sorted_vals:
        count_below = sum(1 for _, v in valid if v < sv)
        count_equal = sum(1 for _, v in valid if v == sv)
        val_to_rank[sv] = ((count_below + (count_equal - 1) / 2) / (n - 1)) * 100
    val_to_rank_map = {idx: val_to_rank[v] for idx, v in valid}
    return val_to_rank_map

metrics = ['qpv', 'qsv', 'roce', 'ret3m']
weights = {'qpv': 0.35, 'qsv': 0.35, 'roce': 0.20, 'ret3m': 0.10}

pct_ranks = {}
for m in metrics:
    values_with_idx = []
    for i, s in enumerate(stocks):
        v = s.get(m)
        if m == 'roce' and v is not None and v < 0:
            values_with_idx.append((i, None))
        else:
            values_with_idx.append((i, v))
    pct_ranks[m] = percentile_rank(values_with_idx)

for i, s in enumerate(stocks):
    score = 0.0
    flags = []
    for m in metrics:
        if i in pct_ranks[m]:
            score += weights[m] * pct_ranks[m][i]
        else:
            flags.append(f"{m}_zero")
    qpv = s.get('qpv')
    qsv = s.get('qsv')
    roce = s.get('roce')
    ret3m = s.get('ret3m')
    if qpv is not None and qpv <= 0:
        score -= 12
        flags.append("neg_qpv")
    if qsv is not None and qsv <= 0:
        score -= 12
        flags.append("neg_qsv")
    if roce is not None and roce < 15:
        score -= 8
        flags.append("low_roce")
    if roce is not None and roce < 0:
        score -= 12
        flags.append("neg_roce")
    if ret3m is not None and ret3m <= 0:
        score -= 8
        flags.append("neg_ret3m")
    s['prerank_score'] = round(score, 2)
    s['flags'] = flags

ranked = sorted(stocks, key=lambda x: x['prerank_score'], reverse=True)

print(f"{'Rank':<5} {'Symbol':<15} {'Name':<25} {'Score':<10} {'QPV%':<10} {'QSV%':<10} {'ROCE%':<8} {'3mR%':<8} Flags")
print("=" * 120)
for rank, s in enumerate(ranked, 1):
    marker = " <<<" if rank <= 20 else ""
    print(f"{rank:<5} {s['symbol']:<15} {s['name']:<25} {s['prerank_score']:<10} {str(s.get('qpv','')):<10} {str(s.get('qsv','')):<10} {str(s.get('roce','')):<8} {str(s.get('ret3m','')):<8} {','.join(s['flags'])}{marker}")

print(f"\nTotal: {len(stocks)}")
print(f"\nTop 20:")
for rank, s in enumerate(ranked[:20], 1):
    print(f"  {rank}. {s['symbol']} - {s['prerank_score']}")

top20 = []
for rank, s in enumerate(ranked[:20], 1):
    top20.append({"rank": rank, "symbol": s["symbol"], "name": s["name"],
                  "prerank_score": s["prerank_score"], "qpv": s["qpv"],
                  "qsv": s["qsv"], "roce": s["roce"], "ret3m": s["ret3m"],
                  "cmp": s["cmp"], "pe": s["pe"], "mcap": s["mcap"],
                  "divyld": s["divyld"], "npqtr": s["npqtr"],
                  "salesqtr": s["salesqtr"], "flags": s["flags"]})
with open("scripts/top20.json", "w") as f:
    json.dump(top20, f, indent=2)

full = []
for rank, s in enumerate(ranked, 1):
    full.append({"rank": rank, "symbol": s["symbol"], "name": s["name"],
                 "prerank_score": s["prerank_score"], "qpv": s["qpv"],
                 "qsv": s["qsv"], "roce": s["roce"], "ret3m": s["ret3m"],
                 "cmp": s["cmp"], "pe": s["pe"], "mcap": s["mcap"],
                 "divyld": s["divyld"], "npqtr": s["npqtr"],
                 "salesqtr": s["salesqtr"], "flags": s["flags"],
                 "in_working_universe": rank <= 20})
with open("scripts/full_universe.json", "w") as f:
    json.dump(full, f, indent=2)

print("\nSaved top20.json and full_universe.json")
