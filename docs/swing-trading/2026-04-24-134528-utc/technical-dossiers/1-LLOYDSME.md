# LLOYDSME — Technical Dossier

**Fundamental Rank**: #1 of 3
**Run Date**: 2026-04-24
**Technical Data Mode**: api_fallback (yfinance + stockstats; TradingView MCP disconnected)

---

## Snapshot

- **CMP**: ₹1,686.70 (intraday 2026-04-24 09:45 IST); prior daily close 2026-04-23 = ₹1,697.80
- **3% Floor**: ₹1,636.10
- **Practical Stop Zone**: ₹1,619.2 – ₹1,653.0
- **Technical Verdict**: Watchlist
- **Confidence**: Medium
- **One-line Rationale**: Steep 5-week rally places CMP above every EMA with thin intraday support; the stop zone holds structure but requires confirmation of a pullback base before entry.

## Timeframe Notes

**Weekly**: Last 5 weekly candles form an unbroken staircase from 1388 to 1698, each closing near its high — a clean impulsive advance with zero weekly lower-close reversals. CMP is dramatically extended above weekly EMA10 (1417) and EMA20 (1344); MACD histogram of 56.76 confirms momentum but weekly ATR of 120.85 implies a ~7% weekly range is normal — extension risk is high. Closest weekly support cluster sits near 1618–1629 (week of 2026-04-20 low).

**Daily**: Sequence of higher lows and higher closes since 26 January low (~1073); every session from 17 April onward closed above prior day's open. Daily EMA10 (1609) is 4.6% below CMP — outside the stop zone — so EMA alone cannot anchor the stop. Structural lows of 1665.9 (Apr-23), 1645.0 (Apr-22), 1628.4 (Apr-21) constitute the visible support shelf. Last three daily candles progressively smaller-bodied — early deceleration signal. No visible daily resistance above until all-time-high territory near 1701.

**60m**: Price opened at 1698 and fell to 1686 within first 45 minutes of 24 April — inside range suggests distribution pressure at prior high. 60m EMA10 (1689) and EMA20 (1679) stacked bullishly below CMP, forming demand shelf between 1679–1689; 60m MACD histogram is negative (-3.72) — momentum flipped bearish at this timeframe. 60m Bollinger lower band at 1669.7 aligns with broader demand. Sustained close below 1669 on 60m would invalidate intraday structure.

**30m (execution frame)**: EMA20 (1686.8) is essentially at CMP — stock sitting on short-term dynamic support. EMA50 (1666.9) is 1.17% below providing secondary cushion; Bollinger lower band (1669.72) layers confluence between 1666–1670. 30m MACD histogram (-0.16) is essentially flat — momentum neutral. RSI 52.6. A 30m close back above 1698–1701 with volume expansion would confirm demand absorption and offer a clean risk-defined entry.

**15m**: MACD histogram turned marginally positive (0.21) — micro-momentum improving off the morning dip. RSI at 46.9 is sub-neutral. Recent 50-bar low of 1662.8 marks nearest intraday floor and sits just inside the stop zone. 15m EMA50 (1684) immediately below CMP, tested twice this session. Break below 1680 without recovery exposes 1669–1671 cluster. Air-pocket risk exists between 1665 and 1645 (gap of ~1.2%).

## Support Inventory

| Timeframe | Type | Level | Distance below CMP |
|---|---|---|---|
| 15m / 30m | Bollinger Lower Band confluence | 1669–1671 | 0.93%–1.05% |
| 30m | EMA50 | 1666.9 | 1.17% |
| Daily | Prior day low (Apr-23) | 1665.9 | 1.23% |
| 15m | Recent 50-bar intraday low | 1662.8 | 1.42% |
| Daily | Apr-22 swing low | 1645.0 | 2.47% |
| Daily | Apr-21 swing low | 1628.4 | 3.46% |
| Weekly | Week-of-Apr-20 candle low | 1618.4 | 4.05% |

## Resistance Inventory

| Timeframe | Type | Level | Distance above CMP |
|---|---|---|---|
| Daily / 60m | Prior intraday high / ATH area | 1701.0 | 0.85% |
| 60m | Bollinger Upper Band | 1701.7 | 0.89% |
| 30m | Bollinger Upper Band | 1703.8 | 1.01% |
| 15m | Bollinger Upper Band | 1706.1 | 1.15% |

## Trade Plan

- **Entry**: 1698–1702 (breakout above prior high on 30m close with volume; OR pullback entry at 1669–1672 if 30m EMA50 + Bollinger LB cluster holds as a base candle)
- **Stoploss**: 1618 (below Apr-20 weekly candle low; ~4.1% below CMP; respects the full stop zone floor)
- **First Trouble Area**: 1701–1706 (multi-timeframe Bollinger upper band convergence; resistance wall from 15m through 30m to 60m)
- **Swing Target**: 1780–1800 (daily Bollinger upper band at 1779; ~5.5% upside from CMP, giving ≥1.3R)
- **Reasoning**: Weekly/daily structure confirm impulsive trend with ladder of higher lows since January; any pullback to the Apr-21/22 swing-low shelf (1628–1645) lands inside the 2%–4% stop zone and represents genuine structural defense, not just EMA proximity. On the 30m execution frame, EMA20/EMA50 + Bollinger lower band cluster between 1666–1672 forms a tight demand block; base candle printed here with recovering 30m RSI above 55 would offer risk-defined entry where structural support from two timeframes overlaps inside the stop zone.

## Hard Ban Audit

- **EMA distance alone**: Verdict uses structural swing lows (Apr-21/22/23 daily lows) and Bollinger band confluence; EMAs corroborate, not drive.
- **One timeframe alone**: All five timeframes integrated — weekly trend, daily structure, 60m demand shelf, 30m execution frame, 15m micro HL.
- **Duplicate EMAs**: EMA10/20/50 from 30m are each cited once for a specific level; no double-counting.
- **HTF fine, LTF breaks**: 60m MACD negative and 15m RSI<50 caution signals are explicitly incorporated in the Watchlist (not Select) verdict and the base-candle requirement before entry.

## Known Data Limitations

- Weekly and daily RSI returned 0 (stockstats quirk for long intervals) — RSI used only on 60m/30m/15m; MACD and price structure substitute on weekly/daily.
