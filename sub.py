#!/usr/bin/python3

import argparse
import functools
import re


SUBS = {
    # Greek letters.
    "@sub_beta@": ("ᵦ", "<sub>&beta;</sub>"),
    "@sub_gamma@": ("ᵧ", "<sub>&gamma;</sub>"),
    "@alpha@": ("α", "&alpha;"),
    "@beta@": ("β", "&beta;"),
    "@gamma@": ("γ", "&gamma;"),
    "@delta@": ("Δ", "&Delta;"),
    "@eps@": ("ε", "&epsilon;"),
    "@lambda@": ("λ", "&lambda;"),
    # Greek letters without subscript in Unicode, using Latin instead.
    "@sub_alpha@": ("ₐ", "<sub>&alpha;</sub>"),
    "@sub_eps@": ("ₑ", "<sub>&epsilon;</sub>"),
    # No subscript lambda, using chi.
    "@sub_lambda@": ("ᵪ", "<sub>&lambda;</sub>"),
    # No subscript delta, using rho.
    "@sub_delta@": ("ᵨ", "<sub>&Delta;</sub>"),
    # No capital letter subscripts, using lowercase.
    "@sub_S@": ("ₛ", "<sub>S</sub>"),
    "@sub_T@": ("ₜ", "<sub>T</sub>"),
    "@sub_M@": ("ₘ", "<sub>M</sub>"),
    "@sub_E@": ("ₑ", "<sub>E</sub>"),
    "@sub_A@": ("ₐ", "<sub>A</sub>"),
    "@sub_I@": ("ᵢ", "<sub>I</sub>"),
    "@sub_X@": ("ₓ", "<sub>X</sub>"),
    "@sub_R@": ("ᵣ", "<sub>R</sub>"),
    "@sub_K@": ("ₖ", "<sub>K</sub>"),
    # Neither capital nor lowercase subscript c, using what's left.
    "@sub_C@": ("ᵩ", "<sub>C</sub>"),
    # These are transcription problems, where char is unclear.
    # Replacing them with ? to be able to verify that all @..@
    # tokens have been converted.
    "@sub_?@": ("?", "<sub>?</sub>"),
    "@sup_?@": ("?", "<sup>?</sup>"),
    "@?@": ("?", "?"),
    # No subscript dot, using regular one.
    # TODO: fix this, it will confuse the parser.
    "@sub_dot@": (".", "<sub>.</sub>"),
    # Subscript and superscript numbers.
    "@sub_0@": ("₀", "<sub>0</sub>"),
    "@sub_1@": ("₁", "<sub>1</sub>"),
    "@sub_2@": ("₂", "<sub>2</sub>"),
    "@sub_3@": ("₃", "<sub>3</sub>"),
    "@sub_4@": ("₄", "<sub>4</sub>"),
    "@sub_5@": ("₅", "<sub>5</sub>"),
    "@sub_6@": ("₆", "<sub>6</sub>"),
    "@sub_7@": ("₇", "<sub>7</sub>"),
    "@sub_8@": ("₈", "<sub>8</sub>"),
    "@sub_9@": ("₉", "<sub>9</sub>"),
    "@sup_0@": ("⁰", "<sup>0</sup>"),
    "@sup_1@": ("¹", "<sup>1</sup>"),
    "@sup_2@": ("²", "<sup>2</sup>"),
    "@sup_3@": ("³", "<sup>3</sup>"),
    "@sup_4@": ("⁴", "<sup>4</sup>"),
    "@sup_5@": ("⁵", "<sup>5</sup>"),
    "@sup_6@": ("⁶", "<sup>6</sup>"),
    "@sup_7@": ("⁷", "<sup>7</sup>"),
    "@sup_8@": ("⁸", "<sup>8</sup>"),
    "@sup_9@": ("⁹", "<sup>9</sup>"),
    # Special symbols.
    "@hamb@": ("☰", "&equiv;"),
    "@times@": ("×", "&times;"),
    "@arr@": ("→", "&rarr;"),
    "@sup_minus@": ("⁻", "<sup>-</sup>"),
    "@hand@": ("☛", "&#9755;"),
    "@sub_pipe@": ("╷", "<sub>|</sub>"),
    # Rectangle with a horizontal dash, using something similar.
    "@rect_dash@": ("▣ ", "&#9635;"),
    "@circled_v@": ("Ⓥ", "&#9419;"),
    "@sup@": ("⊃", "&sup;"),
}


class Sub:
    """Implements common function to substitute tokens."""

    # Substitution table, subclasses should override.
    SUB_TABLE = {}

    TOKEN_RE = re.compile("(@[a-zA-Z0-9_?]+@)")

    def SubLine(self, line):
        """Returns a line with @..@ tokens substituted."""
        matches = self.TOKEN_RE.findall(line)
        for match in matches:
            if match not in self.SUB_TABLE:
                raise ValueError(f"Unknown substitution token: {match}")
            line = line.replace(match, self.SUB_TABLE[match])
        if "@" in line:
            raise ValueError(f'Substitution failed for line: "{line}"')
        return line


class TextGenerator(Sub):
    """Generates text listing by substituting tokens."""

    SUB_TABLE = {key: val[0] for key, val in SUBS.items()}

    def __init__(self, file_name):
        self.file_name = file_name

    def Generate(self):
        for line in open(self.file_name):
            line = line.rstrip()
            print(self.SubLine(line))


class HTMLGenerator(Sub):
    """Generates HTML listing by substituting tokens.

    Produces a listing with all code in one HTML page.
    """

    SUB_TABLE = {key: val[1] for key, val in SUBS.items()}

    def __init__(self, file_name):
        self.file_name = file_name

    def Generate(self):
        print("<html><body style='font-size:150%'><pre><code>")
        for line in open(self.file_name):
            line = line.rstrip()
            if "[meta" in line:
                # Page break.
                print("<hr>")
                continue
            print(self.SubLine(line))
        print("</code></pre></body></html>")


def main(file_name, format_arg):
    if format_arg == "text":
        gen = TextGenerator(file_name)
    elif format_arg == "html":
        gen = HTMLGenerator(file_name)
    else:
        raise ValueError(f"Unsupported output format: {format_arg}")

    gen.Generate()


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

HTMLGenerator("sk.tx2as").Generate()
