# RSI 50 Crossover + 20 EMA Strategy — Design Spec

**Date:** 2026-04-11
**File:** `pinescript/rsi50_ema20_strategy.pine`

---

## Overview

A Pine Script v6 strategy that enters a long position when RSI crosses above 50 while the price is already above the 20 EMA, and exits when the price closes below the 20 EMA. No stop loss or take profit — the exit is purely price-based.

---

## Inputs

| Input | Type | Default | Description |
|---|---|---|---|
| `emaLength` | int | 20 | Period for the EMA |
| `rsiLength` | int | 14 | Period for RSI |
| `rsiSource` | source | `close` | Price source for RSI calculation |

---

## Indicators

- `ema20 = ta.ema(close, emaLength)`
- `rsiValue = ta.rsi(rsiSource, rsiLength)`

---

## Entry Condition

```pinescript
ta.crossover(rsiValue, 50) and close > ema20 and strategy.position_size == 0
```

- RSI must cross **above** 50 on this exact bar (not already above)
- Price must be **above** the EMA at bar close
- No existing open position

---

## Exit Condition

```pinescript
strategy.position_size > 0 and close < ema20
```

- Exits entire position when candle closes below the EMA
- No stop loss, no take profit

---

## Strategy Settings

Consistent with existing strategies in the project:

| Setting | Value |
|---|---|
| `overlay` | `true` |
| `pyramiding` | `0` |
| `initial_capital` | `100000` |
| `default_qty_type` | `strategy.percent_of_equity` |
| `default_qty_value` | `100` |
| `commission_type` | `strategy.commission.percent` |
| `commission_value` | `0.0` |

---

## Chart Plots

- EMA line: orange, linewidth 2 (consistent with `ema20_close_strategy.pine`)
- RSI is not plotted (separate pane when added as indicator)

---

## File Conventions

- Follows existing naming: `pinescript/<descriptor>_strategy.pine`
- Pine Script version: v6
