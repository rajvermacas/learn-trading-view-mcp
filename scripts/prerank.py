#!/usr/bin/env python3
"""Compute PreRankScore for the screener universe."""
import json

stocks = [
    # Page 1
    {"name": "Shilchar Tech.", "symbol": "SHILCTECH", "cmp": 4983.30, "pe": 30.79, "mcap": 5700.99, "divyld": 0.25, "npqtr": 42.34, "profitvar": 21.77, "salesqtr": 170.26, "salesvar": 10.75, "roce": 71.30, "ret3m": 66.97},
    {"name": "Siemens Ener.Ind", "symbol": "ENRIN", "cmp": 3138.40, "pe": 91.62, "mcap": 111764.86, "divyld": 0.13, "npqtr": 312.90, "profitvar": 51.67, "salesqtr": 1910.90, "salesvar": 25.97, "roce": 67.75, "ret3m": 39.43},
    {"name": "Ingersoll-Rand", "symbol": "INGERSOLL", "cmp": 4148.60, "pe": 47.30, "mcap": 13096.30, "divyld": 1.93, "npqtr": 71.89, "profitvar": 15.75, "salesqtr": 455.48, "salesvar": 19.39, "roce": 60.02, "ret3m": 32.78},
    {"name": "GE Vernova T&D", "symbol": "GVT&D", "cmp": 4232.30, "pe": 96.97, "mcap": 108368.04, "divyld": 0.12, "npqtr": 290.80, "profitvar": 138.53, "salesqtr": 1700.64, "salesvar": 58.40, "roce": 54.74, "ret3m": 65.47},
    {"name": "Saatvik Green", "symbol": "SAATVIK", "cmp": 464.05, "pe": 15.05, "mcap": 5898.31, "divyld": 0.00, "npqtr": 98.72, "profitvar": 144.05, "salesqtr": 1257.02, "salesvar": 142.58, "roce": 52.33, "ret3m": 31.98},
    {"name": "Atlanta Electric", "symbol": "ATLANTAELE", "cmp": 1385.90, "pe": 68.24, "mcap": 10657.10, "divyld": 0.00, "npqtr": 49.42, "profitvar": 125.33, "salesqtr": 471.82, "salesvar": 79.71, "roce": 50.20, "ret3m": 84.39},
    {"name": "BSE", "symbol": "BSE", "cmp": 3470.70, "pe": 64.80, "mcap": 141361.29, "divyld": 0.17, "npqtr": 596.59, "profitvar": 175.79, "salesqtr": 1244.10, "salesvar": 61.97, "roce": 46.57, "ret3m": 32.03},
    {"name": "Premier Energies", "symbol": "PREMIERENE", "cmp": 1010.75, "pe": 34.41, "mcap": 45786.41, "divyld": 0.10, "npqtr": 391.62, "profitvar": 53.48, "salesqtr": 1936.46, "salesvar": 13.02, "roce": 41.12, "ret3m": 42.12},
    {"name": "Schneider Elect.", "symbol": "SCHNEIDER", "cmp": 1087.85, "pe": 99.40, "mcap": 26010.49, "divyld": 0.00, "npqtr": 97.03, "profitvar": 16.65, "salesqtr": 1029.17, "salesvar": 20.06, "roce": 40.90, "ret3m": 87.82},
    {"name": "Lloyds Metals", "symbol": "LLOYDSME", "cmp": 1629.10, "pe": 37.22, "mcap": 91683.32, "divyld": 0.06, "npqtr": 1089.56, "profitvar": 169.05, "salesqtr": 5058.08, "salesvar": 201.94, "roce": 38.28, "ret3m": 42.63},
    {"name": "Inox India", "symbol": "INOXINDIA", "cmp": 1477.30, "pe": 53.02, "mcap": 13408.49, "divyld": 0.14, "npqtr": 60.70, "profitvar": 26.34, "salesqtr": 428.56, "salesvar": 28.45, "roce": 37.98, "ret3m": 33.64},
    {"name": "CG Power & Ind", "symbol": "CGPOWER", "cmp": 795.70, "pe": 112.62, "mcap": 125317.72, "divyld": 0.16, "npqtr": 283.91, "profitvar": 18.42, "salesqtr": 3175.35, "salesvar": 26.22, "roce": 37.48, "ret3m": 38.31},
    {"name": "Aditya AMC", "symbol": "ABSLAMC", "cmp": 1066.70, "pe": 30.26, "mcap": 30806.96, "divyld": 2.25, "npqtr": 269.52, "profitvar": 21.01, "salesqtr": 478.08, "salesvar": 7.41, "roce": 35.51, "ret3m": 36.42},
    {"name": "Waaree Energies", "symbol": "WAAREEENER", "cmp": 3489.10, "pe": 28.83, "mcap": 100364.43, "divyld": 0.06, "npqtr": 1106.79, "profitvar": 158.06, "salesqtr": 7565.05, "salesvar": 118.81, "roce": 34.94, "ret3m": 44.24},
    {"name": "Insolation Ener", "symbol": "INSOLATION", "cmp": 142.86, "pe": 17.77, "mcap": 3148.56, "divyld": 0.07, "npqtr": 50.72, "profitvar": 173.57, "salesqtr": 575.34, "salesvar": 77.05, "roce": 34.73, "ret3m": 40.40},
    {"name": "Gokul Agro", "symbol": "GOKULAGRO", "cmp": 206.05, "pe": 20.32, "mcap": 6080.26, "divyld": 0.00, "npqtr": 77.70, "profitvar": 7.17, "salesqtr": 6314.25, "salesvar": 26.58, "roce": 34.20, "ret3m": 33.18},
    {"name": "Steelcast", "symbol": "STEELCAST", "cmp": 298.32, "pe": 33.38, "mcap": 3019.00, "divyld": 0.48, "npqtr": 20.59, "profitvar": 7.18, "salesqtr": 97.40, "salesvar": -4.33, "roce": 32.94, "ret3m": 63.59},
    {"name": "Natco Pharma", "symbol": "NATCOPHARM", "cmp": 1100.05, "pe": 12.65, "mcap": 19702.98, "divyld": 0.55, "npqtr": 151.30, "profitvar": 13.91, "salesqtr": 647.30, "salesvar": 36.33, "roce": 32.78, "ret3m": 31.00},
    {"name": "Apar Inds.", "symbol": "APARINDS", "cmp": 11977.00, "pe": 48.52, "mcap": 48109.59, "divyld": 0.43, "npqtr": 208.93, "profitvar": 29.80, "salesqtr": 5479.73, "salesvar": 16.18, "roce": 32.70, "ret3m": 71.94},
    {"name": "Bajaj Consumer", "symbol": "BAJAJCON", "cmp": 474.30, "pe": 32.58, "mcap": 6195.23, "divyld": 0.00, "npqtr": 63.60, "profitvar": 105.29, "salesqtr": 326.66, "salesvar": 30.41, "roce": 30.60, "ret3m": 91.68},
    {"name": "TD Power Systems", "symbol": "TDPOWERSYS", "cmp": 1030.70, "pe": 73.32, "mcap": 16101.06, "divyld": 0.12, "npqtr": 56.32, "profitvar": 25.35, "salesqtr": 442.68, "salesvar": 26.36, "roce": 30.35, "ret3m": 62.29},
    {"name": "A B B", "symbol": "ABB", "cmp": 7158.00, "pe": 90.85, "mcap": 151684.01, "divyld": 0.55, "npqtr": 432.85, "profitvar": -18.35, "salesqtr": 3557.01, "salesvar": 5.71, "roce": 29.93, "ret3m": 52.06},
    {"name": "Volt.Transform.", "symbol": "VOLTAMP", "cmp": 10307.00, "pe": 29.43, "mcap": 10427.72, "divyld": 0.97, "npqtr": 99.08, "profitvar": 34.99, "salesqtr": 630.32, "salesvar": 30.36, "roce": 29.11, "ret3m": 52.05},
    {"name": "Emmvee Photovol.", "symbol": "EMMVEE", "cmp": 261.19, "pe": 33.90, "mcap": 18083.36, "divyld": 0.00, "npqtr": 263.64, "profitvar": 165.77, "salesqtr": 1152.25, "salesvar": 118.11, "roce": 28.01, "ret3m": 33.71},
    {"name": "T R I L", "symbol": "TRIL", "cmp": 321.35, "pe": 36.16, "mcap": 9645.83, "divyld": 0.06, "npqtr": 75.97, "profitvar": 34.89, "salesqtr": 736.76, "salesvar": 31.71, "roce": 27.97, "ret3m": 32.03},
    # Page 2
    {"name": "Krishana Phosch.", "symbol": "KRISHANA", "cmp": 638.75, "pe": 21.47, "mcap": 3867.80, "divyld": 0.08, "npqtr": 83.08, "profitvar": 152.83, "salesqtr": 755.49, "salesvar": 59.76, "roce": 27.24, "ret3m": 35.77},
    {"name": "Prec. Wires (I)", "symbol": "PRECWIRE", "cmp": 365.00, "pe": 51.33, "mcap": 6672.49, "divyld": 0.32, "npqtr": 37.70, "profitvar": 98.94, "salesqtr": 1347.61, "salesvar": 37.19, "roce": 26.78, "ret3m": 66.63},
    {"name": "Quality Power El", "symbol": "QPOWER", "cmp": 1277.25, "pe": 92.43, "mcap": 9891.55, "divyld": 0.08, "npqtr": 62.76, "profitvar": 169.18, "salesqtr": 283.99, "salesvar": 291.22, "roce": 26.60, "ret3m": 93.64},
    {"name": "Rubicon Research", "symbol": "RUBICON", "cmp": 927.55, "pe": 90.73, "mcap": 15281.42, "divyld": 0.00, "npqtr": 72.80, "profitvar": 91.23, "salesqtr": 475.53, "salesvar": 51.73, "roce": 26.05, "ret3m": 40.67},
    {"name": "Shriram Pistons", "symbol": "SHRIPISTON", "cmp": 3627.60, "pe": 28.47, "mcap": 15979.51, "divyld": 0.28, "npqtr": 125.70, "profitvar": 17.91, "salesqtr": 1023.20, "salesvar": 20.67, "roce": 25.70, "ret3m": 31.97},
    {"name": "Engineers India", "symbol": "ENGINERSIN", "cmp": 242.06, "pe": 17.53, "mcap": 13604.80, "divyld": 1.65, "npqtr": 347.17, "profitvar": 219.30, "salesqtr": 1210.24, "salesvar": 58.29, "roce": 25.01, "ret3m": 35.57},
    {"name": "Goldiam Intl.", "symbol": "GOLDIAM", "cmp": 407.25, "pe": 29.37, "mcap": 4598.58, "divyld": 0.74, "npqtr": 68.39, "profitvar": 37.52, "salesqtr": 319.71, "salesvar": 14.33, "roce": 24.59, "ret3m": 39.23},
    {"name": "KSB", "symbol": "KSB", "cmp": 981.95, "pe": 59.16, "mcap": 17089.78, "divyld": 0.45, "npqtr": 81.00, "profitvar": 33.43, "salesqtr": 784.00, "salesvar": 7.93, "roce": 24.52, "ret3m": 43.44},
    {"name": "Avanti Feeds", "symbol": "AVANTIFEED", "cmp": 1503.40, "pe": 32.38, "mcap": 20483.17, "divyld": 0.60, "npqtr": 163.47, "profitvar": 10.40, "salesqtr": 1383.52, "salesvar": 1.31, "roce": 23.99, "ret3m": 101.35},
    {"name": "Supreme Petroch.", "symbol": "SUPPETRO", "cmp": 769.90, "pe": 53.32, "mcap": 14477.30, "divyld": 1.30, "npqtr": 30.15, "profitvar": -50.25, "salesqtr": 1264.69, "salesvar": -10.01, "roce": 22.76, "ret3m": 45.73},
    {"name": "Adani Power", "symbol": "ADANIPOWER", "cmp": 200.83, "pe": 33.81, "mcap": 387294.52, "divyld": 0.00, "npqtr": 2488.09, "profitvar": -18.89, "salesqtr": 12451.44, "salesvar": -8.92, "roce": 22.54, "ret3m": 45.92},
    {"name": "Aeroflex", "symbol": "AEROFLEX", "cmp": 300.89, "pe": 81.06, "mcap": 3981.70, "divyld": 0.10, "npqtr": 16.49, "profitvar": 8.42, "salesqtr": 120.89, "salesvar": 21.13, "roce": 22.34, "ret3m": 85.95},
    {"name": "AGI Infra", "symbol": "AGIIL", "cmp": 372.05, "pe": 55.42, "mcap": 4650.53, "divyld": 0.03, "npqtr": 26.11, "profitvar": 36.92, "salesqtr": 87.50, "salesvar": -4.28, "roce": 22.03, "ret3m": 35.59},
    {"name": "Hind Rectifiers", "symbol": "HIRECT", "cmp": 884.80, "pe": 57.91, "mcap": 3040.85, "divyld": 0.11, "npqtr": 13.73, "profitvar": 47.85, "salesqtr": 243.27, "salesvar": 44.00, "roce": 21.60, "ret3m": 41.84},
    {"name": "KSH Internationa", "symbol": "KSHINTL", "cmp": 563.25, "pe": 57.13, "mcap": 3816.34, "divyld": 0.00, "npqtr": 23.33, "profitvar": -4.62, "salesqtr": 817.77, "salesvar": 58.52, "roce": 21.45, "ret3m": 61.14},
    {"name": "Indian Metals", "symbol": "IMFA", "cmp": 1532.00, "pe": 22.44, "mcap": 8265.77, "divyld": 1.31, "npqtr": 131.46, "profitvar": 40.69, "salesqtr": 702.83, "salesvar": 9.27, "roce": 21.29, "ret3m": 40.18},
    {"name": "Welspun Corp", "symbol": "WELCORP", "cmp": 1076.65, "pe": 18.30, "mcap": 28401.02, "divyld": 0.46, "npqtr": 456.36, "profitvar": -32.91, "salesqtr": 4532.48, "salesvar": 25.43, "roce": 21.24, "ret3m": 43.49},
    {"name": "Allied Blenders", "symbol": "ABDL", "cmp": 573.40, "pe": 59.80, "mcap": 16038.58, "divyld": 0.63, "npqtr": 63.74, "profitvar": 19.51, "salesqtr": 1002.98, "salesvar": 2.98, "roce": 21.08, "ret3m": 31.44},
    {"name": "Data Pattern", "symbol": "DATAPATTNS", "cmp": 3467.60, "pe": 77.84, "mcap": 19413.00, "divyld": 0.23, "npqtr": 58.30, "profitvar": 35.76, "salesqtr": 173.13, "salesvar": 47.92, "roce": 21.00, "ret3m": 56.57},
    {"name": "KRN Heat Exchan", "symbol": "KRN", "cmp": 1245.80, "pe": 113.92, "mcap": 7743.47, "divyld": 0.00, "npqtr": 22.66, "profitvar": 65.04, "salesqtr": 153.23, "salesvar": 37.46, "roce": 20.75, "ret3m": 100.71},
    {"name": "Garware Hi Tech", "symbol": "GARFIBRES", "cmp": 3977.50, "pe": 30.02, "mcap": 9240.68, "divyld": 0.30, "npqtr": 55.77, "profitvar": -8.29, "salesqtr": 458.74, "salesvar": -1.64, "roce": 20.57, "ret3m": 47.07},
    {"name": "Park Medi World", "symbol": "PARKHOSPS", "cmp": 221.79, "pe": 45.25, "mcap": 9579.79, "divyld": 0.00, "npqtr": 52.85, "profitvar": 11.38, "salesqtr": 409.97, "salesvar": 17.76, "roce": 20.36, "ret3m": 47.83},
    {"name": "Ram Ratna Wires", "symbol": "RRWL", "cmp": 372.40, "pe": 39.20, "mcap": 3476.32, "divyld": 0.34, "npqtr": 31.64, "profitvar": 106.33, "salesqtr": 1277.94, "salesvar": 43.80, "roce": 20.17, "ret3m": 32.22},
    {"name": "Acutaas Chemical", "symbol": "ACUTAAS", "cmp": 2410.70, "pe": 68.78, "mcap": 19736.67, "divyld": 0.06, "npqtr": 106.22, "profitvar": 140.18, "salesqtr": 393.18, "salesvar": 42.98, "roce": 19.92, "ret3m": 50.43},
    {"name": "GNG Electronics", "symbol": "EBGNG", "cmp": 412.10, "pe": 44.91, "mcap": 4698.41, "divyld": 0.00, "npqtr": 38.69, "profitvar": 102.78, "salesqtr": 487.22, "salesvar": 40.26, "roce": 19.84, "ret3m": 61.13},
    # Page 3
    {"name": "Aditya Infotech", "symbol": "CPPLUS", "cmp": 2273.80, "pe": 105.54, "mcap": 26784.93, "divyld": 0.00, "npqtr": 95.98, "profitvar": 138.82, "salesqtr": 1139.11, "salesvar": 37.32, "roce": 19.49, "ret3m": 65.20},
    {"name": "Hitachi Energy", "symbol": "POWERINDIA", "cmp": 29645.00, "pe": 149.81, "mcap": 132134.78, "divyld": 0.02, "npqtr": 261.42, "profitvar": 119.97, "salesqtr": 2082.21, "salesvar": 28.51, "roce": 19.44, "ret3m": 77.63},
    {"name": "Gallantt Ispat", "symbol": "GALLANTT", "cmp": 869.05, "pe": 43.74, "mcap": 20968.52, "divyld": 0.14, "npqtr": 100.41, "profitvar": -11.67, "salesqtr": 1073.58, "salesvar": -4.00, "roce": 19.20, "ret3m": 59.80},
    {"name": "Finolex Cables", "symbol": "FINCABLES", "cmp": 946.55, "pe": 21.26, "mcap": 14476.47, "divyld": 0.85, "npqtr": 164.03, "profitvar": 11.40, "salesqtr": 1598.62, "salesvar": 35.23, "roce": 17.67, "ret3m": 32.67},
    {"name": "Nava", "symbol": "NAVA", "cmp": 702.10, "pe": 22.20, "mcap": 19869.52, "divyld": 1.14, "npqtr": 325.71, "profitvar": -11.98, "salesqtr": 991.12, "salesvar": 17.64, "roce": 17.17, "ret3m": 32.06},
    {"name": "Cupid", "symbol": "CUPID", "cmp": 105.42, "pe": 169.64, "mcap": 14175.41, "divyld": 0.00, "npqtr": 32.87, "profitvar": 196.66, "salesqtr": 104.40, "salesvar": 105.67, "roce": 17.10, "ret3m": 39.96},
    {"name": "Pitti Engg.", "symbol": "PITTIENG", "cmp": 950.50, "pe": 28.11, "mcap": 3578.97, "divyld": 0.16, "npqtr": 28.22, "profitvar": -1.88, "salesqtr": 477.42, "salesvar": 15.05, "roce": 17.05, "ret3m": 38.75},
    {"name": "Techno Elec.Engg", "symbol": "TECHNOE", "cmp": 1264.25, "pe": 31.36, "mcap": 14703.17, "divyld": 0.71, "npqtr": 119.25, "profitvar": 24.23, "salesqtr": 872.20, "salesvar": 37.12, "roce": 16.54, "ret3m": 39.28},
    {"name": "Sharda Cropchem", "symbol": "SHARDACROP", "cmp": 1102.75, "pe": 17.58, "mcap": 9949.07, "divyld": 0.82, "npqtr": 145.11, "profitvar": 365.87, "salesqtr": 1288.76, "salesvar": 38.68, "roce": 16.50, "ret3m": 37.34},
    {"name": "Thermax", "symbol": "THERMAX", "cmp": 4185.20, "pe": 77.83, "mcap": 49869.29, "divyld": 0.33, "npqtr": 205.01, "profitvar": 40.63, "salesqtr": 2634.68, "salesvar": 4.19, "roce": 16.22, "ret3m": 42.87},
    {"name": "Man Industries", "symbol": "MANINDS", "cmp": 535.75, "pe": 21.40, "mcap": 4018.64, "divyld": 0.00, "npqtr": 55.04, "profitvar": 61.31, "salesqtr": 830.38, "salesvar": 13.45, "roce": 15.98, "ret3m": 65.53},
    {"name": "ISGEC Heavy", "symbol": "ISGEC", "cmp": 1046.45, "pe": 23.50, "mcap": 7694.50, "divyld": 0.48, "npqtr": 84.44, "profitvar": 102.88, "salesqtr": 1738.56, "salesvar": 16.26, "roce": 14.83, "ret3m": 40.35},
    {"name": "Amber Enterp.", "symbol": "AMBER", "cmp": 7980.50, "pe": 120.83, "mcap": 28084.71, "divyld": 0.00, "npqtr": -9.34, "profitvar": 26.43, "salesqtr": 2942.82, "salesvar": 37.94, "roce": 14.49, "ret3m": 37.98},
    {"name": "Belrise Industri", "symbol": "BELRISE", "cmp": 222.18, "pe": 41.09, "mcap": 19771.34, "divyld": 0.25, "npqtr": 121.97, "profitvar": 25.79, "salesqtr": 2340.52, "salesvar": 8.02, "roce": 14.30, "ret3m": 34.40},
    {"name": "Rashi Peripheral", "symbol": "RASHI", "cmp": 474.35, "pe": 12.88, "mcap": 3125.95, "divyld": 0.42, "npqtr": 74.60, "profitvar": 131.00, "salesqtr": 4030.41, "salesvar": 42.60, "roce": 14.19, "ret3m": 34.68},
    {"name": "TruAlt Bioenergy", "symbol": "TRUALT", "cmp": 458.00, "pe": 26.57, "mcap": 3927.47, "divyld": 0.00, "npqtr": 69.19, "profitvar": -7.79, "salesqtr": 713.24, "salesvar": 71.82, "roce": 14.18, "ret3m": 35.82},
    {"name": "Apollo Micro Sys", "symbol": "APOLLOMICRO", "cmp": 289.29, "pe": 115.75, "mcap": 10336.11, "divyld": 0.09, "npqtr": 22.88, "profitvar": 40.64, "salesqtr": 252.22, "salesvar": 69.97, "roce": 13.98, "ret3m": 30.05},
    {"name": "Sambhv Steel", "symbol": "SAMBHV", "cmp": 120.05, "pe": 34.03, "mcap": 3537.53, "divyld": 0.00, "npqtr": 24.13, "profitvar": 112.79, "salesqtr": 589.14, "salesvar": 59.64, "roce": 13.92, "ret3m": 42.95},
    {"name": "AXISCADES Tech.", "symbol": "AXISCADES", "cmp": 1855.40, "pe": 71.90, "mcap": 7888.68, "divyld": 0.00, "npqtr": 27.66, "profitvar": 110.65, "salesqtr": 343.18, "salesvar": 25.01, "roce": 13.76, "ret3m": 65.78},
    {"name": "Kirloskar Oil", "symbol": "KIRLOSENG", "cmp": 1639.90, "pe": 43.86, "mcap": 23837.46, "divyld": 0.40, "npqtr": 109.13, "profitvar": 79.61, "salesqtr": 1872.60, "salesvar": 28.82, "roce": 13.68, "ret3m": 48.68},
    {"name": "Sansera Enginee.", "symbol": "SANSERA", "cmp": 2275.50, "pe": 51.82, "mcap": 14183.66, "divyld": 0.14, "npqtr": 69.42, "profitvar": 44.51, "salesqtr": 907.67, "salesvar": 24.71, "roce": 13.38, "ret3m": 32.38},
    {"name": "Paisalo Digital", "symbol": "PAISALO", "cmp": 43.42, "pe": 18.69, "mcap": 3949.14, "divyld": 0.23, "npqtr": 66.26, "profitvar": 7.06, "salesqtr": 240.05, "salesvar": 17.82, "roce": 13.13, "ret3m": 35.31},
    {"name": "Jayaswal Neco", "symbol": "JAYNECOIND", "cmp": 95.34, "pe": 24.27, "mcap": 9257.50, "divyld": 0.00, "npqtr": 74.09, "profitvar": 6.08, "salesqtr": 1727.23, "salesvar": 4.25, "roce": 12.59, "ret3m": 30.76},
    {"name": "Lux Industries", "symbol": "LUXIND", "cmp": 1490.00, "pe": 39.53, "mcap": 4480.68, "divyld": 0.13, "npqtr": 13.32, "profitvar": -46.66, "salesqtr": 672.53, "salesvar": 21.59, "roce": 12.54, "ret3m": 69.18},
    {"name": "Azad Engineering", "symbol": "AZAD", "cmp": 1893.30, "pe": 99.36, "mcap": 12227.26, "divyld": 0.00, "npqtr": 34.04, "profitvar": 40.14, "salesqtr": 155.80, "salesvar": 31.38, "roce": 12.23, "ret3m": 34.83},
    # Page 4
    {"name": "SMS Pharma.", "symbol": "SMSPHARMA", "cmp": 417.70, "pe": 44.80, "mcap": 3911.85, "divyld": 0.10, "npqtr": 23.34, "profitvar": 35.93, "salesqtr": 210.45, "salesvar": 21.40, "roce": 12.19, "ret3m": 39.96},
    {"name": "Bharat Forge", "symbol": "BHARATFORG", "cmp": 1866.20, "pe": 76.41, "mcap": 89220.90, "divyld": 0.46, "npqtr": 272.80, "profitvar": 40.77, "salesqtr": 4342.93, "salesvar": 24.96, "roce": 12.18, "ret3m": 35.23},
    {"name": "Deep Industries", "symbol": "DEEPINDS", "cmp": 476.80, "pe": 13.17, "mcap": 3051.52, "divyld": 0.64, "npqtr": 71.35, "profitvar": 56.07, "salesqtr": 221.50, "salesvar": 43.06, "roce": 12.06, "ret3m": 34.75},
    {"name": "Centum Electron", "symbol": "CENTUM", "cmp": 2881.80, "pe": 76.36, "mcap": 4248.06, "divyld": 0.21, "npqtr": -61.75, "profitvar": 423.59, "salesqtr": 331.44, "salesvar": 21.39, "roce": 12.03, "ret3m": 31.93},
    {"name": "Syrma SGS Tech.", "symbol": "SYRMA", "cmp": 963.35, "pe": 65.29, "mcap": 18576.32, "divyld": 0.16, "npqtr": 110.32, "profitvar": 108.80, "salesqtr": 1264.18, "salesvar": 45.36, "roce": 11.67, "ret3m": 50.49},
    {"name": "SG Mart", "symbol": "SGMART", "cmp": 533.75, "pe": 65.47, "mcap": 6725.25, "divyld": 0.00, "npqtr": 10.74, "profitvar": -61.70, "salesqtr": 1644.43, "salesvar": 23.21, "roce": 11.33, "ret3m": 67.14},
    {"name": "RPSG Ventures", "symbol": "RPSGVENT", "cmp": 951.95, "pe": None, "mcap": None, "divyld": 0.00, "npqtr": -136.30, "profitvar": -203.72, "salesqtr": 2756.40, "salesvar": 15.57, "roce": 11.33, "ret3m": 43.70},
    {"name": "Vardhman Textile", "symbol": "VTL", "cmp": 549.90, "pe": 19.94, "mcap": 15907.61, "divyld": 0.91, "npqtr": 168.50, "profitvar": -21.02, "salesqtr": 2505.31, "salesvar": 1.62, "roce": 10.83, "ret3m": 36.47},
    {"name": "MTAR Technologie", "symbol": "MTARTECH", "cmp": 4942.00, "pe": 223.95, "mcap": 15201.39, "divyld": 0.00, "npqtr": 35.17, "profitvar": 131.84, "salesqtr": 277.90, "salesvar": 59.30, "roce": 10.51, "ret3m": 102.77},
    {"name": "Adani Energy Sol", "symbol": "ADANIENSOL", "cmp": 1259.40, "pe": 67.36, "mcap": 151289.54, "divyld": 0.00, "npqtr": 574.06, "profitvar": -1.69, "salesqtr": 6729.65, "salesvar": 15.43, "roce": 10.23, "ret3m": 40.04},
    {"name": "S C I", "symbol": "SCI", "cmp": 299.96, "pe": 12.33, "mcap": 13972.14, "divyld": 2.20, "npqtr": 404.97, "profitvar": 436.24, "salesqtr": 1611.67, "salesvar": 22.50, "roce": 9.81, "ret3m": 48.03},
    {"name": "Power Fin.Corpn.", "symbol": "PFC", "cmp": 472.85, "pe": 6.19, "mcap": 156045.31, "divyld": 3.34, "npqtr": 8211.90, "profitvar": 8.14, "salesqtr": 29094.81, "salesvar": 8.57, "roce": 9.73, "ret3m": 32.21},
    {"name": "Dalmia Bharat Sugar", "symbol": "DALMIASUG", "cmp": 390.55, "pe": 9.33, "mcap": 3161.08, "divyld": 1.54, "npqtr": 69.77, "profitvar": 17.64, "salesqtr": 697.75, "salesvar": -16.70, "roce": 9.48, "ret3m": 47.68},
    {"name": "SG Finserve", "symbol": "SGFIN", "cmp": 496.75, "pe": 25.64, "mcap": 3273.33, "divyld": 0.00, "npqtr": 42.27, "profitvar": 77.68, "salesqtr": 105.41, "salesvar": 94.88, "roce": 9.32, "ret3m": 37.19},
    {"name": "Adani Green", "symbol": "ADANIGREEN", "cmp": 1152.70, "pe": 115.16, "mcap": 189870.00, "divyld": 0.00, "npqtr": 5.00, "profitvar": -106.78, "salesqtr": 2618.00, "salesvar": 11.88, "roce": 8.70, "ret3m": 31.18},
    {"name": "SEAMEC Ltd", "symbol": "SEAMECLTD", "cmp": 1559.70, "pe": 20.78, "mcap": 3965.54, "divyld": 0.00, "npqtr": 99.76, "profitvar": 3100.60, "salesqtr": 317.05, "salesvar": 112.30, "roce": 8.60, "ret3m": 42.86},
    {"name": "ACME Solar Hold.", "symbol": "ACMESOLAR", "cmp": 299.05, "pe": 36.12, "mcap": 18121.59, "divyld": 0.07, "npqtr": 113.70, "profitvar": -3.66, "salesqtr": 496.79, "salesvar": 42.34, "roce": 8.42, "ret3m": 46.46},
    {"name": "Rossell Techsys", "symbol": "ROSSELLIND", "cmp": 932.90, "pe": 160.07, "mcap": 3516.70, "divyld": 0.02, "npqtr": 5.41, "profitvar": 18.27, "salesqtr": 129.93, "salesvar": 71.55, "roce": 8.18, "ret3m": 45.07},
    {"name": "Prime Focus", "symbol": "PFOCUS", "cmp": 327.55, "pe": 96.63, "mcap": 25417.57, "divyld": 0.00, "npqtr": 69.20, "profitvar": 237.06, "salesqtr": 1207.24, "salesvar": 32.74, "roce": 7.95, "ret3m": 49.47},
    {"name": "Shilpa Medicare", "symbol": "SHILPAMED", "cmp": 411.25, "pe": 45.47, "mcap": 8043.30, "divyld": 0.12, "npqtr": 44.58, "profitvar": 69.92, "salesqtr": 409.73, "salesvar": 28.32, "roce": 7.82, "ret3m": 51.11},
    {"name": "HFCL", "symbol": "HFCL", "cmp": 93.30, "pe": 275.63, "mcap": 14280.52, "divyld": 0.11, "npqtr": 102.37, "profitvar": 32.55, "salesqtr": 1210.79, "salesvar": 19.65, "roce": 7.55, "ret3m": 50.44},
    {"name": "Karnataka Bank", "symbol": "KTKBANK", "cmp": 245.67, "pe": 8.05, "mcap": 9290.79, "divyld": 2.04, "npqtr": 290.79, "profitvar": 2.54, "salesqtr": 2220.05, "salesvar": -1.02, "roce": 6.33, "ret3m": 35.88},
    {"name": "Aarti Industries", "symbol": "AARTIIND", "cmp": 445.65, "pe": 43.56, "mcap": 16159.02, "divyld": 0.22, "npqtr": 133.00, "profitvar": 221.74, "salesqtr": 2318.00, "salesvar": 25.77, "roce": 6.32, "ret3m": 31.07},
    {"name": "GE Power", "symbol": "GEPOWER", "cmp": 497.60, "pe": 19.92, "mcap": 3345.24, "divyld": 0.00, "npqtr": 72.32, "profitvar": 431.62, "salesqtr": 385.62, "salesvar": 21.69, "roce": 6.09, "ret3m": 77.97},
    {"name": "Mahindra Logis.", "symbol": "MAHLOG", "cmp": 432.35, "pe": None, "mcap": 4289.88, "divyld": 0.58, "npqtr": None, "profitvar": 6.01, "salesqtr": 146.23, "salesvar": 1898.03, "roce": 19.06, "ret3m": 5.64},
    # Page 5
    {"name": "Sindhu Trade", "symbol": "SINDHUTRAD", "cmp": 24.59, "pe": None, "mcap": 3791.60, "divyld": 0.00, "npqtr": 13.87, "profitvar": 285.68, "salesqtr": 119.15, "salesvar": -76.68, "roce": 5.45, "ret3m": 32.78},
    {"name": "Jindal Poly Film", "symbol": "JPFL", "cmp": 715.30, "pe": None, "mcap": 3132.04, "divyld": 0.82, "npqtr": -96.92, "profitvar": -453.42, "salesqtr": 371.66, "salesvar": -68.66, "roce": 5.36, "ret3m": 94.80},
    {"name": "Sterlite Tech.", "symbol": "STLTECH", "cmp": 271.63, "pe": 1104.93, "mcap": 13259.14, "divyld": 0.00, "npqtr": -17.00, "profitvar": 53.33, "salesqtr": 1257.00, "salesvar": 25.95, "roce": 2.86, "ret3m": 193.34},
    {"name": "Aequs", "symbol": "AEQUS", "cmp": 194.59, "pe": None, "mcap": 13050.48, "divyld": 0.00, "npqtr": -42.68, "profitvar": 17.87, "salesqtr": 326.17, "salesvar": 50.77, "roce": 1.11, "ret3m": 43.70},
    {"name": "Dhenu Buildcon", "symbol": "DHENU", "cmp": 9.94, "pe": 4468.33, "mcap": 5898.19, "divyld": 0.00, "npqtr": 0.81, "profitvar": 4150.00, "salesqtr": 0.84, "salesvar": -0.08, "roce": 42.61, "ret3m": None},
    {"name": "Gujarat Alkalies", "symbol": "GUJALKALI", "cmp": 734.80, "pe": 5396.37, "mcap": None, "divyld": 2.15, "npqtr": -19.95, "profitvar": -77.65, "salesqtr": 1044.46, "salesvar": 1.46, "roce": -0.34, "ret3m": 60.33},
    {"name": "E2E Networks", "symbol": "E2E", "cmp": 2709.00, "pe": 5568.75, "mcap": None, "divyld": 0.00, "npqtr": 6.44, "profitvar": -52.68, "salesqtr": 95.64, "salesvar": 185.66, "roce": -0.51, "ret3m": 31.23},
    {"name": "Ather Energy", "symbol": "ATHERENRGY", "cmp": 889.45, "pe": 34036.86, "mcap": None, "divyld": 0.00, "npqtr": -84.60, "profitvar": 59.76, "salesqtr": 953.60, "salesvar": 50.20, "roce": -65.71, "ret3m": 45.04},
    {"name": "Suven Life Scie.", "symbol": "SUVEN", "cmp": 210.18, "pe": 5542.88, "mcap": None, "divyld": 0.00, "npqtr": -101.92, "profitvar": -160.53, "salesqtr": 2.81, "salesvar": 74.53, "roce": -86.96, "ret3m": 55.62},
    {"name": "Indiabulls", "symbol": "IBULHSGFIN", "cmp": 16.99, "pe": 137.60, "mcap": 3949.13, "divyld": 0.00, "npqtr": 78.37, "profitvar": 2250.95, "salesqtr": 96.96, "salesvar": -8.90, "roce": 41.47, "ret3m": None},
    {"name": "Jindal Saw", "symbol": "JINDALSAW", "cmp": None, "pe": None, "mcap": None, "divyld": None, "npqtr": None, "profitvar": None, "salesqtr": None, "salesvar": None, "roce": None, "ret3m": None},
    {"name": "Sona BLW", "symbol": "SONACOMS", "cmp": None, "pe": None, "mcap": None, "divyld": None, "npqtr": None, "profitvar": None, "salesqtr": None, "salesvar": None, "roce": None, "ret3m": None},
    {"name": "Sky Gold", "symbol": "SKYGOLD", "cmp": None, "pe": None, "mcap": None, "divyld": None, "npqtr": None, "profitvar": None, "salesqtr": None, "salesvar": None, "roce": None, "ret3m": None},
]

