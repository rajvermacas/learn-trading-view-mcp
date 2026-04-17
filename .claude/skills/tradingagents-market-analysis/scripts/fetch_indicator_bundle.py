#!/usr/bin/env python3
"""CLI wrapper for fetching multiple indicator series."""

import argparse

from common import configure_logging, require_text, write_json
from market_data_lib import fetch_indicator_payload


def main() -> None:
    """Parse arguments and print a bundle of indicator payloads."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Fetch multiple indicator series as JSON.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--current-date", required=True)
    parser.add_argument("--look-back-days", required=True)
    parser.add_argument("--indicators", nargs="+", required=True)
    args = parser.parse_args()
    ticker = require_text(args.ticker, "ticker")
    indicators = [
        fetch_indicator_payload(
            ticker,
            indicator_name,
            args.current_date,
            args.look_back_days,
        )
        for indicator_name in args.indicators
    ]
    write_json(
        {
            "ticker": ticker,
            "current_date": args.current_date,
            "look_back_days": int(args.look_back_days),
            "indicators": indicators,
        }
    )


if __name__ == "__main__":
    main()
