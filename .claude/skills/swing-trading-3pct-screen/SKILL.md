---
name: swing-trading-3pct-screen
description: Use when screening Indian stocks from a Screener.in HTML universe for swing trades that need full-universe fundamental sponsorship ranking first, then technical review through TradingView MCP or deterministic public-data API mode when TradingView MCP is disconnected.
---

# Swing Trading 3pct Screen

## Purpose

Use this skill for Screener.in HTML universes that need a dynamic screen thesis, a user-capped pre-ranked universe, a full-universe fundamental sponsorship ranking inside that capped set, and then stock-by-stock technical review against a practical `2%` to `4%` downside zone around the usual `3%` reference.

The analysis must not hardcode a specific screen recipe. Extract the screen thesis from the user-provided URL, title, and visible filters on each run.

## Workflow

1. Fetch the user-provided Screener.in URL as HTML across every page.
2. Extract a compact screen thesis from the title, visible filters, and screen intent.
3. Require the user prompt to specify the pre-ranked universe cap. If the cap is missing, stop with a clear exception instead of assuming any number.
4. Build the full stock universe and deduplicate it.
5. Compute `PreRankScore` plus soft penalties from the visible Screener columns defined in [references/methodology.md](references/methodology.md).
6. Sort the full parsed universe by adjusted `PreRankScore` descending and keep only the top user-capped names as the working universe.
7. Read `docs/swing-trading/fundamentals/index.md`.
8. Derive which capped-universe names are runtime `missing`, `fresh`, `review_due`, and `hard_stale`.
9. Build one fundamental refresh queue containing all runtime `missing`, all `hard_stale`, and exactly top `3` `review_due`.
10. Run that fundamental refresh queue with at most `6` inflight fundamental sub-agents at any time, creating one new fundamental sub-agent per stock.
11. As soon as one fundamental sub-agent returns an accepted dossier, immediately overwrite that stock dossier and update its `index.md` row before waiting for any other fundamental result.
12. Reuse cached dossiers for all `fresh` and remaining `review_due`.
13. Build the capped-universe fundamental ranking from authoritative stock dossiers only.
14. Run [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh), then select `technical_data_mode`.
15. Use `technical_data_mode=tradingview_mcp` only after TradingView and the EMA study setup are verified.
16. If TradingView MCP is disconnected or unreachable, use `technical_data_mode=api_fallback` and fetch deterministic technical data with this skill's local API scripts.
17. Dispatch one technical sub-agent per stock only after the ranking exists.
18. Run technical sub-agents strictly one at a time.
19. If the user specifies a technical coverage count such as `analyze 12 stocks`, run technical sub-agents only for the top `12` fundamentally ranked names; otherwise continue through the full capped universe.
20. After each accepted technical result, immediately write one verbose technical dossier for that stock before moving to the next symbol.
21. Write the five-file report set with reviewed versus pending technical status explicit and include the technical dossier directory in the run output.

## Delegation Rules

Every main-agent to sub-agent handoff must include all of the following:

- Goal
- Context
- Few-shot examples
- Output schema

If any of those pieces are missing, the handoff is invalid and must be rejected.

Ownership is always singular:

- one fundamental sub-agent owns exactly one stock
- one technical sub-agent owns exactly one stock
- every stock requiring fresh fundamental analysis must be assigned to a newly created fundamental sub-agent

Fundamental sub-agent reuse is forbidden:

- the same fundamental sub-agent must never be reused for a second stock
- after one fundamental sub-agent returns its one-stock dossier, that sub-agent's fundamental work is finished
- if another stock needs fresh fundamental analysis, the main agent must create a different new fundamental sub-agent for that stock

A handoff that assigns multiple stocks, a tranche, or a batch to one sub-agent is invalid and must be redone.

Responsibility split is strict:

- the main agent compares one stock's fundamentals against another stock's fundamentals
- the main agent assigns sponsorship rank across the universe
- each fundamental sub-agent only analyzes the single stock it is given and returns that stock's dossier

## Cache Rules

- `index.md` is a registry only.
- The main agent must never rank from `index.md`.
- The main agent must treat a reused cached stock dossier as equivalent to a previously accepted fundamental sub-agent response.
- The main agent must write refreshed stock dossiers in the exact canonical markdown structure defined in [references/fundamental-dossier-contract.md](references/fundamental-dossier-contract.md).
- The main agent must persist each accepted fresh fundamental dossier immediately when that worker returns.
- The main agent must update the matching `index.md` row in the same step as the dossier write.
- The main agent must never wait for all fundamental sub-agents to finish before persisting accepted results.
- If an accepted dossier cannot be written immediately, stop with a clear exception instead of deferring that cache update.

## Analysis Rules

