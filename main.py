#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't.

Writes exactly one original weather-forecast line for the invented city
Drizzlewick to /output/entry.txt.
"""

import os


FORECAST = "Drizzlewick: light rain of lost umbrellas, 14°C, with a 90% chance your umbrella joins them."


def main() -> None:
    line = FORECAST
    text = line.strip()
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry must be 1-120 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
