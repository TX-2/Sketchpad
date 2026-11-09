# Sketchpad Reconstruction

## Objective

Produce a complete plain-text TX-2 M4 assembly listing for Ivan
Sutherland's Sketchpad.  The listing must assemble with a documented
cross-assembler and reproduce the printed octal words where those words
survive.  A readable C translation is a later deliverable.

## Preserved Baselines

| Material | Upstream commit | Local marker |
| --- | --- | --- |
| TX-2/Sketchpad | `1263829ba8561d03b5c364bf7e339e5dd2d400ed` | `upstream-baseline-2026-09-14` |
| TX-2/TX-2-simulator | `8757845b8aeb1777c73ee2b9ad2885dd66e26288` | `sketchpad-reconstruction-baseline-2026-09-14` |
| CHM Historical Highlights Documents Repository | `31425aaad4268b6b225409b1e1b21c5c8076a0a6` | Pinned source URLs in `sources/README.md` |
| TX-2 Users Handbook, November 1963 | Internet Archive item `tx-2-users-handbook-nov-63` | SHA-256 in `sources/SHA256SUMS` |

The reconstruction branch starts at the unmodified Sketchpad baseline.
The simulator remains in a separate sibling checkout.  Changes to the
simulator must use their own branch and commits.

## Toolchain Baseline

- Host: macOS 15.7.3 on x86_64.
- Cargo: 1.98.1 (`797e8a9bc`, 2026-08-05).
- Rust: 1.98.1 (`48a229cea`, 2026-09-01).
- Simulator workspace build: successful.

Build the simulator:

```sh
cd TX-2-simulator
cargo build --workspace
```

Run the Sketchpad assembly check:

```sh
cd TX-2-simulator/sources/Sketchpad
./scripts/assemble.sh
```

## Unmodified Assembly Baseline

At the time Graham Goudeau began the reconstruction work, the
assembler failed at line 451 of sk.tx2as, but that problem with the
Sketchpad source was recently solved (in commit
119d62507ba18d63c043b86c253f985dce73599f), so now assembly fails for a
different reason, at line 656.

```text
error in user program: line 656, column 33: found '(error: '@circled_v@' is not a recognised glyph name)
```

The @circled_v@ symbol should probably be @circle@@or@, the
exclusive-or operation (see section 6-2.7 "WORD ASSEMBLY" of the TX-2
Users Handbook.  However, the assembler does not yet support this
operation.

## Current Assembly Frontier

Graham Goudeau's mechanical repairs R001-R004 moved the first
diagnostic to line 657 in the version of the code he was working with.
However those problems had already been fixed upstream.

Hence the current failure point is still as described under
"Unmodified Assembly Baseline".

## Evidence Order

Use the strongest available evidence first:

1. Printed octal output beside the original source line.
2. A second occurrence in either surviving Sketchpad listing.
3. M4 syntax and TX-2 instruction encoding.
4. Local symbol, macro, control-flow, and data-flow constraints.
5. Behavior described in Sutherland's thesis and related primary records.
6. A semantic reconstruction with no direct textual witness.

## Change Classes

Every source change must have one class in the Git commit message and in
the reconstruction log.

- `mechanical`: The change preserves known source meaning and only changes
  representation or assembler compatibility.
- `verified`: Printed octal output or another primary copy proves the
  reconstructed text.
- `inferred`: Program constraints select one reading, but no direct copy
  proves it.
- `speculative`: More than one reading remains plausible.

Do not place speculative text in the canonical assembly file unless the
file marks it clearly and the log records the alternatives.

## Reconstruction Log

| ID | File and location | Class | Evidence | Result |
| --- | --- | --- | --- | --- |
| R000 | `sk.tx2as:451` | baseline | Assembler diagnostic and upstream limitation documentation (but this is out-of-date, as mentioned above) | Compound macro glyph blocks parsing. |
| R002 | `sk.tx2as:453-461`, `2988`, and `3054` | mechanical | Printed logical-AND glyph; Users Handbook section 6-4.5; assembler glyph table (but this is out-of-date, as mentioned above)| Markup `@and@` replaces the unsupported ASCII caret transcription marker. |
| R003 | `sk.tx2as:484` | verified | Later `GORR` copies at `sk.tx2as:3112` and `sk2.tx2as:691,3809` (but this is out-of-date, as mentioned above) | Explicit zero preserves the printed blank address and satisfies the parser. |
| R004 | `sk.tx2as:492-504` | mechanical | The source invokes `ERROR1` only after both definitions; validator uses one-pass macro lookup | Obsolete since the assembler now supports calling macros before they are defined. |
| R005 | `sk.tx2as:657,678,696,718,3189,4157,4178,4196,4218` | mechanical | Printed compound XOR glyph; Users Handbook section 6-2.7 | Markup `@xor@` replaces the unsupported compound-glyph name `@circled_v@`. |

## Publication Gate

The upstream Sketchpad repository has no license file.  The Computer
History Museum also limits reuse of its scans.  Confirm publication rights
before a public fork or release.  Keep downloaded scans outside Git.
