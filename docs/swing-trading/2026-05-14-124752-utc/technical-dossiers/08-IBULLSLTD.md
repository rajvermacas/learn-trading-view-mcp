# Indiabulls Limited (IBULLSLTD)
_Analysis date: 2026-05-14 | Fundamental rank: #8 | Coverage: api_fallback_

## Core Fields
- `symbol`: `IBULLSLTD`
- `technical_data_mode`: `api_fallback`
- `cmp`: `19.55`
- `3pct_floor`: `18.96`
- `practical_stop_zone`: `18.82-18.94`

## Timeframe Notes
### `weekly_note`
- Market structure stays bullish: the weekly chart still prints a higher-high / higher-low sequence and price holds above the full EMA stack from 10 through 200.
- Pattern is a post-breakout consolidation under the 21.70-22.78 supply zone, not a failed trend; support is still the 18.94 breakout shelf.
- Volume was heaviest on the breakout weeks, then eased on the latest pullback; API evidence: `stock-1wk.json`, `indicators-1wk.json`. Indicators were populated, so no null-current limitation was accepted.

### `daily_note`
- Daily structure is a strong impulse followed by a controlled pullback: the close remains above the 20/50/100/200 EMA cluster even while it sits under the 10 EMA.
- The pattern is a breakout-and-pause after the 19.73/20.20 run-up, with demand visible near 19.35 and prior structural demand at 18.94-18.36.
- Volume expanded on the breakout days and contracted on the last two red sessions; API evidence: `stock-1d.json`, `indicators-1d.json`. Indicators were populated, so no null-current limitation was accepted.

### `60_note`
- 60m structure is a shallow pullback inside an intact intraday trend; price is below the 10/20/50 EMA trio but still above the 100/200 EMA anchors.
- The working pattern is a tightening range after the 20.92 swing high, with demand at 19.35 and supply at 19.75-20.20.
- Volume on the sellback was not climactic enough to imply distribution; API evidence: `stock-60m.json`, `indicators-60m.json`. Indicators were populated, so no null-current limitation was accepted.

### `30_note`
- 30m is the main execution frame: price is holding the 19.35-19.45 demand pocket after a fast run, even though it is still capped by the 10/20/50 EMA cluster overhead.
- The chart is a compact pullback/flag under 20.20, with no confirmed lower-low through the practical stop band; that keeps the stop path intact for now.
- Volume spiked into the final bar, but the bar still held above the intraday demand shelf; API evidence: `stock-30m.json`, `indicators-30m.json`. Indicators were populated, so no null-current limitation was accepted.

### `15_note`
- 15m structure is constructive but fragile: the tape is coiling above 19.42-19.35 and has not broken the micro-demand shelf.
- Pattern is a small consolidation after the afternoon push, with supply at 19.67-19.75 and demand at 19.35-19.45.
- The close came on elevated volume after repeated tests of support, which argues for absorption more than for breakdown; API evidence: `stock-15m.json`, `indicators-15m.json`. Indicators were populated, so no null-current limitation was accepted.

## Support Inventory
| timeframe | support type | price level | distance from CMP |
| --- | --- | ---: | ---: |
| 15m | micro demand shelf | 19.42 | -0.7% |
| 30m | intraday demand shelf | 19.35 | -1.0% |
| 1d | prior breakout low | 18.94 | -3.1% |
| 1d | 20 EMA support | 18.36 | -6.1% |
| 1wk | breakout base shelf | 17.58 | -10.1% |

## Resistance Inventory
| timeframe | resistance type | price level | distance from CMP |
| --- | --- | ---: | ---: |
| 15m | micro supply | 19.75 | +1.0% |
| 30m | overhead flag cap | 20.20 | +3.3% |
| 1d | impulse stall / first hurdle | 20.85 | +6.6% |
| 1d | swing retrace high | 21.04 | +7.6% |
| 1wk | prior breakout high | 22.78 | +16.5% |

## Trade Parameters
- `entry_zone`: `19.35-19.60`  
  Lower frames are still defending the demand shelf, so the entry should be tied to that hold rather than chased above the short EMA cluster.
- `stop_zone`: `18.82-18.94`  
  This sits just under the 3% floor and beneath the daily breakout shelf, so a loss there would mean the pullback has become a real structure break.
- `first_trouble_area`: `19.75-20.20`  
  Intraday supply and the daily stall zone sit here first, so upside needs to clear this band before the move can re-extend.
- `swing_target`: `21.70-22.78`  
  The next credible reward band is the weekly supply / prior peak area; that is the level cluster that would confirm the breakout leg is still alive.

## Verdict Fields
- `technical_verdict`: `Defendable long setup, but only on a hold of 19.35-18.94 support`
- `stop_survivability_label`: `Moderately defendable`
- `primary_failure_risk`: `30m and 60m lose 19.35, which exposes 18.94 quickly and can turn the pullback into a failed breakout`
- `ranking_reason`: `Fundamental rank #8 has a real catalyst behind it, and the chart still respects the post-breakout base, but the move is extended enough that only clean lower-timeframe support justifies the stop`

## Summary Rationale
The stop zone is defendable because the weekly and daily trends are still intact, the 30m and 15m charts are holding a real demand shelf, and the pullback has not yet opened an air pocket into the stop zone. The most important alignment is the lower-timeframe defense of 19.35-19.42 while the daily chart stays above the 18.94 breakout shelf. What would invalidate the thesis first is a clean loss of 19.35 on the 30m/60m tape, because that would put 18.94 and then the daily 20 EMA directly in play. Volume and structure still favor absorption over distribution, but the setup is not clean enough to ignore the overhead 19.75-20.20 supply.
