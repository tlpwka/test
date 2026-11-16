#!/usr/bin/env python3
"""Minimal hello world, used to verify the GitHub MCP server write path."""

import sys


def hello(name: str = "world") -> str:
    return f"Hello, {name}!"


def main(argv=None) -> int:
    args = (sys.argv if argv is None else list(argv))[1:]
    print(hello(" ".join(args) or "world"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
