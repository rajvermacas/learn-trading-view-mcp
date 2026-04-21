# Reporting Contract

# Run Output

Each run output folder must contain:

- `README.md`
- `3pct-selected-and-watchlist.md`
- `3pct-rejected.md`
- `screen-universe.md`
- `3pct-ranked-by-stop-safety.md`
- `technical-dossiers/`

`technical-dossiers/` must contain one verbose markdown dossier for every
technically reviewed stock and no dossier for pending names.

## README.md

- run date and screen URL
- screen thesis
- universe size
- coverage mode
- counts for analyzed, reviewed, selected, watchlist, rejected, and pending names
- count and location of technical dossiers written
- top previews for fundamental, technical, and combined rankings
- a short explanation of the fifth file and its three sections
- a short explanation of the technical dossier directory and how to read it

## 3pct-selected-and-watchlist.md

- only names that deserve full trade-level writeups
- explicit fundamentals, multi-timeframe structure, support inventory, resistance inventory, and trade levels
- one concise verdict block per name
- reference the corresponding technical dossier filename for every reviewed name

## 3pct-rejected.md

- concise, evidence-based rejection summaries
- technical review status must be explicit
- best support found near the stop zone
- why that support was insufficient
- whether the name is a re-check candidate or a hard reject
- user-limited technical coverage must be labeled as `technical review not run in this execution`

## screen-universe.md

- proof of full HTML coverage across all pages
- pagination handling
- deduplication
- normalized raw universe used for analysis
- the fixed visible screen schema used in the run
- the four scoring columns used for `PreRankScore`
- the six context-only visible columns
- adjusted `PreRankScore`
- working-universe inclusion status
- key penalty flags
- key zero-contribution metric flags

## 3pct-ranked-by-stop-safety.md

- `Fundamentally Strongest Top Ten`
- `Technically Strongest Top Ten`
- `Overall Combined Ranking`
- every row must show technical review status
- every row should include a technical label or combined verdict
- every row should include a key reason for the ranking
- reviewed and pending names must be distinguishable
- the third section is the default master ranking for the full universe
