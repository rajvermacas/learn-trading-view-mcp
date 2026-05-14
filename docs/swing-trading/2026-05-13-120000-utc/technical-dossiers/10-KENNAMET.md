# KENNAMET Technical Dossier

## Verdict
Conditional watchlist, not a chase at CMP. KENNAMET has a strong bullish EMA stack, but price is stretched after a sharp move and daily ATR is wider than the allowed 3% risk band. Trade only on a tight lower-timeframe setup.

## Price/3pct Envelope
- CMP: `3077.10` from fetched 2026-05-13 close
- 3% floor: `2984.79`
- Proposed stop: `3038.00`, about `1.27%` below CMP
- Daily ATR14: `181.74`, about `5.91%` of CMP, so a daily-structure stop is not feasible under the 3% rule
- Data note: bundled daily OHLCV fetch returned only 17 rows from 2026-04-20 to 2026-05-13; intraday and indicator artifacts were fetched under `api/10-KENNAMET`.

## Trend & Momentum
Daily trend is bullish: CMP is above EMA20 `2837.31`, EMA50 `2779.52`, and EMA200 `2749.40`. RSI14 is elevated at `72.61`, MACD is positive with histogram `25.74`.

Weekly is also bullish but overheated: weekly RSI `91.95`. Lower timeframes are mixed: 30m RSI `52.91` with positive MACD histogram, while 60m MACD histogram is negative, showing momentum cooling.

## Support/Resistance
- Immediate support: `3060-3040`, aligned with 15m/30m structure and 30m EMA50 near `3039.13`.
- Rule floor support: `2984.79`; below this the 3% setup fails.
- Deeper support: `2962-2964`, but that is below the 3% floor and not acceptable for this mandate.
- Resistance: `3128-3147`, then `3180`; spike/supply zone near `3400`.

## Entry Plan
Preferred trigger: enter only above `3148` after price clears the `3128-3147` resistance band with volume holding above recent intraday averages.

Alternative pullback trigger: price holds `3040-3060`, then reclaims `3099` on 30m closing strength. No entry if price drifts below `3040`.

## Risk Controls
Use stop `3038.00`. Do not widen below `2984.79`. Invalidate on a 30m close below `3038` or any failed breakout that rejects below `3128` with rising volume.

Initial target zone: `3180`. Stretch target: `3400`. If entering near `3148`, move risk down only after sustained trade above `3180`; otherwise reward/risk is marginal.

## Final Call
Watchlist / conditional long only. The franchise quality supports interest, but the chart is extended and daily volatility is too large for a clean 3% swing stop. Take it only if the `3148` breakout confirms or a controlled `3040-3060` pullback holds.
