# Atlanta Electricals Ltd (ATLANTAELE)
Generated: 2026-05-14 | Fundamental Rank: #4 of 20 | Coverage: top 15 of top-20 working universe | Mode: api_fallback

## Core Fields
| Field | Value |
|---|---|
| symbol | ATLANTAELE |
| technical_data_mode | api_fallback |
| cmp | 1811.30 |
| 3pct_floor | 1756.96 |
| practical_stop_zone | 1738.85-1775.07 |

## Timeframe Notes
### weekly_note
- API evidence: `stock-1wk.json` + `indicators-1wk.json`; full EMA/MACD/RSI/VWMA/MFI surface present, no null-only limitation.
- Weekly structure still prints a higher-high/higher-low trend after the 1886.8 supply test; MACD/RSI are strong but stretched, so this is constructive and extended, not fresh.
- Volume from 4/20 (2.91m) through 5/11 (883k) shows demand absorbing the 5/4-5/6 washout; support is 1728.4-1757.0, resistance is 1846.2-1886.8.

### daily_note
- API evidence: `stock-1d.json` + `indicators-1d.json`; full indicator surface present, no null-only limitation.
- Daily structure is a violent flush to 1508.1 followed by a two-day reclaim to 1811.3, with price back above EMA10/20/50/100/200 and VWMA; MACD is still slightly below signal, so momentum is repaired but not fully clean.
- Volume on 5/12 (436.5k) and 5/13 (198.1k) follows the 5/11 one-price hold, which reads like acceptance; 1756.0-1728.4 is the support shelf and 1846.2-1886.8 remains supply.

### 60_note
- API evidence: `stock-60m.json` + `indicators-60m.json`; full indicator surface present, no null-only limitation.
- 60m reclaimed EMA10/20/50/100/200, but MACD histogram is still negative, so the recovery is controlled rather than impulsive; 1777.5 is the first meaningful intraday defense and 1720.5 is the deeper demand shelf.
- The last 60m bars held 1799-1811 with churn, not capitulation; a loss of 1777.5 would expose the 1759.8/1756.0 stop band and then 1728.4.

### 30_note
- API evidence: `stock-30m.json` + `indicators-30m.json`; full indicator surface present, no null-only limitation.
- 30m is the execution map: EMA10/20 sit above price, EMA50 is 1759.8, EMA100 is 1714.4, and VWMA 1818.0 is slightly above close; MACD below signal means consolidation under supply, not a fresh momentum burst.
- The 13:00-14:30 spikes into 1849.8/1833.4 were sold back to 1805-1811, but the close stayed above 1799 and the 15m EMA50, so the 1759.8-1756.0 support ladder is still intact.
- Pattern-wise the 1799-1811 range is a higher-low coil inside the rebound leg; supply sits at 1833.4-1849.8, and a break of 1777.5 would make the map fragile fast.

### 15_note
- API evidence: `stock-15m.json` + `indicators-15m.json`; full indicator surface present, no null-only limitation.
- 15m is constructive, with price above EMA10/20/50/100/200 and VWMA; MACD is positive and RSI is mid-50s, so the micro trend is holding but not overheating.
- The final bars oscillated between 1798 and 1827 with a late push to 1833, which is two-way trade rather than clean breakout impulse; 1794.1 is the first micro support, then 1777.5.

## Support Inventory
| Timeframe | Support Type | Price Level | Distance From CMP |
|---|---|---:|---:|
| 15m | EMA50 micro shelf | 1794.10 | -0.95% |
| 60m | EMA20 intraday defense | 1777.53 | -1.87% |
| 30m/Daily | EMA50 + daily low confluence | 1756.00-1759.77 | -3.05% to -2.86% |
| 60m/Weekly | EMA50 + weekly swing low | 1720.49-1728.40 | -5.01% to -4.58% |

## Resistance Inventory
| Timeframe | Resistance Type | Price Level | Distance From CMP |
|---|---|---:|---:|
| 15m/30m | Intraday supply | 1833.40-1849.80 | +1.22% to +2.13% |
| Weekly/Daily | Prior ATH supply | 1846.20-1886.80 | +1.93% to +4.17% |
| 60m | Bollinger upper | 1866.19 | +3.03% |
| Daily | Bollinger upper | 1965.02 | +8.49% |

## Trade Parameters
| Field | Value |
|---|---|
| entry_zone | 1777.53-1811.30; best on a shallow pullback that respects 60m EMA20 / 30m VWMA, or on a fresh reclaim through 1846.20. |
| stop_zone | 1748.00-1755.50; below the daily 1756.0 low and under the 30m EMA50 shelf, so a break there hands control back to the weekly 1728.4 base. |
| first_trouble_area | 1833.40-1849.80; immediate intraday supply before the prior ATH band. |
| swing_target | 1886.80-1965.02; clears the ATH and opens the daily Bollinger extension. |

## Verdict Fields
| Field | Value |
|---|---|
| technical_verdict | Constructive and stop-defendable. |
| stop_survivability_label | Defendable. |
| primary_failure_risk | A clean 30m/60m break of 1777.5 and 1756.0 would expose the 1728.4 weekly base; 1849.8-1886.8 is the upside hurdle. |
| ranking_reason | Strong sponsorship backdrop and a stacked 15m/30m/60m support ladder above the 3% floor make the stop usable; the only real caution is weekly extension and nearby intraday supply. |

## Summary Rationale
Weekly and daily trend are intact, and the latest close held the rebound after the 5/11 weekly low and the 5/12-5/13 acceptance sequence. The stop is defendable because 15m EMA50, 60m EMA20, and 30m EMA50/daily low cluster around 1794 / 1777 / 1756, giving real support density around the 3% floor instead of a bare EMA touch. Volume on 5/12 and 5/13 looks like absorption, not distribution, but 30m MACD below signal says this is a hold, not a launch. The thesis breaks first if 1777.5 fails; it fails hard below 1756-1748, which would reopen 1728.4, while upside still has to clear 1833-1849 before any 1887-1965 extension.
