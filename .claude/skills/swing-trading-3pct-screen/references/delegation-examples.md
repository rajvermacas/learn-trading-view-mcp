# Delegation Examples

## Fundamental Few-Shots

### Example: Strongly Sponsored

- Input context: screen thesis shows fresh momentum; company page shows recent operating improvement and an identifiable catalyst.
- What the worker noticed: price strength is backed by improving business evidence, not just relative momentum.
- Correct verdict: `Strongly Sponsored`
- Why: the recent trigger, business evidence, and price action line up.
- Output shape: return a full dossier with `Ranking Packet` and `Sponsorship Reasoning`.

### Example: Mixed

- Input context: the stock is in the screen, but operating evidence is uneven and the catalyst is weak or indirect.
- What the worker noticed: the move may be real, but the proof is not clean enough yet.
- Correct verdict: `Mixed`
- Why: the setup is plausible, but sponsorship is not decisive.
- Output shape: keep the ranking packet explicit about what keeps the stock from ranking higher.

### Example: Weakly Sponsored

- Input context: price is active, but the company evidence is stale, contradictory, or too fragile for conviction.
- What the worker noticed: momentum looks disconnected from recent business support.
- Correct verdict: `Weakly Sponsored`
- Why: the stock should not be ranked near the top of the sponsorship list.
- Output shape: explain clearly why stronger peers should outrank this stock.

### Example: News Escalation Needed

- Input context: price strength is obvious, but the quarterly evidence alone does not cleanly explain the move.
- What the worker noticed: the stock may have a real catalyst, but that catalyst cannot be inferred confidently from screen data alone.
- Correct verdict: escalate to targeted news or catalyst validation before finalizing the sponsorship label.
- Why: news is not mandatory for every stock, but it should be used when catalyst clarity changes the ranking outcome.
- Output shape: still return a dossier candidate after the targeted escalation, not a loose note.

### Example: Invalid Batched Fundamental Handoff

- Input context: the main agent sends one worker `SHILCTECH, GVT&D, ATLANTAELE, PREMIERENE, SCHNEIDER`.
- What the worker should notice: ownership is malformed because one fundamental worker must own exactly one stock.
- Correct verdict: reject the handoff and request a one-stock redo.
- Why: batched ownership degrades ranking clarity, cache writes, and acceptance checks.
- Output shape: do not return a multi-stock dossier.

### Example: Immediate Cache Persistence After First Fundamental Result

- Input context: six fundamental workers are inflight and one valid dossier for `SCHNEIDER` returns before the others.
- What the main agent should notice: accepted fundamental outputs are cache-authoritative immediately, not only after the whole batch completes.
- Correct verdict: write `by-symbol/SCHNEIDER.md` and update its `index.md` row before waiting for the remaining five workers.
- Why: eager cache persistence prevents lost work and keeps the authoritative dossier surface current throughout the run.
- Output shape: persist the canonical dossier first, then continue queue orchestration.

### Example: Invalid Fundamental Over-Parallelization

- Input context: the main agent launches `12` or `20` fundamental workers because the universe is large.
- What the main agent should notice: bounded concurrency is violated because the fundamental inflight cap is `6`.
- Correct verdict: stop dispatching, reduce inflight count to at most `6`, and continue only with queue-based replenishment.
- Why: unbounded dispatch makes cache persistence harder to control and breaks the skill contract.
- Output shape: no worker should be told to own more than one stock to compensate.

### Example: Invalid Fundamental Sub-Agent Reuse

- Input context: a fundamental sub-agent finishes `SCHNEIDER`, then the main agent sends the same sub-agent `PREMIERENE`.
- What the main agent should notice: one stock per fundamental sub-agent means one stock for that sub-agent's full lifecycle, not one stock at a time with later reuse.
- Correct verdict: do not reuse that sub-agent; create a new fundamental sub-agent for `PREMIERENE`.
- Why: every fresh fundamental stock analysis must be isolated to its own newly created worker.
- Output shape: one worker, one stock, one dossier, then stop using that worker for fundamentals.

## Technical Few-Shots

