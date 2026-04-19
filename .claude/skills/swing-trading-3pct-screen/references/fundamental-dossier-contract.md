# Fundamental Dossier Contract

## Canonical Shape

Every cached dossier and every fresh worker result must use two sections in this exact order:

1. `Ranking Packet`
2. `Sponsorship Reasoning`

The main agent must write refreshed stock dossiers in this exact canonical shape.

## Ranking Packet

The top section is the normalized comparison interface. It must include:

- `Symbol`
- `Company`
- `Analysis Date`
- `Screen Thesis Fit`
- `Sponsorship Verdict`
- `Confidence`

### Comparison Dimensions

Include a judgment and a reason for each:

- `Recent Trigger`
- `Operating Evidence`
- `Earnings Quality`
- `Balance Sheet Comfort`
- `Catalyst Credibility`
- `Evidence-to-Price Alignment`
- `Near-Term Fragility`

### Ranking Summary

- `Why It Ranks Here`
- `What Keeps It From Ranking Higher`
- `What Kind Of Peer Should Rank Above It`
- `What Kind Of Peer Should Rank Below It`

### Refresh Timing

- `Next Review On`
- `Hard Stale On`

## Sponsorship Reasoning

The bottom section is the verbose audit record. It must include:

- `Why Sponsorship Is Present Or Not`
- `Recent Trigger And What Likely Drove The Move`
- `Business And Financial Evidence`
- `Catalyst Context`
- `Why The Rally Looks Legit Or Fragile For 1-8 Weeks`
- `Contradictions, Weaknesses, And Open Risks`
- `Peer Placement Notes`

## Main-Agent Acceptance

- `accepted`: output follows the canonical structure, covers required dimensions, and is usable for peer ranking
- `redo`: output is malformed, contradictory, too shallow, wrong-stock, or otherwise unusable

No third state is allowed.
