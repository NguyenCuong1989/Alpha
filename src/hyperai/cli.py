"""Command-line interface for the HyperAI framework."""

from __future__ import annotations

import argparse
from typing import Iterable, Optional

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="hyperai",
        description="HyperAI framework command-line interface.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the HyperAI framework version and exit.",
    )
    return parser


def main(argv: Optional[Iterable[str]] = None) -> int:
    """Run the HyperAI CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(f"hyperai {__version__}")
        return 0

    print("HyperAI framework is installed. Use --version for version info.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
