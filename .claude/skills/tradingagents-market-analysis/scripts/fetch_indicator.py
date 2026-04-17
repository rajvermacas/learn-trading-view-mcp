#!/usr/bin/env python3
"""CLI wrapper for indicator retrieval."""

import argparse

from common import configure_logging, require_text, write_json
from market_data_lib import fetch_indicator_payload


def main() -> None:
    """Parse arguments and print indicator JSON."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Fetch a single indicator series as JSON.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--indicator", required=True)
    parser.add_argument("--current-date", required=True)
    parser.add_argument("--look-back-days", required=True)
    args = parser.parse_args()
    payload = fetch_indicator_payload(
        require_text(args.ticker, "ticker"),
        args.indicator,
        args.current_date,
        args.look_back_days,
    )
    write_json(payload)


if __name__ == "__main__":
    main()