# Filter out stocks with all None scoring columns (weren't actually scraped)
stocks = [s for s in stocks if s.get("profitvar") is not None or s.get("salesvar") is not None or s.get("roce") is not None or s.get("ret3m") is not None]

def percentile_rank(values, val, higher_is_better=True):
    """Compute percentile rank for val in list of valid values."""
    if val is None:
        return 0
    valid = sorted([v for v in values if v is not None])
    n = len(valid)
    if n == 0:
        return 0
    count_below = sum(1 for v in valid if v < val)
    count_equal = sum(1 for v in valid if v == val)
    # Percentile rank = (count_below + 0.5 * count_equal) / n * 100
    pct = (count_below + 0.5 * count_equal) / n * 100
    if not higher_is_better:
        pct = 100 - pct
    return pct

# Collect valid values for each scoring column
profit_vals = [s["profitvar"] for s in stocks if s["profitvar"] is not None]
sales_vals = [s["salesvar"] for s in stocks if s["salesvar"] is not None]
roce_vals_all = [s["roce"] for s in stocks if s["roce"] is not None]
ret3m_vals = [s["ret3m"] for s in stocks if s["ret3m"] is not None]

# Only use non-negative ROCE for ranking pool (negative ROCE => contribution 0)
roce_vals_positive = [v for v in roce_vals_all if v >= 0]

