# RSI 50 Crossover + 20 EMA Strategy Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a Pine Script v6 strategy that buys when RSI crosses above 50 with price above 20 EMA, and exits when price closes below 20 EMA.

**Architecture:** Single Pine Script file with configurable inputs for EMA length, RSI length, and RSI source. Entry uses `ta.crossover` for strict RSI 50 crossover detection combined with EMA filter. Exit is purely price-based — no stop loss or take profit.

**Tech Stack:** Pine Script v6, TradingView strategy framework

---

## File Structure

| Action | File | Responsibility |
|---|---|---|
| Create | `pinescript/rsi50_ema20_strategy.pine` | Complete strategy — inputs, indicators, entry/exit logic, chart plot |

---

### Task 1: Write the Pine Script strategy file

**Files:**
- Create: `pinescript/rsi50_ema20_strategy.pine`

- [ ] **Step 1: Create the strategy file**

Create `pinescript/rsi50_ema20_strategy.pine` with the following content:

```pinescript
//@version=6
strategy("RSI 50 Crossover + 20 EMA Strategy", overlay=true, pyramiding=0, initial_capital=100000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.0)

emaLength = input.int(20, "EMA Length", minval=1)
rsiLength = input.int(14, "RSI Length", minval=1)
rsiSource = input.source(close, "RSI Source")

ema20 = ta.ema(close, emaLength)
rsiValue = ta.rsi(rsiSource, rsiLength)

longCondition = ta.crossover(rsiValue, 50) and close > ema20 and strategy.position_size == 0
exitCondition = strategy.position_size > 0 and close < ema20

if longCondition
    strategy.entry("Long", strategy.long)

if exitCondition
    strategy.close("Long")

plot(ema20, title="EMA 20", color=color.orange, linewidth=2)
```

- [ ] **Step 2: Load the strategy into TradingView via MCP**

Use `mcp__tradingview__pine_new` to create a new Pine Script editor with the above source, then `mcp__tradingview__pine_smart_compile` to compile it. Check for errors with `mcp__tradingview__pine_get_errors`.

Expected: No compilation errors.

- [ ] **Step 3: Verify inputs appear in TradingView settings panel**

Use `mcp__tradingview__capture_screenshot` with region `"chart"` to confirm the strategy loads on the chart and the EMA line is visible (orange).

Expected: Strategy applied to chart, EMA plotted, no error messages.

- [ ] **Step 4: Commit**

```bash
git add pinescript/rsi50_ema20_strategy.pine
git commit -m "Add RSI 50 crossover + 20 EMA strategy"
```

---

### Task 2: Verify entry and exit logic via backtest

**Files:**
- Modify: none (visual/backtest verification only)

- [ ] **Step 1: Open Strategy Tester in TradingView**

Use `mcp__tradingview__capture_screenshot` with region `"strategy_tester"` to capture the backtest results panel.

Expected: Strategy tester shows trade list with entries and exits populated (not zero trades).

- [ ] **Step 2: Verify entry bars visually**

Use `mcp__tradingview__chart_get_state` to get current symbol and timeframe. Then use `mcp__tradingview__data_get_trades` to retrieve trade history.

Expected: Each entry corresponds to a bar where RSI crossed above 50 and close was above EMA.

- [ ] **Step 3: Verify exit bars visually**

From `data_get_trades` results, spot-check that exit bars correspond to candles that closed below the EMA.

Expected: No exits triggered by stop loss or take profit — only by EMA close condition.

- [ ] **Step 4: Confirm no open position is carried across entry signals**

Check that trade history shows one trade at a time — no overlapping entries.

Expected: Each entry is followed by an exit before the next entry.