### Example: Best Aligned

- Input context: higher timeframes are constructive and lower timeframes show stacked support above the practical stop band.
- What the worker noticed: the structure has defendable support, not just close EMAs.
- Correct verdict: `Best Aligned`
- Why: market structure, support density, and EMA context all agree.

### Example: Near-Valid

- Input context: the broader trend is good and support is visible, but price is still slightly extended from the support stack.
- What the worker noticed: the setup is close, but the current location does not yet justify a confident stop-survivability verdict.
- Correct verdict: `Near-Valid`
- Why: the chart deserves watchlist status, not immediate selection.

### Example: Likely To Break

- Input context: one timeframe looks acceptable, but lower timeframes show an air pocket into the stop zone and weak structural support.
- What the worker noticed: the path into the stop band is too loose to trust.
- Correct verdict: `Likely To Break`
- Why: the stock should rank lower even if one EMA or one timeframe still looks superficially fine.

### Example: Bad EMA-Only Analysis

- Input context: the worker cites only EMA proximity and ignores the actual price structure.
- What the worker noticed: there is no verified support shelf, no demand zone, and no clean retest.
- Correct verdict: invalid analysis
- Why: EMA clustering alone does not prove stop survivability.

### Example: Invalid Batched Technical Handoff

- Input context: the main agent sends one worker `analyze these top 5 charts together`.
- What the worker should notice: ownership is malformed because one technical worker must own exactly one stock; concurrency is controlled by running multiple one-stock workers, not by batching stocks into one worker.
- Correct verdict: reject the handoff and request a one-stock redo.
- Why: one-stock ownership keeps chart interpretation, API evidence, and output schema unambiguous in both TradingView and API fallback modes.

### Example: Immediate Technical Dossier Persistence

- Input context: the technical worker returns a valid one-stock result for `ACUTAAS`, and the next fundamentally ranked stock is ready for chart review.
- What the main agent should notice: the user-facing technical dossier is required output for every reviewed stock, not an optional end-of-run cleanup step.
- Correct verdict: write `technical-dossiers/01-ACUTAAS.md` immediately. In `tradingview_mcp`, do this before moving TradingView to the next symbol; in `api_fallback`, do this before replenishing the bounded parallel worker queue.
- Why: immediate persistence keeps the technical audit trail aligned with each accepted one-stock result and prevents the reviewed reasoning from being lost.
- Output shape: one worker result becomes one main-agent dossier for that same stock before the next technical review starts.

### Example: Invalid Main-Agent Technical Pre-Fetch

- Input context: after selecting `technical_data_mode=tradingview_mcp`, the main agent collects OHLCV bars, EMA study values, screenshots, or batch chart data for all top-ranked names before dispatching technical workers.
- What the main agent should notice: this violates the technical ownership split because the one-stock technical worker must acquire and validate its own chart evidence.
- Correct verdict: stop the pre-fetch plan, discard the main-agent-collected technical evidence, and dispatch one one-stock technical worker with only identity, ranking context, required timeframes/factors, `technical_data_mode`, and verified MCP/EMA setup status.
- Why: keeping data acquisition inside the worker prevents stale shared chart state, batch interpretation drift, and unclear responsibility for technical evidence.
- Output shape: the worker returns one stock's technical output schema; the main agent then writes that stock's dossier immediately.

### Example: Valid TradingView MCP Handoff

- Input context: TradingView MCP and EMA setup are verified, and `LLOYDSME` is fundamental rank `#1`.
- What the main agent should send: one-stock identity, screen thesis, fundamental rank, sponsorship context, coverage mode, `technical_data_mode=tradingview_mcp`, required timeframes, required factors, and confirmation that MCP/EMA preflight passed.
- Correct verdict: the worker navigates/reads TradingView MCP for `LLOYDSME` inside its own task across `weekly`, `daily`, `60`, `30`, and `15`, then returns the output schema.
- Why: the main agent selected the mode and built the handoff, while the worker owns technical evidence collection and interpretation.
- Output shape: no pre-fetched chart packets appear in the handoff.
