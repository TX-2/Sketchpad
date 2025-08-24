# Assembling the Sketchpad Code

## The "tx2m4as" Cross-Assembler

We do not have a copy of the TX-2's assembler, "M4".

The TX-2 project is in the process of writing a compatible
cross-assembler ("tx2m4as") which runs on modern computer which
generates binaries suitable for running on the TX-2 (or at least an
emulator, since the original TX-2 machine no longer exists).


To assemble the Sketchpad code, you will need two git repositories
checked out at the same time: the TX-2-Simulator repository containing
the assembler and this repository, containing the Sketchpad code.

## Example

Here's an example terminal session in which we build the assembler
itself and then attempt to use it to assemble Sketchpad.

### Building the Assembler

The assembler's [Getting
Started](https://github.com/TX-2/TX-2-simulator/blob/main/docs/assembler/getting-started.md)
guide gives more detailed instructions on how to build it, but here we
will simply show an example of doing so.


```
mkdir assembling-sketchpad
cd assembling-sketchpad
git clone https://github.com/TX-2/TX-2-simulator.git
git clone https://github.com/TX-2/Sketchpad.git
( cd TX-2-simulator && cargo build --workspace )
```


### Running the Assembler

```
cd Sketchpad
../TX-2-simulator/target/debug/tx2m4as --list --output sk.tape sk.tx2as
```

You will notice if you do this that the assembler cannot currently
assemble the code, due to [limitations in the
assembler](https://github.com/TX-2/TX-2-simulator/blob/main/docs/assembler/limitations.md).
Because assembly did not succeed, no output file is created.