for s in stocks:
    flags = []

    # Profit Var percentile
    if s["profitvar"] is not None:
        s["profitvar_pct"] = percentile_rank(profit_vals, s["profitvar"])
    else:
        s["profitvar_pct"] = 0
        flags.append("profitvar_missing")

    # Sales Var percentile
    if s["salesvar"] is not None:
        s["salesvar_pct"] = percentile_rank(sales_vals, s["salesvar"])
    else:
        s["salesvar_pct"] = 0
        flags.append("salesvar_missing")

    # ROCE percentile - negative ROCE gets 0 contribution + extra penalty
    if s["roce"] is not None and s["roce"] < 0:
        s["roce_pct"] = 0
        flags.append("roce_negative")
    elif s["roce"] is not None:
        s["roce_pct"] = percentile_rank(roce_vals_positive, s["roce"])
    else:
        s["roce_pct"] = 0
        flags.append("roce_missing")

    # 3m return percentile
    if s["ret3m"] is not None:
        s["ret3m_pct"] = percentile_rank(ret3m_vals, s["ret3m"])
    else:
        s["ret3m_pct"] = 0
        flags.append("ret3m_missing")

    # Base PreRankScore
    base = (0.35 * s["profitvar_pct"] +
            0.35 * s["salesvar_pct"] +
            0.20 * s["roce_pct"] +
            0.10 * s["ret3m_pct"])

    # Soft penalties
    penalty = 0
    if s["profitvar"] is not None and s["profitvar"] <= 0:
        penalty -= 12
        flags.append("neg_profit")
    if s["salesvar"] is not None and s["salesvar"] <= 0:
        penalty -= 12
        flags.append("neg_sales")
    if s["roce"] is not None and s["roce"] < 15:
        penalty -= 8
        flags.append("low_roce")
    if s["roce"] is not None and s["roce"] < 0:
        penalty -= 12  # extra penalty for negative ROCE
        flags.append("neg_roce_extra")
    if s["ret3m"] is not None and s["ret3m"] <= 0:
        penalty -= 8
        flags.append("neg_ret3m")
    if s["ret3m"] is None:
        flags.append("ret3m_missing_penalty_skip")

    s["base_score"] = round(base, 2)
    s["penalty"] = penalty
    s["adjusted_score"] = round(base + penalty, 2)
    s["flags"] = flags

