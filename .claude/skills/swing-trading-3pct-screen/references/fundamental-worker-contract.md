# Fundamental Worker Contract

## Goal

Determine whether the stock's current momentum is credibly sponsored by recent business evidence and worthy of a strong for a `1-8` week swing.

The worker owns exactly one stock. If the handoff contains multiple stocks, a batch, or a tranche, reject it and require a one-stock redo.
The worker analyzes only the stock it was given.  

## Context Required From Main Agent

- symbol
- company
- screen title
- visible filters
- screen thesis
- why the stock is in this universe
- phase: `fundamental-ranking`
- coverage mode
- whether this is a first-time analysis or a refresh
- prior analysis date and cached dossier path when this is a refresh

## Required Investigation

- recent trigger
- operating evidence
- earnings quality read
- balance-sheet comfort
- catalyst status
- evidence-to-price alignment
- event-risk modifier

## News Rule

Use news only when needed to resolve contradiction, validate a catalyst, or assess near-term event risk.

## Output Requirement

Return one canonical stock dossier candidate using the exact structure from `fundamental-dossier-contract.md`.

## Output Schema

- `Ranking Packet`
- `Sponsorship Reasoning`

The dossier must be complete enough that the main agent can compare it against other stocks without asking the worker for follow-up clarification.
It must cover one stock only.
