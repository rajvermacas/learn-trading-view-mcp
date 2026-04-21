#!/usr/bin/env python3
"""Compute PreRankScore for the screener universe."""
import json
import sys

stocks = [
    # Page 1
    {"name": "Shilchar Tech.", "symbol": "SHILCTECH", "cmp": 4966.80, "pe": 30.71, "mcap": 5684.57, "divyld": 0.25, "npqtr": 42.34, "qpv": 21.77, "salesqtr": 170.26, "qsv": 10.75, "roce": 71.30, "ret3m": 66.42},
    {"name": "Siemens Ener.Ind", "symbol": "ENRIN", "cmp": 3208.20, "pe": 93.66, "mcap": 114250.58, "divyld": 0.12, "npqtr": 312.90, "qpv": 51.67, "salesqtr": 1910.90, "qsv": 25.97, "roce": 67.75, "ret3m": 42.53},
    {"name": "Ingersoll-Rand", "symbol": "INGERRAND", "cmp": 4076.30, "pe": 46.42, "mcap": 12854.12, "divyld": 1.96, "npqtr": 71.89, "qpv": 15.75, "salesqtr": 455.48, "qsv": 19.39, "roce": 60.02, "ret3m": 30.47},
    {"name": "GE Vernova T&D", "symbol": "GVT&D", "cmp": 4252.10, "pe": 97.42, "mcap": 108863.44, "divyld": 0.12, "npqtr": 290.80, "qpv": 138.53, "salesqtr": 1700.64, "qsv": 58.40, "roce": 54.74, "ret3m": 66.24},
    {"name": "Saatvik Green", "symbol": "SAATVIKGL", "cmp": 461.85, "pe": 14.97, "mcap": 5867.19, "divyld": 0.00, "npqtr": 98.72, "qpv": 144.05, "salesqtr": 1257.02, "qsv": 142.58, "roce": 52.33, "ret3m": 31.36},
    {"name": "Atlanta Electric", "symbol": "ATLANTAELE", "cmp": 1377.00, "pe": 67.78, "mcap": 10585.99, "divyld": 0.00, "npqtr": 49.42, "qpv": 125.33, "salesqtr": 471.82, "qsv": 79.71, "roce": 50.20, "ret3m": 83.21},
    {"name": "BSE", "symbol": "BSE", "cmp": 3515.80, "pe": 65.64, "mcap": 143198.21, "divyld": 0.17, "npqtr": 596.59, "qpv": 175.79, "salesqtr": 1244.10, "qsv": 61.97, "roce": 46.57, "ret3m": 33.74},
    {"name": "Oriana Power Ltd", "symbol": "ORIANA", "cmp": 2120.35, "pe": 18.62, "mcap": 4308.37, "divyld": 0.00, "npqtr": 121.63, "qpv": 149.88, "salesqtr": 781.18, "qsv": 117.27, "roce": 42.31, "ret3m": 30.53},
    {"name": "Premier Energies", "symbol": "PREMIERENE", "cmp": 995.70, "pe": 33.92, "mcap": 45140.38, "divyld": 0.10, "npqtr": 391.62, "qpv": 53.48, "salesqtr": 1936.46, "qsv": 13.02, "roce": 41.12, "ret3m": 40.00},
    {"name": "Schneider Elect.", "symbol": "SCHNEIDER", "cmp": 1058.80, "pe": 97.04, "mcap": 25392.93, "divyld": 0.00, "npqtr": 97.03, "qpv": 16.65, "salesqtr": 1029.17, "qsv": 20.06, "roce": 40.90, "ret3m": 82.80},
    {"name": "Lloyds Metals", "symbol": "LLOYDSME", "cmp": 1649.90, "pe": 37.72, "mcap": 92922.36, "divyld": 0.06, "npqtr": 1089.56, "qpv": 169.05, "salesqtr": 5058.08, "qsv": 201.94, "roce": 38.28, "ret3m": 44.45},
    {"name": "Inox India", "symbol": "INOXINDIA", "cmp": 1482.60, "pe": 53.21, "mcap": 13454.77, "divyld": 0.13, "npqtr": 60.70, "qpv": 26.34, "salesqtr": 428.56, "qsv": 28.45, "roce": 37.98, "ret3m": 34.12},
    {"name": "CG Power & Ind", "symbol": "CGPOWER", "cmp": 805.25, "pe": 113.84, "mcap": 126670.55, "divyld": 0.16, "npqtr": 283.91, "qpv": 18.42, "salesqtr": 3175.35, "qsv": 26.22, "roce": 37.48, "ret3m": 39.97},
    {"name": "Billionbrains", "symbol": "IDEAFORGE", "cmp": 214.01, "pe": 64.34, "mcap": 134028.87, "divyld": 0.00, "npqtr": 686.35, "qpv": 122.06, "salesqtr": 1505.37, "qsv": 87.93, "roce": 37.38, "ret3m": 32.70},
    {"name": "Zen Technologies", "symbol": "ZENTEC", "cmp": 1742.70, "pe": 60.06, "mcap": 15754.55, "divyld": 0.11, "npqtr": 55.71, "qpv": 37.89, "salesqtr": 177.82, "qsv": 16.83, "roce": 37.22, "ret3m": 32.93},
    {"name": "Aditya AMC", "symbol": "ABSLAMC", "cmp": 1037.85, "pe": 29.44, "mcap": 29975.16, "divyld": 2.31, "npqtr": 269.52, "qpv": 21.01, "salesqtr": 478.08, "qsv": 7.41, "roce": 35.51, "ret3m": 32.73},
    {"name": "Waaree Energies", "symbol": "WAAREEENER", "cmp": 3472.80, "pe": 28.71, "mcap": 99949.99, "divyld": 0.06, "npqtr": 1106.79, "qpv": 158.06, "salesqtr": 7565.05, "qsv": 118.81, "roce": 34.94, "ret3m": 43.56},
    {"name": "Insolation Ener", "symbol": "INSOLATION", "cmp": 143.60, "pe": 17.85, "mcap": 3161.99, "divyld": 0.07, "npqtr": 50.72, "qpv": 173.57, "salesqtr": 575.34, "qsv": 77.05, "roce": 34.73, "ret3m": 41.13},
    {"name": "Gokul Agro", "symbol": "GOKULAGRO", "cmp": 210.28, "pe": 20.73, "mcap": 6202.07, "divyld": 0.00, "npqtr": 77.70, "qpv": 7.17, "salesqtr": 6314.25, "qsv": 26.58, "roce": 34.20, "ret3m": 35.92},
    {"name": "Steelcast", "symbol": "STEELCAST", "cmp": 296.79, "pe": 33.32, "mcap": 3013.82, "divyld": 0.49, "npqtr": 20.59, "qpv": 7.18, "salesqtr": 97.40, "qsv": -4.33, "roce": 32.94, "ret3m": 62.75},
    {"name": "Apar Inds.", "symbol": "APARINDS", "cmp": 11714.00, "pe": 47.45, "mcap": 47052.77, "divyld": 0.44, "npqtr": 208.93, "qpv": 29.80, "salesqtr": 5479.73, "qsv": 16.18, "roce": 32.70, "ret3m": 68.16},
    {"name": "Bajaj Consumer", "symbol": "BAJAJCON", "cmp": 458.90, "pe": 31.52, "mcap": 5994.08, "divyld": 0.00, "npqtr": 63.60, "qpv": 105.29, "salesqtr": 326.66, "qsv": 30.41, "roce": 30.60, "ret3m": 85.45},
    {"name": "TD Power Systems", "symbol": "TDPOWERSYS", "cmp": 1017.45, "pe": 72.40, "mcap": 15898.70, "divyld": 0.12, "npqtr": 56.32, "qpv": 25.35, "salesqtr": 442.68, "qsv": 26.36, "roce": 30.35, "ret3m": 60.20},
    {"name": "A B B", "symbol": "ABB", "cmp": 7255.00, "pe": 92.11, "mcap": 153788.94, "divyld": 0.54, "npqtr": 432.85, "qpv": -18.35, "salesqtr": 3557.01, "qsv": 5.71, "roce": 29.93, "ret3m": 54.12},
    {"name": "Volt.Transform.", "symbol": "VOLTAMP", "cmp": 10524.50, "pe": 30.09, "mcap": 10660.85, "divyld": 0.95, "npqtr": 99.08, "qpv": 34.99, "salesqtr": 630.32, "qsv": 30.36, "roce": 29.11, "ret3m": 55.26},
    # Page 2
    {"name": "Emmvee Photovol.", "symbol": "EMMVEE", "cmp": 261.31, "pe": 33.94, "mcap": 18104.84, "divyld": 0.00, "npqtr": 263.64, "qpv": 165.77, "salesqtr": 1152.25, "qsv": 118.11, "roce": 28.01, "ret3m": 33.77},
    {"name": "T R I L", "symbol": "TRIL", "cmp": 333.30, "pe": 37.52, "mcap": 10007.64, "divyld": 0.06, "npqtr": 75.97, "qpv": 34.89, "salesqtr": 736.76, "qsv": 31.71, "roce": 27.97, "ret3m": 36.94},
    {"name": "Krishana Phosch.", "symbol": "KRISHANA", "cmp": 623.65, "pe": 20.96, "mcap": 3776.37, "divyld": 0.08, "npqtr": 83.08, "qpv": 152.83, "salesqtr": 755.49, "qsv": 59.76, "roce": 27.24, "ret3m": 32.56},
    {"name": "Prec. Wires (I)", "symbol": "PRECWIRE", "cmp": 386.95, "pe": 54.41, "mcap": 7072.78, "divyld": 0.30, "npqtr": 37.70, "qpv": 98.94, "salesqtr": 1347.61, "qsv": 37.19, "roce": 26.78, "ret3m": 76.65},
    {"name": "Quality Power El", "symbol": "QPOWER", "cmp": 1265.35, "pe": 91.54, "mcap": 9795.94, "divyld": 0.08, "npqtr": 62.76, "qpv": 169.18, "salesqtr": 283.99, "qsv": 291.22, "roce": 26.60, "ret3m": 91.84},
    {"name": "Rubicon Research", "symbol": "RUBICON", "cmp": 921.35, "pe": 89.88, "mcap": 15139.29, "divyld": 0.00, "npqtr": 72.80, "qpv": 91.23, "salesqtr": 475.53, "qsv": 51.73, "roce": 26.05, "ret3m": 39.73},
    {"name": "Shriram Pistons", "symbol": "SHRIPISTON", "cmp": 3586.80, "pe": 28.15, "mcap": 15801.31, "divyld": 0.28, "npqtr": 125.70, "qpv": 17.91, "salesqtr": 1023.20, "qsv": 20.67, "roce": 25.70, "ret3m": 30.49},
    {"name": "Engineers India", "symbol": "ENGINERSIN", "cmp": 243.24, "pe": 17.63, "mcap": 13677.34, "divyld": 1.64, "npqtr": 347.17, "qpv": 219.30, "salesqtr": 1210.24, "qsv": 58.29, "roce": 25.01, "ret3m": 36.23},
    {"name": "Goldiam Intl.", "symbol": "GOLDIAM", "cmp": 411.50, "pe": 29.72, "mcap": 4652.28, "divyld": 0.73, "npqtr": 68.39, "qpv": 37.52, "salesqtr": 319.71, "qsv": 14.33, "roce": 24.59, "ret3m": 40.68},
    {"name": "KSB", "symbol": "KSB", "cmp": 990.05, "pe": 59.75, "mcap": 17259.75, "divyld": 0.44, "npqtr": 81.00, "qpv": 33.43, "salesqtr": 784.00, "qsv": 7.93, "roce": 24.52, "ret3m": 44.63},
    {"name": "Skipper", "symbol": "SKIPPER", "cmp": 465.20, "pe": 28.57, "mcap": 5250.83, "divyld": 0.02, "npqtr": 50.17, "qpv": 39.71, "salesqtr": 1370.59, "qsv": 20.73, "roce": 24.42, "ret3m": 36.48},
    {"name": "Avanti Feeds", "symbol": "AVANTIFEED", "cmp": 1463.00, "pe": 31.60, "mcap": 19989.91, "divyld": 0.62, "npqtr": 163.47, "qpv": 10.40, "salesqtr": 1383.52, "qsv": 1.31, "roce": 23.99, "ret3m": 95.94},
    {"name": "Manorama Indust.", "symbol": "MANORAMA", "cmp": 1447.70, "pe": 39.95, "mcap": 8628.42, "divyld": 0.04, "npqtr": 68.24, "qpv": 131.09, "salesqtr": 362.54, "qsv": 73.30, "roce": 23.03, "ret3m": 32.74},
    {"name": "Rolex Rings", "symbol": "ROLEXRINGS", "cmp": 161.76, "pe": 22.29, "mcap": 4407.79, "divyld": 0.00, "npqtr": 47.75, "qpv": 57.61, "salesqtr": 274.84, "qsv": 5.76, "roce": 22.81, "ret3m": 35.81},
    {"name": "Supreme Petroch.", "symbol": "SUPPETRO", "cmp": 773.40, "pe": 53.69, "mcap": 14578.14, "divyld": 1.29, "npqtr": 30.15, "qpv": -50.25, "salesqtr": 1264.69, "qsv": -10.01, "roce": 22.76, "ret3m": 46.39},
    {"name": "Adani Power", "symbol": "ADANIPOWER", "cmp": 202.98, "pe": 34.18, "mcap": 391499.21, "divyld": 0.00, "npqtr": 2488.09, "qpv": -18.89, "salesqtr": 12451.44, "qsv": -8.92, "roce": 22.54, "ret3m": 47.48},
    {"name": "Aeroflex", "symbol": "AEROFLEX", "cmp": 289.11, "pe": 77.86, "mcap": 3824.42, "divyld": 0.10, "npqtr": 16.49, "qpv": 8.42, "salesqtr": 120.89, "qsv": 21.13, "roce": 22.34, "ret3m": 78.67},
    {"name": "AGI Infra", "symbol": "AGIIL", "cmp": 365.95, "pe": 54.58, "mcap": 4579.82, "divyld": 0.03, "npqtr": 26.11, "qpv": 36.92, "salesqtr": 87.50, "qsv": -4.28, "roce": 22.03, "ret3m": 33.36},
    {"name": "Hind Rectifiers", "symbol": "HIRECT", "cmp": 894.60, "pe": 58.65, "mcap": 3079.93, "divyld": 0.11, "npqtr": 13.73, "qpv": 47.85, "salesqtr": 243.27, "qsv": 44.00, "roce": 21.60, "ret3m": 43.41},
    {"name": "KSH Internationa", "symbol": "KSHINTL", "cmp": 601.85, "pe": 61.15, "mcap": 4084.77, "divyld": 0.00, "npqtr": 23.33, "qpv": -4.62, "salesqtr": 817.77, "qsv": 58.52, "roce": 21.45, "ret3m": 72.18},
    {"name": "Indian Metals", "symbol": "IMFA", "cmp": 1499.20, "pe": 21.97, "mcap": 8093.29, "divyld": 1.33, "npqtr": 131.46, "qpv": 40.69, "salesqtr": 702.83, "qsv": 9.27, "roce": 21.29, "ret3m": 37.18},
    {"name": "Welspun Corp", "symbol": "WELCORP", "cmp": 1100.60, "pe": 18.69, "mcap": 29005.86, "divyld": 0.45, "npqtr": 456.36, "qpv": -32.91, "salesqtr": 4532.48, "qsv": 25.43, "roce": 21.24, "ret3m": 46.68},
    {"name": "Data Pattern", "symbol": "DATAPATTNS", "cmp": 3526.40, "pe": 79.15, "mcap": 19740.76, "divyld": 0.22, "npqtr": 58.30, "qpv": 35.76, "salesqtr": 173.13, "qsv": 47.92, "roce": 21.00, "ret3m": 59.23},
    {"name": "KRN Heat Exchan", "symbol": "KRN", "cmp": 1212.80, "pe": 111.02, "mcap": 7545.92, "divyld": 0.00, "npqtr": 22.66, "qpv": 65.04, "salesqtr": 153.23, "qsv": 37.46, "roce": 20.75, "ret3m": 95.39},
    {"name": "Garware Hi Tech", "symbol": "GARFIBRES", "cmp": 3927.20, "pe": 29.70, "mcap": 9142.21, "divyld": 0.31, "npqtr": 55.77, "qpv": -8.29, "salesqtr": 458.74, "qsv": -1.64, "roce": 20.57, "ret3m": 45.21},
    # Page 3
    {"name": "Park Medi World", "symbol": "PARKHOSPS", "cmp": 224.31, "pe": 45.75, "mcap": 9686.02, "divyld": 0.00, "npqtr": 52.85, "qpv": 11.38, "salesqtr": 409.97, "qsv": 17.76, "roce": 20.36, "ret3m": 49.51},
    {"name": "Ram Ratna Wires", "symbol": "RRWL", "cmp": 389.65, "pe": 41.18, "mcap": 3651.07, "divyld": 0.32, "npqtr": 31.64, "qpv": 106.33, "salesqtr": 1277.94, "qsv": 43.80, "roce": 20.17, "ret3m": 38.35},
    {"name": "Acutaas Chemical", "symbol": "ACUTAAS", "cmp": 2374.40, "pe": 67.73, "mcap": 19435.85, "divyld": 0.06, "npqtr": 106.22, "qpv": 140.18, "salesqtr": 393.18, "qsv": 42.98, "roce": 19.92, "ret3m": 48.17},
    {"name": "GNG Electronics", "symbol": "EBGNG", "cmp": 415.65, "pe": 45.30, "mcap": 4739.46, "divyld": 0.00, "npqtr": 38.69, "qpv": 102.78, "salesqtr": 487.22, "qsv": 40.26, "roce": 19.84, "ret3m": 62.52},
    {"name": "Va Tech Wabag", "symbol": "WABAG", "cmp": 1487.10, "pe": 26.81, "mcap": 9258.25, "divyld": 0.27, "npqtr": 91.30, "qpv": 35.67, "salesqtr": 961.30, "qsv": 18.53, "roce": 19.70, "ret3m": 35.33},
    {"name": "Aditya Infotech", "symbol": "CPPLUS", "cmp": 2258.00, "pe": 104.75, "mcap": 26584.78, "divyld": 0.00, "npqtr": 95.98, "qpv": 138.82, "salesqtr": 1139.11, "qsv": 37.32, "roce": 19.49, "ret3m": 64.05},
    {"name": "Hitachi Energy", "symbol": "POWERINDIA", "cmp": 29890.00, "pe": 151.01, "mcap": 133193.78, "divyld": 0.02, "npqtr": 261.42, "qpv": 119.97, "salesqtr": 2082.21, "qsv": 28.51, "roce": 19.44, "ret3m": 79.10},
    {"name": "Gallantt Ispat L", "symbol": "GALLANTT", "cmp": 862.45, "pe": 43.44, "mcap": 20827.25, "divyld": 0.14, "npqtr": 100.41, "qpv": -11.67, "salesqtr": 1073.58, "qsv": -4.00, "roce": 19.20, "ret3m": 58.58},
    {"name": "Sona BLW Precis.", "symbol": "SONACOMS", "cmp": 581.30, "pe": 55.50, "mcap": 36204.47, "divyld": 0.55, "npqtr": 150.16, "qpv": 16.27, "salesqtr": 1199.76, "qsv": 38.24, "roce": 17.82, "ret3m": 30.79},
    {"name": "Finolex Cables", "symbol": "FINCABLES", "cmp": 953.50, "pe": 21.45, "mcap": 14605.91, "divyld": 0.84, "npqtr": 164.03, "qpv": 11.40, "salesqtr": 1598.62, "qsv": 35.23, "roce": 17.67, "ret3m": 33.65},
    {"name": "Nava", "symbol": "NAVA", "cmp": 692.00, "pe": 21.87, "mcap": 19569.75, "divyld": 1.16, "npqtr": 325.71, "qpv": -11.98, "salesqtr": 991.12, "qsv": 17.64, "roce": 17.17, "ret3m": 30.16},
    {"name": "Cupid", "symbol": "CUPID", "cmp": 109.92, "pe": 176.68, "mcap": 14763.70, "divyld": 0.00, "npqtr": 32.87, "qpv": 196.66, "salesqtr": 104.40, "qsv": 105.67, "roce": 17.10, "ret3m": 45.94},
    {"name": "Pitti Engg.", "symbol": "PITTIENG", "cmp": 921.80, "pe": 27.27, "mcap": 3472.91, "divyld": 0.16, "npqtr": 28.22, "qpv": -1.88, "salesqtr": 477.42, "qsv": 15.05, "roce": 17.05, "ret3m": 34.56},
    {"name": "Techno Elec.Engg", "symbol": "TECHNOE", "cmp": 1251.30, "pe": 31.00, "mcap": 14534.74, "divyld": 0.72, "npqtr": 119.25, "qpv": 24.23, "salesqtr": 872.20, "qsv": 37.12, "roce": 16.54, "ret3m": 37.85},
    {"name": "Sharda Cropchem", "symbol": "SHARDACROP", "cmp": 1107.90, "pe": 17.69, "mcap": 10006.88, "divyld": 0.81, "npqtr": 145.11, "qpv": 365.87, "salesqtr": 1288.76, "qsv": 38.68, "roce": 16.50, "ret3m": 37.98},
    {"name": "Thermax", "symbol": "THERMAX", "cmp": 4125.10, "pe": 76.76, "mcap": 49187.24, "divyld": 0.34, "npqtr": 205.01, "qpv": 40.63, "salesqtr": 2634.68, "qsv": 4.19, "roce": 16.22, "ret3m": 40.82},
    {"name": "Man Industries", "symbol": "MANINDS", "cmp": 531.75, "pe": 21.22, "mcap": 3985.29, "divyld": 0.00, "npqtr": 55.04, "qpv": 61.31, "salesqtr": 830.38, "qsv": 13.45, "roce": 15.98, "ret3m": 64.30},
    {"name": "ISGEC Heavy", "symbol": "ISGEC", "cmp": 1047.00, "pe": 23.37, "mcap": 7652.84, "divyld": 0.48, "npqtr": 84.44, "qpv": 102.88, "salesqtr": 1738.56, "qsv": 16.26, "roce": 14.83, "ret3m": 40.42},
    {"name": "Amber Enterp.", "symbol": "AMBER", "cmp": 7858.50, "pe": 119.14, "mcap": 27692.15, "divyld": 0.00, "npqtr": -9.34, "qpv": 26.43, "salesqtr": 2942.82, "qsv": 37.94, "roce": 14.49, "ret3m": 35.87},
    {"name": "Belrise Industri", "symbol": "BELRISE", "cmp": 219.05, "pe": 40.47, "mcap": 19473.53, "divyld": 0.25, "npqtr": 121.97, "qpv": 25.79, "salesqtr": 2340.52, "qsv": 8.02, "roce": 14.30, "ret3m": 32.51},
    {"name": "Rashi Peripheral", "symbol": "RASHI", "cmp": 474.35, "pe": 12.87, "mcap": 3125.62, "divyld": 0.42, "npqtr": 74.60, "qpv": 131.00, "salesqtr": 4030.41, "qsv": 42.60, "roce": 14.19, "ret3m": 34.68},
    {"name": "TruAlt Bioenergy", "symbol": "TRUALT", "cmp": 457.00, "pe": 26.51, "mcap": 3918.04, "divyld": 0.00, "npqtr": 69.19, "qpv": -7.79, "salesqtr": 713.24, "qsv": 71.82, "roce": 14.18, "ret3m": 35.53},
    {"name": "Sambhv Steel", "symbol": "SAMBHV", "cmp": 119.92, "pe": 33.94, "mcap": 3528.41, "divyld": 0.00, "npqtr": 24.13, "qpv": 112.79, "salesqtr": 589.14, "qsv": 59.64, "roce": 13.92, "ret3m": 42.80},
    {"name": "GE Shipping Co", "symbol": "GESHIP", "cmp": 1445.60, "pe": 9.13, "mcap": 20650.75, "divyld": 2.05, "npqtr": 812.52, "qpv": 142.21, "salesqtr": 1454.44, "qsv": 17.59, "roce": 13.86, "ret3m": 31.99},
    {"name": "AXISCADES Tech.", "symbol": "AXISCADES", "cmp": 1916.70, "pe": 74.03, "mcap": 8122.39, "divyld": 0.00, "npqtr": 27.66, "qpv": 110.65, "salesqtr": 343.18, "qsv": 25.01, "roce": 13.76, "ret3m": 71.26},
    # Page 4
    {"name": "Kirloskar Oil", "symbol": "KIRLOSENG", "cmp": 1663.30, "pe": 44.43, "mcap": 24150.36, "divyld": 0.39, "npqtr": 109.13, "qpv": 79.61, "salesqtr": 1872.60, "qsv": 28.82, "roce": 13.68, "ret3m": 50.80},
    {"name": "Sansera Enginee.", "symbol": "SANSERA", "cmp": 2374.60, "pe": 54.03, "mcap": 14787.40, "divyld": 0.14, "npqtr": 69.42, "qpv": 44.51, "salesqtr": 907.67, "qsv": 24.71, "roce": 13.38, "ret3m": 38.15},
    {"name": "Paisalo Digital", "symbol": "PAISALO", "cmp": 44.51, "pe": 19.18, "mcap": 4052.01, "divyld": 0.22, "npqtr": 66.26, "qpv": 7.06, "salesqtr": 240.05, "qsv": 17.82, "roce": 13.13, "ret3m": 38.70},
    {"name": "Jayaswal Neco", "symbol": "JAYNECOIND", "cmp": 98.95, "pe": 25.17, "mcap": 9599.98, "divyld": 0.00, "npqtr": 74.09, "qpv": 6.08, "salesqtr": 1727.23, "qsv": 4.25, "roce": 12.59, "ret3m": 35.72},
    {"name": "Lux Industries", "symbol": "LUXIND", "cmp": 1462.55, "pe": 38.96, "mcap": 4416.06, "divyld": 0.14, "npqtr": 13.32, "qpv": -46.66, "salesqtr": 672.53, "qsv": 21.59, "roce": 12.54, "ret3m": 66.07},
    {"name": "Azad Engineering", "symbol": "AZAD", "cmp": 1862.60, "pe": 97.86, "mcap": 12042.35, "divyld": 0.00, "npqtr": 34.04, "qpv": 40.14, "salesqtr": 155.80, "qsv": 31.38, "roce": 12.23, "ret3m": 32.64},
    {"name": "SMS Pharma.", "symbol": "SMSPHARMA", "cmp": 408.10, "pe": 43.87, "mcap": 3830.20, "divyld": 0.10, "npqtr": 23.34, "qpv": 35.93, "salesqtr": 210.45, "qsv": 21.40, "roce": 12.19, "ret3m": 36.74},
    {"name": "Bharat Forge", "symbol": "BHARATFORG", "cmp": 1895.80, "pe": 77.67, "mcap": 90694.36, "divyld": 0.45, "npqtr": 272.80, "qpv": 40.77, "salesqtr": 4342.93, "qsv": 24.96, "roce": 12.18, "ret3m": 37.38},
    {"name": "Deep Industries", "symbol": "DEEPINDS", "cmp": 474.15, "pe": 13.07, "mcap": 3028.84, "divyld": 0.64, "npqtr": 71.35, "qpv": 56.07, "salesqtr": 221.50, "qsv": 43.06, "roce": 12.06, "ret3m": 34.00},
    {"name": "Syrma SGS Tech.", "symbol": "SYRMA", "cmp": 985.95, "pe": 66.84, "mcap": 19018.04, "divyld": 0.15, "npqtr": 110.32, "qpv": 108.80, "salesqtr": 1264.18, "qsv": 45.36, "roce": 11.67, "ret3m": 54.02},
    {"name": "SG Mart", "symbol": "SGMART", "cmp": 548.60, "pe": 67.24, "mcap": 6907.18, "divyld": 0.00, "npqtr": 10.74, "qpv": -61.70, "salesqtr": 1644.43, "qsv": 23.21, "roce": 11.33, "ret3m": 71.79},
    {"name": "RPSG Ventures", "symbol": "RPSGVENT", "cmp": 937.60, "pe": None, "mcap": 3102.34, "divyld": 0.00, "npqtr": -136.30, "qpv": -203.72, "salesqtr": 2756.40, "qsv": 15.57, "roce": 11.33, "ret3m": 41.54},
    {"name": "Vardhman Textile", "symbol": "VTL", "cmp": 560.35, "pe": 20.33, "mcap": 16221.71, "divyld": 0.89, "npqtr": 168.50, "qpv": -21.02, "salesqtr": 2505.31, "qsv": 1.62, "roce": 10.83, "ret3m": 39.06},
    {"name": "Gokaldas Exports", "symbol": "GOKEX", "cmp": 768.50, "pe": 48.11, "mcap": 5630.22, "divyld": 0.00, "npqtr": 14.61, "qpv": -70.98, "salesqtr": 978.65, "qsv": -0.92, "roce": 10.62, "ret3m": 36.27},
    {"name": "MTAR Technologie", "symbol": "MTARTECH", "cmp": 5071.10, "pe": 229.68, "mcap": 15590.45, "divyld": 0.00, "npqtr": 35.17, "qpv": 131.84, "salesqtr": 277.90, "qsv": 59.30, "roce": 10.51, "ret3m": 108.06},
    {"name": "Adani Energy Sol", "symbol": "ADANIENSOL", "cmp": 1265.30, "pe": 67.57, "mcap": 151757.30, "divyld": 0.00, "npqtr": 574.06, "qpv": -1.69, "salesqtr": 6729.65, "qsv": 15.43, "roce": 10.23, "ret3m": 40.70},
    {"name": "S C I", "symbol": "SCI", "cmp": 300.60, "pe": 12.34, "mcap": 13986.10, "divyld": 2.19, "npqtr": 404.97, "qpv": 436.24, "salesqtr": 1611.67, "qsv": 22.50, "roce": 9.81, "ret3m": 48.34},
    {"name": "Power Fin.Corpn.", "symbol": "PFC", "cmp": 471.10, "pe": 6.16, "mcap": 155467.79, "divyld": 3.35, "npqtr": 8211.90, "qpv": 8.14, "salesqtr": 29094.81, "qsv": 8.57, "roce": 9.73, "ret3m": 31.72},
    {"name": "Dalmia Bharat", "symbol": "DALMIASUG", "cmp": 382.95, "pe": 9.11, "mcap": 3084.17, "divyld": 1.57, "npqtr": 69.77, "qpv": 17.64, "salesqtr": 697.75, "qsv": -16.70, "roce": 9.48, "ret3m": 44.81},
    {"name": "SG Finserve", "symbol": "SGFIN", "cmp": 541.40, "pe": 27.97, "mcap": 3571.15, "divyld": 0.00, "npqtr": 42.27, "qpv": 77.68, "salesqtr": 105.41, "qsv": 94.88, "roce": 9.32, "ret3m": 49.52},
    {"name": "Dynamatic Tech.", "symbol": "DYNAMATECH", "cmp": 10747.00, "pe": 155.69, "mcap": 7289.52, "divyld": 0.05, "npqtr": 5.77, "qpv": 316.15, "salesqtr": 424.87, "qsv": 34.70, "roce": 8.96, "ret3m": 34.17},
    {"name": "Sigma Advanced", "symbol": "SIGMAADV", "cmp": 216.19, "pe": 26.63, "mcap": 3814.76, "divyld": 0.00, "npqtr": -1.03, "qpv": 3.15, "salesqtr": 145.70, "qsv": 667.25, "roce": 8.74, "ret3m": 30.48},
    {"name": "Adani Green", "symbol": "ADANIGREEN", "cmp": 1150.00, "pe": 114.70, "mcap": 189113.55, "divyld": 0.00, "npqtr": 5.00, "qpv": -106.78, "salesqtr": 2618.00, "qsv": 11.88, "roce": 8.70, "ret3m": 30.88},
    {"name": "SEAMEC Ltd", "symbol": "SEAMECLTD", "cmp": 1519.10, "pe": 20.26, "mcap": 3867.15, "divyld": 0.00, "npqtr": 99.76, "qpv": 3100.60, "salesqtr": 317.05, "qsv": 112.30, "roce": 8.60, "ret3m": 39.14},
    {"name": "ACME Solar Hold.", "symbol": "ACMESOLAR", "cmp": 296.25, "pe": 35.79, "mcap": 17957.92, "divyld": 0.07, "npqtr": 113.70, "qpv": -3.66, "salesqtr": 496.79, "qsv": 42.34, "roce": 8.42, "ret3m": 45.09},
    # Page 5
    {"name": "Rossell Techsys", "symbol": "ROSSELLIND", "cmp": 939.00, "pe": 160.66, "mcap": 3529.67, "divyld": 0.02, "npqtr": 5.41, "qpv": 18.27, "salesqtr": 129.93, "qsv": 71.55, "roce": 8.18, "ret3m": 46.02},
    {"name": "Prime Focus", "symbol": "PFOCUS", "cmp": 328.20, "pe": 96.82, "mcap": 25468.01, "divyld": 0.00, "npqtr": 69.20, "qpv": 237.06, "salesqtr": 1207.24, "qsv": 32.74, "roce": 7.95, "ret3m": 49.77},
    {"name": "Shilpa Medicare", "symbol": "SHILPAMED", "cmp": 405.25, "pe": 44.86, "mcap": 7936.57, "divyld": 0.12, "npqtr": 44.58, "qpv": 69.92, "salesqtr": 409.73, "qsv": 28.32, "roce": 7.82, "ret3m": 48.91},
    {"name": "HFCL", "symbol": "HFCL", "cmp": 97.84, "pe": 288.92, "mcap": 14969.00, "divyld": 0.10, "npqtr": 102.37, "qpv": 32.55, "salesqtr": 1210.79, "qsv": 19.65, "roce": 7.55, "ret3m": 57.76},
    {"name": "Karnataka Bank", "symbol": "KTKBANK", "cmp": 250.32, "pe": 8.20, "mcap": 9469.34, "divyld": 2.00, "npqtr": 290.79, "qpv": 2.54, "salesqtr": 2220.05, "qsv": -1.02, "roce": 6.33, "ret3m": 38.45},
    {"name": "Aarti Industries", "symbol": "AARTIIND", "cmp": 451.20, "pe": 44.08, "mcap": 16352.92, "divyld": 0.22, "npqtr": 133.00, "qpv": 221.74, "salesqtr": 2318.00, "qsv": 25.77, "roce": 6.32, "ret3m": 32.71},
    {"name": "GE Power", "symbol": "GEPIL", "cmp": 492.00, "pe": 19.60, "mcap": 3291.39, "divyld": 0.00, "npqtr": 72.32, "qpv": 431.62, "salesqtr": 385.62, "qsv": 21.69, "roce": 6.09, "ret3m": 75.97},
    {"name": "Mahindra Logis.", "symbol": "MAHLOG", "cmp": 425.95, "pe": None, "mcap": None, "divyld": 0.59, "npqtr": 6.01, "qpv": 146.23, "salesqtr": 1898.03, "qsv": 19.06, "roce": 5.64, "ret3m": 50.46},
    {"name": "Jindal Poly Film", "symbol": "JINDALPOLY", "cmp": 728.10, "pe": None, "mcap": None, "divyld": 0.81, "npqtr": -96.92, "qpv": -453.42, "salesqtr": 371.66, "qsv": -68.66, "roce": 5.36, "ret3m": 98.28},
    {"name": "B H E L", "symbol": "BHEL", "cmp": 332.61, "pe": 142.25, "mcap": 115827.58, "divyld": 0.15, "npqtr": 390.40, "qpv": 189.83, "salesqtr": 8473.10, "qsv": 16.44, "roce": 4.87, "ret3m": 31.81},
    {"name": "Sterlite Tech.", "symbol": "STLTECH", "cmp": 278.47, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": -17.00, "qpv": 53.33, "salesqtr": 1257.00, "qsv": 25.95, "roce": 2.86, "ret3m": 200.72},
    {"name": "Aequs", "symbol": "AEQUS", "cmp": 190.36, "pe": None, "mcap": 12720.38, "divyld": 0.00, "npqtr": -42.68, "qpv": 17.87, "salesqtr": 326.17, "qsv": 50.77, "roce": 1.11, "ret3m": 40.58},
    {"name": "Dhenu Buildcon", "symbol": "DHENU", "cmp": 9.75, "pe": None, "mcap": 4382.92, "divyld": 0.00, "npqtr": 0.81, "qpv": 4150.00, "salesqtr": 0.84, "qsv": -0.08, "roce": None, "ret3m": 39.89},
    {"name": "Gujarat Alkalies", "symbol": "GUJALKALI", "cmp": 719.70, "pe": None, "mcap": 5271.49, "divyld": 2.20, "npqtr": -19.95, "qpv": -77.65, "salesqtr": 1044.46, "qsv": 1.46, "roce": -0.34, "ret3m": 57.04},
    {"name": "E2E Networks", "symbol": "E2E", "cmp": 2844.40, "pe": None, "mcap": 5847.08, "divyld": 0.00, "npqtr": 6.44, "qpv": -52.68, "salesqtr": 95.64, "qsv": 185.66, "roce": -0.51, "ret3m": 37.79},
    {"name": "Ather Energy", "symbol": "ATHERENRGY", "cmp": 896.10, "pe": None, "mcap": 34295.19, "divyld": 0.00, "npqtr": -84.60, "qpv": 59.76, "salesqtr": 953.60, "qsv": 50.20, "roce": -65.71, "ret3m": 46.12},
    {"name": "Suven Life Scie.", "symbol": "SUVENLIFE", "cmp": 210.50, "pe": None, "mcap": 5534.99, "divyld": 0.00, "npqtr": -101.92, "qpv": -160.53, "salesqtr": 2.81, "qsv": 74.53, "roce": -86.96, "ret3m": 55.86},
    {"name": "Indiabulls", "symbol": "IBULHSGFIN", "cmp": 17.47, "pe": 141.57, "mcap": 4063.09, "divyld": 0.00, "npqtr": 78.37, "qpv": 2250.95, "salesqtr": 96.96, "qsv": -8.90, "roce": None, "ret3m": 45.46},
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
    return {idx: val_to_rank[v] for idx, v in valid}

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

# Save top 20 as JSON
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

# Save full universe
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
