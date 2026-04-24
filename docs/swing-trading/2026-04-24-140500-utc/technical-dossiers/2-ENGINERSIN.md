# Engineers India Ltd (ENGINERSIN) — Technical Dossier

**Analysis Date:** 2026-04-24 | **Fundamental Rank:** #2 of 3 | **Coverage Mode:** full | **Data Mode:** api_fallback

## Core Fields

| Field | Value |
|---|---|
| symbol | ENGINERSIN |
| technical_data_mode | api_fallback |
| cmp | ₹243.68 |
| 3pct_floor | ₹236.37 |
| practical_stop_zone | ₹234.00–₹238.81 |

## Timeframe Notes

### weekly_note
- Market structure strongly bullish: 5-bar sequence 189→201→214→242→244; all EMAs (10/20/50/100/200 at 213/205/199/191/173) stacked below price; Apr 13 week vol 42.8M was the impulse; API: weekly OHLCV + EMA/RSI/MACD/BB via stockstats/yfinance; no indicator limitation.
- Current week doji-like body (O=241, H=250.39, L=236.71, C=243.68, vol 22.4M) — consolidation; price above weekly BB UB (240.71) = stretched, mean-reversion risk present.
- Demand: higher low structure intact; weekly low 236.71 is primary weekly support at −2.86% from CMP, inside the stop zone.

### daily_note
- Apr 17 breakout (O=230, H=247.56, L=229.48, vol 24.9M) is the impulse bar; Apr 20–23 consolidation without material selling is healthy absorption; API: daily OHLCV + EMA/RSI/MACD/BB/ATR via stockstats/yfinance.
- Daily ATR = 9.39 (3.85% of CMP) — matches the full stop zone width; a single adverse daily bar can mechanically pierce stop without structural break; daily EMA10 (233.80) at −4.05% sits below stop zone.
- RSI=71.45, MACD=12.75 — overbought but not extreme; daily BB UB (258.56) leaves headroom; structural anchor = Apr 17 swing low 229.48.

### 60_note
- 60m: tight consolidation range 241.24–250.29 with gentle drift lower — range compression; API: 60m OHLCV + EMA/RSI/MACD/BB/ATR via stockstats/yfinance; no warm-up caveat on 60m EMAs.
- 60m EMA50 at 237.61 (−2.49%) is rising dynamic support just inside the 2% stop edge; 60m BB LB at 240.98 (−1.11%) is immediate intraday floor.
- RSI=50.93, MACD=0.86 — neutral; no supply pressure visible; demand bracket: 240.98 (BB LB) and 237.61 (EMA50) cover the upper stop zone.

### 30_note
- 30m primary execution frame: bar sequence 246→246→245→244→244 with RSI=45.60, MACD=−0.38 — mildly bearish vs. bullish daily/weekly; API: 30m OHLCV + EMA/RSI/MACD/BB/ATR; EMA200 (225.57) warm-up insufficient (55-day limit) — directional use only.
- 30m EMA50 (242.51, −0.48%) and BB LB (241.65, −0.83%) are immediate support; 30m EMA100 at 236.37 coincides exactly with 3% floor — reinforces zone but single-timeframe coincidence.
- Supply: rejection from 250.39 (week high); 30m BB UB (245.98) acting as near-term lid; break below 241.65 opens path to 237–236 cluster.

### 15_note
- 15m: sideways drift (244→243→244→244→244), RSI=46.59, MACD=−0.29 — mildly bearish intraday; API: 15m OHLCV + EMA/RSI/MACD/BB/ATR; EMA200 (235.72) warm-up insufficient — corroborative only, not decisive.
- 15m EMA50 (243.68=CMP) and EMA100 (242.26, −0.58%) form immediate support; BB (241.93–244.22) at ±0.94% is very narrow — compression breakout direction will define next 1–2% move.
- No supply until 246–250 band; demand 242–243 well-defined; intraday sellers held above 241.24 all week.

## Support Inventory

| Timeframe | Support Type | Price Level | Distance from CMP |
|---|---|---|---|
| 15m | EMA50 | 243.68 | 0.00% |
| 30m | EMA50 | 242.51 | −0.48% |
| 15m | EMA100 | 242.26 | −0.58% |
| 30m | BB Lower Band | 241.65 | −0.83% |
| 60m | BB Lower Band | 240.98 | −1.11% |
| 60m | EMA50 | 237.61 | −2.49% |
| Weekly | Week Low (Apr 20) | 236.71 | −2.86% |
| 30m | EMA100 | 236.37 | −3.00% |
| 15m | EMA200 (warm-up caveat) | 235.72 | −3.27% |
| Daily | EMA10 | 233.80 | −4.05% |
| Daily | Swing Low (Apr 17) | 229.48 | −5.83% |

## Resistance Inventory

| Timeframe | Resistance Type | Price Level | Distance from CMP |
|---|---|---|---|
| 15m | BB Upper Band | 244.22 | +0.22% |
| 30m | BB Upper Band | 245.98 | +0.94% |
| Weekly | Current Week High | 250.39 | +2.75% |
| All TFs | 52-Week High | 255.45 | +4.83% |
| Daily | BB Upper Band | 258.56 | +6.11% |
| Weekly | BB Upper Band (breached) | 240.71 | −1.22% |

## Trade Parameters

- **entry_zone:** ₹242–₹244 (30m/15m EMA cluster); buy consolidation, not chase.
- **stop_zone:** ₹234.00–₹238.81; anchored at 60m EMA50 (237.61), weekly low (236.71), 30m EMA100 (236.37); hard stop sub-234 per daily ATR.
- **first_trouble_area:** ₹240.98 (60m BB LB) — volume breach here signals structure breakdown.
- **swing_target:** ₹255.45 (52W high); extended ₹258–260 (daily BB UB); R:R ~1:2.4.

## Verdict Fields

- **technical_verdict:** Near-Valid
- **stop_survivability_label:** Borderline — 3-level cluster (60m EMA50/weekly low/30m EMA100) supports zone, but daily ATR (3.85%) equals full stop width; one adverse daily bar can breach mechanically.
- **primary_failure_risk:** Daily ATR 9.39 (3.85%) matches stop zone width; weekly price above BB UB adds mean-reversion pressure.
- **ranking_reason:** Rank #2 (Moderately Sponsored); order book + Dangote are real catalysts; 71% Q3 PAT was one-off (Ind AS 115); stop zone thin vs. daily volatility.

## Summary Rationale

Stop zone is borderline-defendable: 60m EMA50 (237.61), weekly low (236.71), and 30m EMA100 (236.37) triple-cluster within 1.24 points at the 3% floor. Critical caveat: daily ATR 9.39 (3.85%) equals full stop zone width — a single adverse day mechanically pierces the stop without any structural signal. Weekly price above BB UB adds mean-reversion pressure.

Daily alignment matters most — Apr 17 breakout (24.9M vol) anchors demand at 229.48; 4-day consolidation without material selling is constructive. Thesis invalidates first on a daily close below 240.98 (60m BB LB) on rising volume, then below 236.37 (structural stop). Intraday bearish momentum (30m/15m RSI sub-50, negative MACDs) is a short-term caution, not a reversal signal.
