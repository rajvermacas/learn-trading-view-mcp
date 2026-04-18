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

## Review-Due Tie Breaker

When more than `3` stocks are `review_due`, choose the refresh selection in this exact order:

1. earlier `Next Review On`
2. earlier `Hard Stale On`
3. lexicographically smaller `Symbol`

## Cache Update Rule

- A fresh accepted analysis overwrites the existing cached dossier for that stock.
- The main agent updates the stock row in `index.md` after writing the refreshed dossier.
- Reused stocks keep their existing cached dossier and existing `index.md` row.
