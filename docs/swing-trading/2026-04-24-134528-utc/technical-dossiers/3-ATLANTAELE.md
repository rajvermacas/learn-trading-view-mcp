# ATLANTAELE — Technical Dossier

**Fundamental Rank**: #3 of 3
**Run Date**: 2026-04-24
**Technical Data Mode**: api_fallback (yfinance + stockstats; TradingView MCP disconnected)

---

## Snapshot

- **CMP**: ₹1,778.5 (intraday 2026-04-24 09:45 IST; gap-up session; prior daily close 1,617.2)
- **3% Floor**: ₹1,724.5
- **Practical Stop Zone**: ₹1,707 – ₹1,742 (2%–4% band)
- **Technical Verdict**: Watchlist (Reject for fresh entry at CMP)
- **Confidence**: Low
- **One-line Rationale**: Gap-up into all-timeframe overbought with no tested structure inside any viable stop zone.

## Timeframe Notes

**Weekly**: Only ~30 bars of weekly history available — limited significance for structural levels. Current week (ending Apr 20 close 1,617.2) is the range high for all data; prior week printed 1,375.7 close. Weekly MACD histogram strongly positive (72.83) and price well above all weekly EMAs — momentum intact but RSI unavailable and the weekly candle is a single data point at all-time highs.

**Daily**: Closed 1,617.2 on Apr 23 (all-time high), gapped up to 1,778.5 today — a ~10% gap on 535K volume. Daily MACD histogram has narrowed to 34.7 from prior highs, signaling momentum deceleration even before the gap. Daily EMA10 at 1,466 is far below — no EMA support within 15% of CMP. The gap has created an unfilled void between 1,617 and 1,778 with zero price structure tested.

**60m**: RSI 86.68 and MFI 0.96 — extreme overbought. Price above 60m Bollinger upper band (1,842 is upper); all EMAs stacked bullishly far below. MACD histogram compressing (13.27) — intraday impulse losing steam. No horizontal demand shelf in the gap zone — 60m chart is in price-discovery territory.

**30m (execution frame)**: Clearest warning frame — RSI 81.43, MACD histogram near zero (1.69), price pressing upper Bollinger band (1,789.85). 30m EMA10 (1,723) sits ~3% below CMP — only EMA-based stop reference, but untested since the gap open and carries no structural validation. 2%–4% stop zone (1,707–1,742) rests entirely in gap air — no prior candle body or swing low to anchor it.

**15m**: RSI 79.48, MACD histogram 2.93 and flattening, price above 15m Bollinger upper band (1,773.95 vs CMP 1,778.5). 15m EMA10 at 1,743 is closest level inside the stop zone, but reflects only ~2 hours of trading — not a tested demand level. All momentum oscillators diverging from price.

## Support Inventory

| Timeframe | Type | Level | Distance below CMP |
|-----------|------|-------|--------------------|
| 15m | EMA10 (untested, gap air) | 1,744 | ~1.9% |
| 30m | EMA10 (untested, gap air) | 1,723 | ~3.1% |
| 15m | EMA20 (untested, gap air) | 1,719 | ~3.3% |
| 30m | EMA20 (untested, gap air) | 1,677 | ~5.7% |
| Daily | Prior ATH close / gap top | 1,617 | ~9.1% |
| Daily | Apr 22 high (prior resistance) | 1,480 | ~16.8% |

## Resistance Inventory

| Timeframe | Type | Level | Distance above CMP |
|-----------|------|-------|--------------------|
| 30m | Bollinger Upper Band | 1,790 | ~0.6% |
| 60m | Bollinger Upper Band | 1,843 | ~3.6% |

## Trade Plan

- **Entry**: No entry recommended at current CMP. For fresh entry, wait for gap fill or consolidation to test and hold the 1,617–1,620 zone with a confirming reversal candle on the 30m or 60m.
- **Stoploss**: Any fresh entry stop below 1,600 (below Apr 23 close structure); trail to 1,700 only if CMP establishes two 30m closes above that level.
- **First Trouble Area**: 1,790 (30m Bollinger upper); 1,843 (60m Bollinger upper). Limited upside headroom (<3.6%) before band resistance.
- **Swing Target**: 1,900–1,950 if gap holds and 1,617 is re-tested and defended; speculative given no confirmed structure above 1,778.
- **Reasoning**: CMP is a 10% gap-up into all-time highs with no structural support within the 2%–4% stop zone — the entire zone is untraded gap air. All intraday oscillators (RSI 80–87, MACD flattening) confirm momentum deceleration at the open. 30m and 60m show a stock pressing Bollinger upper bands with no tested demand shelf, meaning a 2%–4% stop has no structural anchor and any gap-fill would violate it immediately.

## Hard Ban Audit

- **EMA distance alone**: Not used — no entry or stop justified solely by EMA proximity; all EMAs cited are untested in gap zone and lack structural confirmation.
- **One timeframe alone**: Not used — verdict draws on daily gap structure, 30m oscillator state, and 15m Bollinger breach jointly.
- **Duplicate EMAs**: Not used — EMAs cited come from distinct timeframes with distinct structural roles.
- **HTF fine LTF breaks**: Not applicable — daily HTF gap and all-time-high close are consistent with LTF overbought readings, not contradicted.

## Known Data Limitations

- Weekly and daily RSI return 0 (stockstats quirk); relying on intraday RSI only. Weekly data limited to ~30 bars (recent listing). Intraday reflects only first 15 minutes of 2026-04-24 session — full-day structure cannot be assessed. Gap-up session means all intraday EMAs are computed over pre-gap data and are not validated as demand zones.
