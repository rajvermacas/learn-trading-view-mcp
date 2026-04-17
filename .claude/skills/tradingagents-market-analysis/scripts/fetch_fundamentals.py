#!/usr/bin/env python3
"""CLI wrapper for fundamentals retrieval."""

import argparse

from common import configure_logging, require_text, write_json
from fundamentals_lib import fetch_fundamentals_payload


def main() -> None:
    """Parse arguments and print fundamentals JSON."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Fetch company fundamentals as JSON.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--current-date", required=True)
    args = parser.parse_args()
    payload = fetch_fundamentals_payload(
        require_text(args.ticker, "ticker"),
        args.current_date,
    )
    write_json(payload)


if __name__ == "__main__":
    main()
