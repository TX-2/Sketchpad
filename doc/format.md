# Listing Format

The conventions we use to represent this listing were created by Jurij
Smakov.

The TX-2 computer pre-dated ASCII and source code for its assembler
makes use of symbols which are not even present in Unicode.  Therefore
Jurij Smakov invented a markup format to represent listings.

Characters which exist in ASCII are used as ASCII.  Other characters
are represented by a mark-up string such as `@gamma@` (representing the
Greek letter γ). Subscript and superscript are indicated with a "sub_"
or "super_" prefix: `@sub_gamma@` for ᵧ and `@sup_gamma@` for ᵞ.
Similarly for other superscript characters (such as `@sup_alpha` for
which there is no character in Unicode).

## Rendering and Assembling the Source

The script `sub.py` can be used to convert a markup file into HTML.

The [TX-2 Project's
assembler](https://github.com/TX-2/TX-2-simulator/tree/main/assembler)
accepts the same input format.  There are markup symbols which the
assembler understands but which are missing from `sub.py` because
Sketchpad happens not to use them.

## Macros

Sketchpad and other TX-2 programs make quite extensive use of
macros. See [Macros](macros.md) for some notes on defining and using
macros.

The conventions we use to represent this listing were created by Jurij
Smakov.
