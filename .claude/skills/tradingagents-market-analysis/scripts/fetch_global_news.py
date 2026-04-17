#!/usr/bin/env python3
"""CLI wrapper for global-news retrieval."""

import argparse

from common import configure_logging, write_json
from news_lib import fetch_global_news_payload


def main() -> None:
    """Parse arguments and print global-news JSON."""
    configure_logging()
    parser = argparse.ArgumentParser(description="Fetch macro and global news as JSON.")
    parser.add_argument("--current-date", required=True)
    parser.add_argument("--look-back-days", required=True)
    parser.add_argument("--limit", required=True)
    args = parser.parse_args()
    payload = fetch_global_news_payload(
        args.current_date,
        args.look_back_days,
        args.limit,
    )
    write_json(payload)


if __name__ == "__main__":
    main()
