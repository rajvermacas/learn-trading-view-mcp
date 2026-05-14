# Acutaas Chemicals Ltd (ACUTAAS) Technical Dossier
*Generated: 2026-05-12 | Fundamental Rank: #6 of 20 | Coverage: api_fallback redo for one stock*

## Core Fields
- **symbol**: ACUTAAS
- **company**: Acutaas Chemicals Ltd
- **technical_data_mode**: api_fallback
- **cmp**: 2810.30
- **3pct_floor**: 2725.99
- **practical_stop_zone**: 2697.89-2754.09

## Timeframe Notes

### weekly_note
- API evidence: `stock-1wk.json` has 7 rows and `indicators-1wk.json` has all required EMAs; market structure is a sharp recovery from 2073 to a fresh 2825 high, with prior 2635 supply cleared and no proven overhead shelf yet.
- EMA context is strongly bullish but extended: close 2810.30 is above weekly EMA10 2465.83, EMA20 2253.08, EMA50 1981.38, EMA100 1860.50, and EMA200 1797.28; RSI 72.26 and ATR 210.00 warn that a normal weekly shakeout can exceed 3%.
- Pattern is breakout continuation, not a base entry; volume expanded on the 2710 breakout week and faded on the current partial week, so demand exists below, but weekly support sits mostly under the practical stop band.

### daily_note
- API evidence: `stock-1d.json` has 27 rows and `indicators-1d.json` has all required EMAs; daily structure is higher highs and higher lows from the 2073 April low, with the May lows stepping 2538 -> 2604.5 -> 2664 -> 2700 -> 2728.5.
- EMA context is bullish but stretched: CMP is above daily EMA10 2648.71, EMA20 2546.80, EMA50 2364.26, EMA100 2163.76, and EMA200 1966.52; daily RSI 72.48 and ATR 110.99 make a 3% stop tight for a daily swing.
- Demand sits at 2700-2730 from the last two daily lows and broken 2759 resistance; resistance/supply is the new 2825 high, with continuation needing acceptance above that level on volume.

### 60_note
- API evidence: `stock-60m.json` has 185 rows and `indicators-60m.json` has all required EMAs; hourly structure shows an orderly climb, then a late May 11 thrust from 2758 to 2825 on the highest recent hourly volume.
- EMA stack supports trend: EMA10 2770.02, EMA20 2746.07, EMA50 2677.54, EMA100 2588.57, EMA200 2477.27; the 2%-3% band aligns with EMA20 and the 2730-2758 intraday demand shelf.
- Pattern is a breakout from a 2700-2760 range; first failure risk is a loss of 2730-2746, because below that the next meaningful hourly defense is closer to EMA50 near 2678.

### 30_note
- API evidence: `stock-30m.json` has 342 rows and `indicators-30m.json` has all required EMAs; this execution frame shows support density at EMA20 2763.55, EMA50 2726.74, and the May 8/11 demand shelf at 2726-2741.
- Market structure remains higher-low constructive, but the final push into 2825 came after a narrow midday base and high closing volume, so a pullback to 2760-2730 would be normal rather than broken.
- Resistance is immediate at 2824-2825; acceptance above it opens the 2890-2960 target zone, while a 30m close below 2726 would turn the breakout into a likely failed move.

### 15_note
- API evidence: `stock-15m.json` has 656 rows and `indicators-15m.json` has all required EMAs; micro structure improved late on May 11 with rising volume through 2784-2825.
- EMA context supports the lower-timeframe stop map: EMA10 2792.90, EMA20 2777.56, EMA50 2754.28, EMA100 2723.36, EMA200 2661.34; the 3% floor sits just above EMA100.
- Demand is layered at 2754-2765, 2723-2741, and 2661-2678; if 2723 breaks quickly, the lower-timeframe air pocket points toward the 2670s.

## Support Inventory (`support_inventory`)
| Timeframe | Support Type | Price Level | Distance from CMP |
|---|---|---:|---:|
| 15m | EMA50 / upper stop band | 2754.28 | -1.99% |
| 60m | EMA20 | 2746.07 | -2.29% |
| 30m | May 8/11 demand shelf | 2726-2741 | -3.00% to -2.47% |
| 30m | EMA50 / 3pct floor confluence | 2726.74 | -2.97% |
| 15m | EMA100 | 2723.36 | -3.09% |
| 1d | Recent daily lows | 2700-2728.5 | -3.93% to -2.91% |
| 60m | EMA50 deeper support | 2677.54 | -4.72% |

## Resistance Inventory (`resistance_inventory`)
| Timeframe | Resistance Type | Price Level | Distance from CMP |
|---|---|---:|---:|
| 30m/60m/1d | Fresh breakout high / first supply | 2824-2825 | +0.49% to +0.52% |
| 1d | Continuation trouble band | 2890-2960 | +2.84% to +5.33% |
| 1d/weekly | Psychological extension target | 3000 | +6.75% |

## Trade Parameters
- **entry_zone**: 2730-2765 is the preferred execution zone because it retests the 30m/60m support stack; chasing 2810 leaves the stop dependent on fresh breakout acceptance.
- **stop_zone**: 2695-2725; this brackets the 3% floor, 15m EMA100, 30m EMA50, and recent daily lows, but a daily close below 2695 invalidates the near-term breakout.
- **first_trouble_area**: 2824-2825; failure to hold or clear this fresh high after the May 11 volume thrust would signal supply absorption is incomplete.
- **swing_target**: 2890-2960 first, then 3000 only if price accepts above 2825 with expanding volume.

## Verdict Fields
- **technical_verdict**: Watchlist / buy only on pullback or confirmed hold above 2825
- **stop_survivability_label**: Near-Valid
- **primary_failure_risk**: The stock is extended on daily and weekly charts; a routine ATR pullback can break the 3% floor before the fundamental thesis is invalidated.
- **ranking_reason**: Fundamental rank #6 of 20; Strongly Sponsored for Q4/FY26 acceleration, margins, low leverage, and FY27 growth bridge, but valuation and project-execution fragility make a stretched technical entry less forgiving.

## Summary Rationale (`summary_rationale`)
ACUTAAS has real stop support around the 3% floor: the 30m EMA50, 15m EMA100, hourly EMA20, and recent 2700-2730 daily lows all sit in or near the 2698-2754 practical stop band. That makes the setup constructive, not EMA-only.

The issue is entry quality. Weekly and daily trend are strong, but RSI is above 72 on both frames and CMP is well above the daily EMA10 and weekly EMA10. The 30m chart is the key frame: a pullback that holds 2730-2765 keeps the support stack intact, while a quick break of 2723-2726 exposes an air pocket toward 2678 and makes the stop likely to fail.
