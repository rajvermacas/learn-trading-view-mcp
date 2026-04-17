#!/usr/bin/env python3
"""Markdown report helpers for the standalone skill."""

from __future__ import annotations

import json
from pathlib import Path


def load_json_file(path_raw: str, field_name: str) -> dict:
    """Load a required JSON file."""
    if not path_raw:
        raise ValueError(f"{field_name} is required")
    path = Path(path_raw)
    if not path.exists():
        raise FileNotFoundError(f"{field_name} file does not exist: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build_report_path(ticker: str, report_date: str) -> Path:
    """Build the docs path for a generated market report."""
    sanitized_ticker = ticker.replace("/", "-").replace(".", "_")
    return Path("docs") / "market-analysis" / f"{sanitized_ticker}-{report_date}.md"


def write_report_file(report_path: Path, report_content: str) -> Path:
    """Write a markdown report to disk."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content, encoding="utf-8")
    return report_path


def render_market_report(
    ticker: str,
    stock_data: dict,
    indicators: dict,
    fundamentals: dict,
    company_news: dict,
    global_news: dict,
) -> str:
    """Render a deterministic markdown draft from normalized inputs."""
    indicator_names = extract_indicator_names(indicators)
    return "\n".join(
        [
            f"## Market Analysis Report: {ticker}",
            "",
            "### Executive Summary",
            "_Codex should replace this with the final synthesized takeaway._",
            "",
            "### Technical Analysis",
            f"- Price history records: {stock_data['record_count']}",
            f"- Indicators included: {', '.join(sorted(indicator_names))}",
            "",
            "### Fundamental Analysis",
            f"- Summary metrics collected: {len(fundamentals['company_summary'])}",
            f"- Balance-sheet rows: {len(fundamentals['balance_sheet'])}",
            f"- Cashflow rows: {len(fundamentals['cashflow'])}",
            f"- Income-statement rows: {len(fundamentals['income_statement'])}",
            "",
            "### News And Sentiment",
            f"- Company-news articles: {len(company_news['articles'])}",
            f"- Global-news articles: {len(global_news['articles'])}",
            "",
            "### Key Metrics Table",
            "| Category | Value |",
            "|---|---|",
            f"| Price records | {stock_data['record_count']} |",
            f"| Indicators | {len(indicator_names)} |",
            f"| Summary metrics | {len(fundamentals['company_summary'])} |",
            f"| Company-news articles | {len(company_news['articles'])} |",
            f"| Global-news articles | {len(global_news['articles'])} |",
            "",
            "### Recommendation",
            "_Codex should fill in action, confidence, and risk framing here._",
        ]
    )


def extract_indicator_names(indicators: dict) -> list[str]:
    """Validate and extract indicator names from a bundle payload."""
    items = indicators.get("indicators")
    if not isinstance(items, list) or not items:
        raise ValueError("indicators payload must contain a non-empty 'indicators' list")
    names = [item.get("indicator") for item in items if isinstance(item, dict)]
    if any(name is None for name in names):
        raise ValueError("every indicator payload in the bundle must contain an 'indicator' field")
    return names
