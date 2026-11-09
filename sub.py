#!/usr/bin/python3

# Formatted with: black -l 80 sub.py
# https://black.readthedocs.io/en/stable/

import argparse
import functools
import sys

verbose_messages = [None]


def verbose_msg(s):
    if verbose_messages[0] is None:
        raise RuntimeError(
            "you should set verbose_messages to True or False before calling verbose_msg",
        )
    if verbose_messages[0]:
        print(s)


def write_output_if_changed(data, output_file_name):
    byte_count = len(data)
    changed = True
    try:
        with open(output_file_name, "rt") as f:
            existing = f.read()
            changed = (existing != data)
            desc = "different" if changed else "identical"
            verbose_msg(f"The existing and new data for {output_file_name} are {desc}")
    except IOError:
        verbose_msg(f"{output_file_name} does not yet exist")
        changed = True
    if changed:
        with open(output_file_name, "wt") as f:
            f.write(data)
            verbose_msg(f"Wrote {byte_count} bytes to {output_file_name}")
    else:
        verbose_msg(f"There is no need to update {output_file_name}")


def main(input_file_name, format_arg, output_file_name):
    try:
        from scripts import render
    except ModuleNotFoundError as e:
        e.add_note("Unable to import the render.py module, which should be in the same git repository as this program (sub.py).")
        raise

    generated_body = render.render_body(verbose_messages, input_file_name, format_arg)
    # Only write the output if it has changed, so that we do not unnecessarily
    # change the timestamp.
    write_output_if_changed(generated_body, output_file_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="sub.py",
        description="Generate program listing by substituting tokens.",
    )
    parser.add_argument(
        "input",
        help="Input file name.")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output file name.")
    parser.add_argument(
        "-f",
        "--format",
        choices=["text", "html"],
        help="Output format.",
        default="text",
    )
    parser.add_argument('--verbose',
                        action=argparse.BooleanOptionalAction,
                        help="When set, print verbose messages about what is happening.")
    args = parser.parse_args()
    verbose_messages[0] = args.verbose if args.verbose else False
    main(args.input, args.format, args.output)
