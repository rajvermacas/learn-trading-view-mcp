#!/usr/bin/env python3
"""CLI wrapper for company-news retrieval."""

import argparse

from common import configure_logging, require_text, write_json
from news_lib import fetch_company_news_payload


def main() -> None:
    """Parse arguments and print company-news JSON."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Fetch company news as JSON.")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    args = parser.parse_args()
    payload = fetch_company_news_payload(
        require_text(args.ticker, "ticker"),
        args.start_date,
        args.end_date,
    )
    write_json(payload)


if __name__ == "__main__":
    main()
