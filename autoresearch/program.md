# AutoResearch: Pine Script Strategy Optimizer

## Objective
Generate Pine Script v6 strategies passing **all 4 criteria**:
1. **Total P&L > 100%**
2. **Max Equity Drawdown < 20%**
3. **Profitable Trades > 60%**
4. **Total Trades > 100**

## Fixed Constraints (Never Change)
- Pine Script v6 (`//@version=6`)
- `strategy(...)` with: `initial_capital=100000`, `default_qty_type=strategy.percent_of_equity`, `default_qty_value=100`, `commission_type=strategy.commission.percent`, `commission_value=0.1`
- Timeframe: 1D

## Current State (12 Iterations, ~65 Strategies)

### Records
- **WR + Trades simultaneously passing**: C12/NIFTY — WR 64.66% ✓, Trades 133 ✓ (FIRST TIME both pass!)
- **Best multi-criteria**: C11/HDFCBANK — P&L 286% ✓, WR 63% ✓, Trades 95, DD 31%
- **Closest to 4/4**: C11/HDFCBANK missing only Trades(5 short) + DD(11% over)

### THE GAP ANALYSIS (HDFCBANK C11 closest)
- Trades: 95 → need 6 more → try NSE:SBIN (volatile banking, more history)
- DD: 31% → need 11% reduction → **consecutive-stop cooldown prevents crash re-entries**

### WHY DD IS 31% ON HDFCBANK
During 2008 crash: StochRSI<15 fires as HDFCBANK is crashing →
  Entry #1 → 8% stop hit → -8% equity
  StochRSI<15 fires again immediately → Entry #2 → 8% stop → -8% equity
  Entry #3 → -8% equity
  3 consecutive stop-outs = 23% equity drawdown from one crash event!
Fix: After 2 consecutive stop-outs, pause entries for 30 bars (1.5 months)

## Iteration 13 Strategies

### A13 — C11 + Consecutive Stop Cooldown (PRIMARY)
```pinescript
// Track consecutive stops
var int stopStreak  = 0
var int lastStopBar = 0

// Reset streak after 30 calm bars
if bar_index - lastStopBar > 30
    stopStreak := 0

// Only enter if we haven't had 2+ consecutive stops recently
safeToEnter = stopStreak < 2

longCondition = smoothK < 15 and kCrossD and bullTrend and safeToEnter and strategy.position_size == 0

// On stop-out: increment streak
stopHit = strategy.position_size > 0 and not na(stopPrice) and close < stopPrice
if stopHit
    stopStreak  := stopStreak + 1
    lastStopBar := bar_index
// On RSI exit: reset streak (good trade = not a crash)
if strategy.position_size > 0 and rsi14 > 60
    stopStreak := 0
```
Test on: NSE:HDFCBANK (95 trades base → with cooldown ~85-90 trades, DD drops to ~18%)

### B13 — Test on NSE:SBIN (volatile banking, likely >100 trades)
Apply C11 strategy (StochRSI<15 + RSI>60 + 8% stop) to SBIN.
SBIN is highly volatile, part of Nifty 50, data likely from ~1995.
Expected: 100-120 trades, WR 60-65%, DD 25-35%, P&L varies.

### C13 — A13 applied to NSE:SBIN (cooldown + SBIN)
Combine cooldown filter with SBIN's higher volatility.
If SBIN has 110+ trades and cooldown blocks 15 crash entries → 95 quality trades + WR 65%+

### D13 — Test NSE:ICICIBANK with StochRSI<15 + 8% stop
ICICIBANK private banking, data from ~1997, very volatile.
Might have different signal characteristics than HDFCBANK.

### E13 — C11 + require RSI14 < 45 at entry (extra quality gate)
Adding RSI14 < 45 to StochRSI<15 entry:
- Trades will reduce (maybe 65-75 but might hit 80+)
- WR might improve to 65-70% (fewer borderline entries)
- If HDFCBANK with this gives 80+ trades and 65%+ WR, DD may be lower

## Graveyard (All Confirmed Dead)
- ATR dynamic stop (fires during elevated-volatility oversold = kills WR)
- StochRSI threshold 17-20 (kills WR from 62% to 48%)
- NIFTY index (avg win only 2.55% per trade after StochRSI signal)
- NIFTY regime filter (removes profitable early-bull entries)
- Fixed target+stop combinations (WR 34-49%)
- All oscillators except StochRSI<15: CCI, Williams%R, Classic Stochastic
- 1H timeframe, Weekly timeframe, Annual RSI
- EMA touch/reclaim strategies

## Hall of Fame
*Still empty. C11/HDFCBANK closest: P&L 286% ✓, WR 63% ✓, Trades 95 (5 short), DD 31% (11% over)*

## Iteration History
- **Iter 1-9**: Trade count bottleneck. RSI<40 gives 68-88% WR but only 33-59 trades.
- **Iter 10**: StochRSI<15 breakthrough — WR 65.48%!
- **Iter 11**: C11 validated — consistent WR 61-69% on RELIANCE/TCS/HDFCBANK.
- **Iter 12**: NIFTY gives 133 trades + 64.66% WR simultaneously. HDFCBANK closest.
- **Iter 13 target**: Stop cooldown (fixes DD) + SBIN (fixes trade count)

## Pine Script Template (C11 Base)
```pinescript
//@version=6
strategy(title="[NAME]", overlay=true, initial_capital=100000,
         default_qty_type=strategy.percent_of_equity, default_qty_value=100,
         commission_type=strategy.commission.percent, commission_value=0.1)

ema200   = ta.ema(close, 200)
rsi14    = ta.rsi(close, 14)
stochRSI = ta.stoch(rsi14, rsi14, rsi14, 14)
smoothK  = ta.sma(stochRSI, 3)
smoothD  = ta.sma(smoothK, 3)
kCrossD  = ta.crossover(smoothK, smoothD)
bullTrend = close > ema200

longCondition = smoothK < 15 and kCrossD and bullTrend and strategy.position_size == 0
var float stopPrice = na
if longCondition: stopPrice := close * 0.92
exitCondition = strategy.position_size > 0 and (rsi14 > 60 or (not na(stopPrice) and close < stopPrice))
```
