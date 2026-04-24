#!/usr/bin/env python3
"""CLI wrapper for stock-history retrieval."""

import argparse

from common import configure_logging, require_text, write_json
from market_data_lib import fetch_stock_history_payload


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""
    parser = argparse.ArgumentParser(description="Fetch stock history as JSON.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--interval", required=True)
    return parser


def main() -> None:
    """Parse arguments and print stock-history JSON."""
    configure_logging()
    parser = build_parser()
    args = parser.parse_args()
    payload = fetch_stock_history_payload(
        require_text(args.ticker, "ticker"),
        args.start_date,
        args.end_date,
        args.interval,
    )
    write_json(payload)


if __name__ == "__main__":
    main()
