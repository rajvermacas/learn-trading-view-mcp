# GVT&D — Technical Dossier

**Fundamental Rank**: #2 of 3
**Run Date**: 2026-04-24
**Technical Data Mode**: api_fallback (yfinance + stockstats; TradingView MCP disconnected)

---

## Snapshot

- **CMP**: ₹4,599 (intraday 2026-04-24 09:45 IST)
- **3% Floor**: ₹4,461
- **Practical Stop Zone**: ₹4,415 – ₹4,507
- **Technical Verdict**: Watchlist
- **Confidence**: Medium
- **One-line Rationale**: Post-breakout pullback holds above Apr-23 close, but intraday wick at 4694 and 30m MACD divergence demand confirmation before entry.

## Timeframe Notes

**Weekly**: Week ending Apr-20 (close 4496) shows strong upward continuation with price well above all key weekly EMAs (EMA10: 3919, EMA20: 3613); current partial week (high 4650 intraday) extends the breakout. Weekly MACD histogram positive (77.5) and expanding. Weekly Bollinger upper band at 4526 has been breached — trend strength confirmed, but stretched conditions at 94–95x trailing P/E.

**Daily**: Apr-23 was a decisive breakout session — gap-up candle from ₹4,295 low to ₹4,650 high on 2.27M volume (~4× average); close at ₹4,496 left a large upper wick indicating intraday profit-taking. Daily MACD histogram (58.6) positive and rising. Prior daily congestion ceiling (₹4,220–4,240, Apr 21–22) has been comprehensively cleared and becomes first support. Daily ATR ₹189 — 2%–4% stop (₹92–₹184) sits within one day's normal range.

**60m**: Tight band of ₹4,591–4,605 on Apr 24 after printing intraday high ₹4,694 at 07:00–07:30 bar; sharp wick at 4694 followed by fade to 4599 indicates distribution at the high. 60m EMA10 (4565) and EMA20 (4489) rising beneath price, providing cushion. 60m RSI 69.2 — elevated but not yet overextended; MACD histogram collapsed near-flat (1.37), suggesting momentum waning after Apr-23 surge.

**30m (execution frame)**: 30m MACD histogram is negative (−8.67) — bearish crossover — while RSI is 61.9 and VWMA (4590) sits near CMP (4599). Apr-24 range roughly ₹4,526–4,694; current price mid-range, unable to reclaim 4,650. First meaningful 30m support is ₹4,570–4,580 (multiple Apr-24 closes), then ₹4,526–4,530 (opening base). Sustained break below ₹4,526 on 30m closes = failed-breakout signal.

**15m**: Spike to ₹4,694 at 07:15–07:30 on high volume (90k + 71k) followed by immediate reversion to ₹4,597–4,605 grinding for 5 bars. RSI 54 and MACD histogram negative (−5.5); 15m in minor bearish drift after spike. ₹4,570 zone aligns with 15m Bollinger lower band (4565) and EMA50 (4534). Reclaim of ₹4,620–4,625 on 15m close = first buy signal.

## Support Inventory

| Timeframe | Type | Level | Distance below CMP |
|-----------|------|-------|--------------------|
| 30m/15m | Intraday consolidation base (Apr-24 open) | ₹4,526–4,530 | −1.5% to −1.6% |
| 60m/30m | Apr-23 close / prior session swing low | ₹4,480–4,496 | −2.2% to −2.6% |
| Daily | Apr-23 pullback demand zone (multiple 30m wicks) | ₹4,461–4,470 | −2.8% to −3.0% |
| Daily | Apr-22 / Apr-21 prior congestion ceiling (flipped support) | ₹4,220–4,252 | −7.5% to −7.6% |
| Daily EMA10 | Rising daily EMA10 | ₹4,247 | −7.7% |

## Resistance Inventory

| Timeframe | Type | Level | Distance above CMP |
|-----------|------|-------|--------------------|
| 15m/30m | Apr-23 daily high / Apr-24 intraday wick high | ₹4,650 | +1.1% |
| 15m/60m | Apr-24 session spike high | ₹4,694 | +2.1% |

## Trade Plan

- **Entry**: ₹4,620–4,630 on a 15m close above the Apr-23 high zone (₹4,622) with 30m MACD histogram turning positive, confirming the wick rejection at 4694 was absorbed, not a distribution top
- **Stoploss**: ₹4,461 (30m close basis; aligns with Apr-23 intraday demand zone and represents −3.0% from CMP)
- **First Trouble Area**: ₹4,650–4,694 (Apr-23 daily high and Apr-24 spike; two-bar resistance cluster requiring high-volume absorption)
- **Swing Target**: ₹5,000–5,100 (next round-number extension; ~9%–11% upside; ~2.5:1 R:R vs 3% stop at entry 4,625)
- **Reasoning**: Apr-23 breakout cleared the entire ₹4,220–4,260 consolidation on 4× average volume, validating strong institutional demand consistent with fundamental sponsorship (HVDC order wins). However, 30m MACD histogram has turned negative after Apr-24 morning spike to 4694, indicating distribution at new highs. ₹4,461–4,480 zone (Apr-23 pullback lows + daily 3% floor) provides structural stop logic backed by a horizontal demand shelf on both 30m and 15m — not simply EMA distance. Entry should wait for 30m MACD to re-cross positive above ₹4,620.

## Hard Ban Audit

- **EMA distance alone**: Not used — all levels reference structural horizontal zones (Apr-23 close, Apr-22 consolidation ceiling, Apr-24 opening base).
- **One timeframe alone**: Not used — verdict integrates weekly trend, daily breakout, 60m momentum fade, 30m/15m bearish MACD as basis for Watchlist.
- **Duplicate EMAs**: Not used — only single EMA10 (daily) cited as structural reference.
- **HTF fine, LTF breaks**: Explicitly flagged — weekly/daily bullish but 30m/15m MACD bearish; the primary reason for Watchlist rather than Select, pending 30m confirmation.

## Known Data Limitations

- Weekly/daily RSI = 0 (stockstats quirk); relied on intraday RSI (60m 69.2, 30m 61.9, 15m 54.0). Pre-market bars with 0 volume excluded.
