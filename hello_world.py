#!/usr/bin/env python3
"""Minimal hello world, used to verify the GitHub MCP server write path."""


def hello(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
