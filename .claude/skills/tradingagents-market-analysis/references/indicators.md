# Supported Indicators

## Indicator Set

- `close_50_sma`
- `close_200_sma`
- `close_10_ema`
- `macd`
- `macds`
- `macdh`
- `rsi`
- `boll`
- `boll_ub`
- `boll_lb`
- `atr`
- `vwma`
- `mfi`

## Interpretation Guidance

### Trend

- `close_50_sma`: medium-term trend and dynamic support or resistance
- `close_200_sma`: long-term trend benchmark
- `close_10_ema`: short-term trend sensitivity

### Momentum

- `macd`: direction and crossover context
- `macds`: MACD signal-line comparison
- `macdh`: momentum expansion or contraction
- `rsi`: overbought, oversold, and divergence context
- `mfi`: volume-aware momentum confirmation

### Volatility

- `boll`: Bollinger middle line
- `boll_ub`: upper-band pressure or breakout context
- `boll_lb`: lower-band exhaustion or oversold context
- `atr`: volatility and stop-width context

### Volume

- `vwma`: price trend weighted by volume participation

## Usage Notes

- Prefer a balanced set instead of all indicators at once.
- Use exact indicator names from this file.
- Read indicator output in context of price structure, not in isolation.
- Expect `null` values during look-back warm-up periods.