- Fundamental analysis comes first for every stock in the fetched universe.
- Before dispatching any fundamental sub-agent, the main agent must pre-rank the parsed Screener universe with `PreRankScore`, apply the defined soft penalties, and reduce the working universe to the user-specified cap.
- The skill must never assume a pre-rank cap such as `15`; the user must provide that number in the prompt.
- If the prompt does not specify a pre-rank cap, stop with a clear exception instead of defaulting to the full universe or any assumed cap.
- Pre-rank must use only the values already present in the Screener HTML table for that run; the main agent must not fetch per-stock values separately for pre-rank.
- If the Screener headers do not contain `Qtr Profit Var %`, `Qtr Sales Var %`, `ROCE %`, and `3mth return %`, stop with a clear exception that names the missing scoring columns.
- `CMP Rs.`, `P/E`, `Mar Cap Rs.Cr.`, `Div Yld %`, `NP Qtr Rs.Cr.`, and `Sales Qtr Rs.Cr.` are context-only screen columns for this skill and must not contribute to `PreRankScore`.
- If an individual stock row has a missing, blank, non-numeric, or distorted pre-rank value, apply the row-level scoring and penalty rules from [references/methodology.md](references/methodology.md) and continue without extra fetches.
- Fundamental sub-agents may be dispatched multiple at a time with bounded concurrency, but each fundamental sub-agent must process exactly one stock.
- No more than `6` fundamental sub-agents may be inflight at once.
- Each fresh fundamental analysis must run in its own newly created fundamental sub-agent.
- A completed fundamental sub-agent must not be given another stock.
- When one inflight fundamental sub-agent finishes, write that accepted dossier to cache immediately and only then dispatch the next queued fundamental stock if work remains.

- Technical sub-agents must run one at a time and only one stock per worker.
- Technical analysis must cover `weekly`, `daily`, `60`, `30`, and `15`.
- Each technical handoff must include `technical_data_mode`.
- In `tradingview_mcp` mode, workers read the shared chart state from TradingView MCP.
- In `api_fallback` mode, the main agent must fetch per-stock JSON before the handoff using:
  - `scripts/fetch_stock_data.py`
  - `scripts/fetch_indicator_bundle.py`
- In `api_fallback` mode, read `references/api-workflow.md`, `references/api-output-schemas.md`, and `references/api-indicators.md`; keep stdout JSON and stderr logs separate.
- In `api_fallback` mode, resolve an exchange-qualified ticker such as `ATLANTAELE.NS`, explicit ISO dates, and explicit look-back days before fetching. If any required input is missing or cannot be resolved, stop with a clear exception.
- In `api_fallback` mode, TradingView is the source-of-truth capability floor: fetch `15m`, `30m`, `60m`, `1d`, and `1wk`, and fetch EMA `10`, `20`, `50`, `100`, and `200` on every interval. API fallback may include more indicators, but not fewer required timeframes or EMAs.
- If API data cannot support one of the required timeframes or EMA periods, or returns empty price history, stop with a clear exception instead of inventing chart evidence.
- If the indicator bundle returns only `null` current values, state that limitation and use OHLCV-derived price structure only; do not fabricate indicator signals.
- Technical review must use EMA context, support and resistance zones, supply and demand zones, chart patterns, and market structure together.
- EMA proximity alone is not a valid decision rule.
- Use the `30` minute chart as the main lower-timeframe execution and support-mapping frame.
- Treat the `3%` reference as contextual, not binary; judge defendability across the practical `2%` to `4%` stop band.
- Every technically reviewed stock must get one verbose main-agent technical dossier written immediately after that stock review completes.
- Technical dossiers are user-facing audit records only and must never be reused as cache input.

## Reporting Rules

Write a fresh timestamped folder under `docs/swing-trading/` with these five files:

- `README.md`
- `3pct-selected-and-watchlist.md`
- `3pct-rejected.md`
- `screen-universe.md`
- `3pct-ranked-by-stop-safety.md`

The report must make technical status explicit:

- reviewed names
- pending technical review names
- technical review not run because of a user-imposed coverage limit
- technical data mode used for each reviewed name
- the full parsed universe size
- the user-specified pre-rank cap
- the names that survived the pre-rank cut into the working universe

Use [references/fundamental-cache-contract.md](references/fundamental-cache-contract.md), [references/fundamental-dossier-contract.md](references/fundamental-dossier-contract.md), [references/fundamental-worker-contract.md](references/fundamental-worker-contract.md), [references/technical-worker-contract.md](references/technical-worker-contract.md), [references/delegation-examples.md](references/delegation-examples.md), and [references/reporting-contract.md](references/reporting-contract.md) for the detailed cache, worker, and report contracts.

Use [references/technical-dossier-contract.md](references/technical-dossier-contract.md) for the verbose technical dossier that the main agent must persist for every technically reviewed stock.

Use [references/methodology.md](references/methodology.md) for ranking logic, filters, and number discipline.
