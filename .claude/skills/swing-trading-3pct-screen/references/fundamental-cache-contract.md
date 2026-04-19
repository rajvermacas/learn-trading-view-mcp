# Fundamental Cache Contract

## Cache Layout

- `docs/swing-trading/fundamentals/index.md`
- `docs/swing-trading/fundamentals/by-symbol/<SYMBOL>.md`

## Registry Format

`index.md` is a registry only. It must not be used as a ranking surface.

Use one canonical table:

| Symbol | Company | Cache File | Last Analyzed On | Next Review On | Hard Stale On |
|---|---|---|---|---|---|
| NATCOPHARM | Natco Pharma Ltd | by-symbol/NATCOPHARM.md | 2026-04-18 | 2026-04-27 | 2026-05-09 |

## Runtime Derivation

Derive freshness from `index.md` on each run:

- no index row -> runtime `missing`
- `today <= Next Review On` -> `fresh`
- `Next Review On < today <= Hard Stale On` -> `review_due`
- `today > Hard Stale On` -> `hard_stale`

Do not store a derived state column in `index.md`.

## Refresh Rule

Every run must:

- refresh all runtime `missing`
- refresh all `hard_stale`
- refresh exactly top `3` `review_due`

Reuse:

- all `fresh`
- all remaining `review_due`

## Fundamental Queue Rule

- Build one refresh queue from all required refresh names.
- Keep no more than `6` fundamental workers inflight at the same time.
- When one worker finishes, persist that accepted dossier before dispatching another queued refresh.
- Waiting for the full refresh queue to complete before writing accepted dossiers is invalid.

## Review-Due Tie Breaker

When more than `3` stocks are `review_due`, choose the refresh selection in this exact order:

1. earlier `Next Review On`
2. earlier `Hard Stale On`
3. lexicographically smaller `Symbol`

## Cache Update Rule

- A fresh accepted analysis overwrites the existing cached dossier for that stock.
- The main agent writes each accepted dossier immediately when that worker returns.
- The main agent updates the stock row in `index.md` in the same step after writing the refreshed dossier.
- If the write or index update cannot complete immediately, stop with a clear exception.
- Reused stocks keep their existing cached dossier and existing `index.md` row.
