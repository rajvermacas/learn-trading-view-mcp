# Swing Trading Screen — 2026-04-19

## Run Details

| Field | Value |
|---|---|
| Run Date | 2026-04-19 |
| Run Time (UTC) | 00:38:07 |
| Screen URL | https://www.screener.in/screens/3474384/return-over-3-months/?page=1 |
| Pages Fetched | Page 1 only (user instruction) |
| Screen Title | Return over 3 months |

## Screen Thesis

Surface mid-to-large cap stocks where 3-month price momentum exceeds 30% and market cap exceeds ₹3,000 Cr, where the momentum is credibly backed by recent business evidence and identifiable company-specific catalysts. The screen primarily surfaces India capital goods / power infrastructure / transformer sector names riding the country's electricity grid and renewable energy build-out capex cycle.

## Universe and Coverage

| Metric | Count |
|---|---|
| Raw universe (page 1) | 25 stocks |
| Deduplicated universe | 25 stocks |
| Fundamental analysis run | 25 of 25 |
| Cache reused (fresh) | 3 (SHILCTECH, GVT&D, ATLANTAELE — cached 2026-04-18) |
| Fresh analysis (missing) | 22 new dossiers written |
| Technical review run | 5 of 25 (top 5 fundamentally ranked, per user instruction) |
| Technical review pending | 20 stocks (user-limited coverage) |

## Coverage Mode

Full-universe fundamental sponsorship ranking → technical review for top 5 fundamentally ranked names only.

## Fundamental Ranking — Top 5 Preview

| Rank | Symbol | Verdict | Key Differentiator |
|---|---|---|---|
| 1 | SHILCTECH | Strongly Sponsored | Zero debt, OPM 28–33% for 7Q, 29x P/E (lowest in screen) |
| 2 | PREMIERENE | Strongly Sponsored | Triple BSE-filed April catalyst cluster, OPM 12%→33% over 8Q |
| 3 | LLOYDSME | Strongly Sponsored | SEBI-filed 120% iron ore volume growth, 33% OPM 4Q, zero net debt |
| 4 | GVT&D | Strongly Sponsored | Elite business quality, 95x P/E penalizes swing entry |
| 5 | ATLANTAELE | Strongly Sponsored | PGCIL EHV approval April 2026, 50% ROCE, no order yet confirmed |

## Technical Ranking — Top 5 Results

| Rank | Symbol | CMP | Stop Zone | Label | Entry Signal |
|---|---|---|---|---|---|
| 1 | SHILCTECH | ₹4,717 | ₹4,529–4,570 | Best Aligned | Current zone ₹4,690–4,750 |
| 2 | LLOYDSME | ₹1,626 | ₹1,558–1,572 | Best Aligned | Pullback to ₹1,596–1,616 |
| 3 | PREMIERENE | ₹1,048 | ₹1,000–1,006 | Near-Valid | Retracement to ₹1,022–1,035 |
| 4 | GVT&D | ₹4,140 | ₹3,970–4,010 | Near-Valid | Pullback to ₹4,057–4,090 |
| 5 | ATLANTAELE | ₹1,373.5 | ₹1,335 | Near-Valid | Pullback to ₹1,350–1,365 |

## Combined Top 3 (Selected)

| # | Symbol | Fundamental | Technical | Status |
|---|---|---|---|---|
| 1 | SHILCTECH | #1 | Best Aligned | **Selected** |
| 2 | LLOYDSME | #3 | Best Aligned | **Selected** |
| 3 | PREMIERENE | #2 | Near-Valid | **Watchlist** — enter on retracement to ₹1,022–1,035 |

## Output Files

| File | Description |
|---|---|
| `3pct-selected-and-watchlist.md` | Full trade-level writeups for selected and watchlist names with levels |
| `3pct-rejected.md` | Rejection summaries for all other names (20 pending technical, 0 hard rejected in top 5) |
| `screen-universe.md` | Full raw universe proof with deduplication and pagination status |
| `3pct-ranked-by-stop-safety.md` | Three-section master ranking: Fundamentally Strongest Top 10, Technically Strongest Top 5 (reviewed), Overall Combined Ranking (25 stocks). Every row shows technical review status. |
