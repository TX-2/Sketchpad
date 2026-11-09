#!/usr/bin/python3

# Formatted with: black -l 80 sub.py
# https://black.readthedocs.io/en/stable/

import argparse
import functools
import sys


def main(file_name, format_arg):
    try:
        from scripts import render
    except ModuleNotFoundError as e:
        e.add_note("Unable to import the render.py module, which should be in the same git repository as this program (sub.py).")
        raise

    if format_arg == "text":
        gen = render.TextGenerator(file_name)
    elif format_arg == "html":
        gen = render.HTMLGenerator(file_name)
    else:
        raise ValueError(f"Unsupported output format: {format_arg}")

    for line in gen.Generate():
        print(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="sub.py",
        description="Generate program listing by substituting tokens.",
    )
    parser.add_argument("file_name", help="Input file name.")
    parser.add_argument(
        "-f",
        "--format",
        choices=["text", "html"],
        help="Output format.",
        default="text",
    )
    args = parser.parse_args()
    main(args.file_name, args.format)
