#!/usr/bin/env python3
"""CLI wrapper for deterministic markdown report generation."""

import argparse

from common import LOGGER, configure_logging, require_text
from report_lib import (
    build_report_path,
    load_json_file,
    render_market_report,
    write_report_file,
)


def main() -> None:
    """Parse arguments, write the markdown report, and print its path."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Generate a markdown market-report draft.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--report-date", required=True)
    parser.add_argument("--stock-data", required=True)
    parser.add_argument("--indicators", required=True)
    parser.add_argument("--fundamentals", required=True)
    parser.add_argument("--company-news", required=True)
    parser.add_argument("--global-news", required=True)
    args = parser.parse_args()
    report = render_market_report(
        require_text(args.ticker, "ticker"),
        load_json_file(args.stock_data, "stock_data"),
        load_json_file(args.indicators, "indicators"),
        load_json_file(args.fundamentals, "fundamentals"),
        load_json_file(args.company_news, "company_news"),
        load_json_file(args.global_news, "global_news"),
    )
    report_path = build_report_path(
        require_text(args.ticker, "ticker"),
        args.report_date,
    )
    write_report_file(report_path, report)
    LOGGER.info("Wrote market report to %s", report_path)
    print(report_path)


if __name__ == "__main__":
    main()
