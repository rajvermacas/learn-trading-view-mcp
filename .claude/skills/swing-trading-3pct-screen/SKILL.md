---
name: swing-trading-3pct-screen
description: Use when screening Indian stocks from a Screener.in HTML universe for swing trades that must be ranked by full-universe fundamental sponsorship first, then strictly sequential technical review around a practical 2% to 4% stop zone.
---

# Swing Trading 3pct Screen

## Purpose

Use this skill for Screener.in HTML universes that need a dynamic screen thesis, a full-universe fundamental sponsorship ranking, and then stock-by-stock technical review against a practical `2%` to `4%` downside zone around the usual `3%` reference.

The analysis must not hardcode a specific screen recipe. Extract the screen thesis from the user-provided URL, title, and visible filters on each run.

## Workflow

1. Fetch the user-provided Screener.in URL as HTML across every page.
2. Extract a compact screen thesis from the title, visible filters, and screen intent.
3. Build the full stock universe and deduplicate it.
4. Read `docs/swing-trading/fundamentals/index.md`.
5. Derive which current-universe names are runtime `missing`, `fresh`, `review_due`, and `hard_stale`.
6. Dispatch one fundamental sub-agent per stock for all runtime `missing`, all `hard_stale`, and exactly top `3` `review_due`.
7. Reuse cached dossiers for all `fresh` and remaining `review_due`.
8. Build the full-universe fundamental ranking from authoritative stock dossiers only.
9. Run [`scripts/ensure_socat.sh`](scripts/ensure_socat.sh) and verify TradingView plus the EMA study setup before chart work begins.
10. Dispatch one technical sub-agent per stock only after the ranking exists.
11. Run technical sub-agents strictly one at a time because TradingView MCP is shared mutable state.
12. If the user specifies a technical coverage count such as `analyze 12 stocks`, run technical sub-agents only for the top `12` fundamentally ranked names; otherwise continue through the full universe.
13. Overwrite refreshed stock dossiers, update `index.md`, and write the five-file report set with reviewed versus pending technical status explicit.

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

## Analysis Rules

- Fundamental analysis comes first for every stock in the fetched universe.
- Fundamental sub-agents may be dispatched multiple at a time with bounded concurrency, but each fundamental sub-agent must process exactly one stock.

- Technical sub-agents must run one at a time and only one stock per worker.
- Technical analysis must cover `weekly`, `daily`, `60`, `30`, and `15`.
- Technical review must use EMA context, support and resistance zones, supply and demand zones, chart patterns, and market structure together.
- EMA proximity alone is not a valid decision rule.
- Use the `30` minute chart as the main lower-timeframe execution and support-mapping frame.
- Treat the `3%` reference as contextual, not binary; judge defendability across the practical `2%` to `4%` stop band.

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

Use [references/fundamental-cache-contract.md](references/fundamental-cache-contract.md), [references/fundamental-dossier-contract.md](references/fundamental-dossier-contract.md), [references/fundamental-worker-contract.md](references/fundamental-worker-contract.md), [references/technical-worker-contract.md](references/technical-worker-contract.md), [references/delegation-examples.md](references/delegation-examples.md), and [references/reporting-contract.md](references/reporting-contract.md) for the detailed cache, worker, and report contracts.

Use [references/methodology.md](references/methodology.md) for ranking logic, filters, and number discipline.