# Sort by adjusted score descending
stocks.sort(key=lambda x: x["adjusted_score"], reverse=True)

print(f"{'Rank':<5} {'Symbol':<15} {'Name':<25} {'ProfitVar%':<12} {'SalesVar%':<12} {'ROCE%':<8} {'3mRet%':<8} {'Base':<8} {'Penalty':<8} {'Adjusted':<10} {'Flags'}")
print("-" * 160)
for i, s in enumerate(stocks, 1):
    pv = f"{s['profitvar']:.2f}" if s['profitvar'] is not None else "—"
    sv = f"{s['salesvar']:.2f}" if s['salesvar'] is not None else "—"
    rc = f"{s['roce']:.2f}" if s['roce'] is not None else "—"
    rt = f"{s['ret3m']:.2f}" if s['ret3m'] is not None else "—"
    fl = ", ".join(s['flags']) if s['flags'] else ""
    print(f"{i:<5} {s['symbol']:<15} {s['name']:<25} {pv:<12} {sv:<12} {rc:<8} {rt:<8} {s['base_score']:<8} {s['penalty']:<8} {s['adjusted_score']:<10} {fl}")

print(f"\n\nTOP 15 (Working Universe):")
print("=" * 80)
for i, s in enumerate(stocks[:15], 1):
    print(f"{i}. {s['symbol']} ({s['name']}) - Adjusted PreRankScore: {s['adjusted_score']}")

# Output as JSON for further processing
top15 = []
for i, s in enumerate(stocks[:15], 1):
    top15.append({
        "prerank": i,
        "symbol": s["symbol"],
        "name": s["name"],
        "adjusted_score": s["adjusted_score"],
        "profitvar": s["profitvar"],
        "salesvar": s["salesvar"],
        "roce": s["roce"],
        "ret3m": s["ret3m"],
        "flags": s["flags"]
    })

with open("/workspaces/learn-trading-view-mcp/scripts/top15.json", "w") as f:
    json.dump(top15, f, indent=2)

# Full universe for reporting
full = []
for i, s in enumerate(stocks, 1):
    full.append({
        "prerank": i,
        "symbol": s["symbol"],
        "name": s["name"],
        "adjusted_score": s["adjusted_score"],
        "base_score": s["base_score"],
        "penalty": s["penalty"],
        "profitvar": s["profitvar"],
        "salesvar": s["salesvar"],
        "roce": s["roce"],
        "ret3m": s["ret3m"],
        "in_working_universe": i <= 15,
        "flags": s["flags"]
    })
with open("/workspaces/learn-trading-view-mcp/scripts/full_universe.json", "w") as f:
    json.dump(full, f, indent=2)
