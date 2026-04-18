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
- What the worker should notice: ownership is malformed because one technical worker must own exactly one stock and TradingView work must stay sequential.
- Correct verdict: reject the handoff and request a one-stock redo.
- Why: shared-state chart work becomes ambiguous and error-prone when one worker owns more than one symbol.
