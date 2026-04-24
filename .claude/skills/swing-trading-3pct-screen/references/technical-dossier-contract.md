# Technical Dossier Contract

## Purpose

`technical-dossiers/` is a user-facing audit surface for technically reviewed
stocks.

- It exists so the user can inspect how the main agent turned one stock's
  chart review into a final verdict.
- It is not cache-authoritative.
- It must never be reused as an input for future runs, freshness checks, or
  cross-stock ranking.

## Layout

- `docs/swing-trading/YYYY-MM-DD-HHMMSS-utc/technical-dossiers/`
- one markdown file per technically reviewed stock
- filename `<RANK>-<SYMBOL>.md`

`RANK` must be the stock's full-universe fundamental rank, left-padded to the
width of the analyzed universe size.

Example:

- universe size `25` -> `01-ACUTAAS.md`
- universe size `132` -> `001-ACUTAAS.md`

## Write Timing

- after one accepted technical worker result returns, the main agent must write
  that stock dossier immediately
- the main agent must write the dossier before dispatching the next technical
  worker or moving TradingView to another symbol
- if the dossier write fails, stop with a clear exception
- do not create placeholder dossier files for pending or unreviewed stocks

## Canonical Sections

Every technical dossier must use these sections in this exact order:

1. title line with company and symbol
2. generated metadata line with analysis date, fundamental rank, and coverage
   mode
3. `Core Fields`
4. `Timeframe Notes`
5. `Support Inventory`
6. `Resistance Inventory`
7. `Trade Parameters`
8. `Verdict Fields`
9. `Summary Rationale`

## Section Requirements

### Core Fields

Include:

- `symbol`
- `technical_data_mode`
- `cmp`
- `3pct_floor`
- `practical_stop_zone`

### Timeframe Notes

Include one subsection for each:

- `weekly_note`
- `daily_note`
- `60_note`
- `30_note`
- `15_note`

The `30_note` section must be the most detailed because it is the primary
execution frame.

Every timeframe note must explicitly cover:

- market structure
- chart patterns
- volume analysis
- EMA context
- support and resistance context
- supply and demand context

If the dossier was produced in `api_fallback` mode, each timeframe note must
name the API evidence used and explicitly state any indicator limitation
accepted by the main agent. Unsupported required timeframes must fail before
dossier writing.

### Support Inventory

Render the worker's support evidence as a table that shows:

- timeframe
- support type
- price level
- distance from `CMP`

### Resistance Inventory

Render the worker's resistance evidence as a table that shows:

- timeframe
- resistance type
- price level
- distance from `CMP`

### Trade Parameters

Include these four labeled blocks with both level and reasoning:

- `entry_zone`
- `stop_zone`
- `first_trouble_area`
- `swing_target`

### Verdict Fields

Include:

- `technical_verdict`
- `stop_survivability_label`
- `primary_failure_risk`
- `ranking_reason`

### Summary Rationale

End with a verbose synthesis that explains:

- why the stop zone is defendable or fragile
- which timeframe alignment matters most
- what would invalidate the thesis first
- how market structure, chart patterns, and volume evidence support or weaken
  the final verdict

## Main-Agent Acceptance

- `accepted`: the dossier follows the canonical section order, preserves the
  one-stock worker evidence, and makes the verdict auditable to the user
- `redo`: the dossier is missing required sections, too shallow to audit, or
  does not match the reviewed stock
