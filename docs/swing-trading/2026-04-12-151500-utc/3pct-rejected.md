# Rejected Stocks — 2026-04-12

All rejections are categorized as either **fundamental** (did not pass minimum quality bar) or **technical** (good fundamentals but failed 3% support-density test).

---

## A. Fundamental Rejects (not analyzed technically)

| Symbol | CMP | ROCE % | NP Qtr Var % | Sales Qtr Var % | Rejection Reason |
|--------|-----|--------|-------------|----------------|-----------------|
| ABB | 6859 | 29.90 | -18.35 | +5.71 | Quarterly profit declined 18%; cannot justify tight stop |
| LUXIND | 1347 | 12.54 | -46.66 | +21.59 | Profit down 47%; fundamentally deteriorating |
| SUPREMEPETROCH | 745 | 22.76 | -50.25 | -10.01 | Both profit and sales contracting sharply |
| SGMART | 539 | 11.33 | -61.70 | +23.21 | Profit collapsed 62%; business quality unclear |
| VTL (Vardhman) | 561 | 10.83 | -21.02 | +1.62 | Profit declining; weak sales growth |
| RPSGVENT | 963 | 11.33 | -203.72 | +15.57 | Deep losses; P/E 3187 |
| JINDALPOLY | 770 | 5.36 | -453.42 | -68.66 | Loss-making; both metrics collapsing |
| STLTECH | 231 | 2.86 | +53.33 | +25.95 | Loss-making despite improving; P/E 941 |
| ATHERENERG | 863 | -65.71 | +59.76 | +50.20 | Loss-making; negative ROCE |
| DHENU | 9 | N/A | +4150 | -0.08 | Suspiciously low price; quarterly revenue ₹0.84 Cr |
| SEAMECLTD | 1525 | 8.60 | +3100 | +112.30 | ROCE too low for tight-stop swing despite profit jump |
| DALMIASUG | 371 | 9.48 | +17.64 | -16.70 | Low ROCE; declining sales |
| ROSSTECH | 916 | 8.18 | +18.27 | +71.55 | ROCE too low |
| HFCL | 84 | 7.55 | +32.55 | +19.65 | ROCE too low; P/E 249 |

---

## B. Technical Rejects (passed fundamental, failed 3% support test)

Stocks below had acceptable fundamentals but did not have enough EMA layers within 3% below CMP to justify entry under the 3% stop rule.

| Symbol | CMP | 3% Floor | Hourly EMA layers in 3% | Reason |
|--------|-----|----------|------------------------|--------|
| SHILCTECH | 4574 | 4437 | 1 (EMA10 at 1.16%) | EMA20 at 4422 = 3.32% away, below floor |
| GVT&D | 4067 | 3945 | — | Classified as Watch (2 layers, 1.14% and 2.97%) |
| ATLANTAELE | 1310 | 1271 | — | Classified as Watch |
| PREMIERENE | 975 | 946 | — | Classified as Watch (tangled daily EMAs) |
| SCHNEIDER | 1010 | 980 | 1 (EMA10 at 1.69%) | EMA20 at 978 = 3.15%, just below floor |
| APARINDS | 11342 | 11002 | 1 (EMA10 at 1.93%) | EMA20 at 10901 = 3.89%, below floor |
| TDPOWERSYS | 927 | 899 | — | Classified as Watch |
| PRECWIRE | 340 | 329 | 1 (EMA10 at 2.00%) | EMA20 at 325 = 4.28%, below floor |
| QPOWER | 962 | 933 | 0 (price below EMA10) | Price has pulled below hourly EMA10; bearish hourly signal |
| AVANTIFEED | 1459 | 1415 | 0 | Even hourly EMA10 (1399) is 4.12% away; news-driven spike, daily volume 10x average |
| AEROFLEX | 289 | 280 | 1 (EMA10 at 1.43%) | EMA20 at 277 = 4.06%, below floor |
| KRN | 969 | 940 | — | Classified as Watch |
| PARKHOSPS | 210 | 204 | — | Classified as Watch |
| POWERINDIA | 28425 | 27572 | 1 (EMA10 at 1.99%) | EMA20 at 27224 = 4.23%, below floor |
| BAJAJCON | 432 | 419 | 0 | Hourly EMA10 (418) is below 3% floor; daily volume 5x average |
| EBGNG | 409 | 397 | 0 | Hourly EMA10 (396) is 3.16% away, just below floor |
| SHARDACROP | 1057 | 1026 | 1 (EMA20 at 1.57%) | Price slipped below hourly EMA10; tangled daily EMA stack |
| PFOCUS | 335 | 325 | N/A | ROCE 7.95%; not analyzed technically |
| SHILPAMED | 420 | 407 | N/A | ROCE 7.82%; not analyzed technically |
| GVPIL | 462 | 448 | N/A | ROCE 6.09%; not analyzed technically |
| MTARTECH | 4174 | 4049 | N/A | ROCE 10.51%; not analyzed technically |
| ARVIND | 390 | 378 | N/A | ROCE 13.04%; not analyzed technically |
| KSHINTL | 534 | 518 | N/A | NP Qtr -4.62%; not analyzed technically |
| MANINDS | 466 | 452 | N/A | ROCE 15.98%; lower-priority; not analyzed |
| KIRLOSENG | 1473 | 1429 | N/A | ROCE 13.68%; not analyzed technically |

---

## Key Pattern

The dominant rejection reason is **"only 1 hourly EMA within 3%."** This screen selects stocks that have run 30%+ in 3 months; most of them have left all meaningful support layers far below. Entry into these stocks with a 3% hard stop has extremely thin margin: one bad hourly candle hits the stop before any support has a chance to hold.

The correct approach is to watch the rejected names that have good fundamentals and wait for price to consolidate long enough that shorter-period EMAs (EMA50, EMA100 on daily) climb into the 3% window.
