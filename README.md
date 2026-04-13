# COMP 3649 Project Part 1 — Register Allocating Code Generator

**Authors:** Daksh Thawani, Iain Black, Vincent Ha

A Haskell program that takes a basic block of intermediate code (IR), performs liveness analysis, builds an interference graph, does graph colouring for register allocation, and outputs target assembly code.

---

## How to run

You need Python installed.

```
python main.py <num_regs> <filename>
```

- `<num_regs>` — number of registers available (must be a positive integer)
- `<filename>` — path to the input file

**Example:**

```
python main.py 3 test.txt
```

This will print the interference table and register colouring table to stdout, then write the generated assembly to `test2.txt.s`.

---

## Input file format

The input file is a plain text file describing a single basic block of intermediate (three-address) code.

**Each code line must follow one of these three forms:**

```
dst = src1 op src2     (binary operation)
dst = op src2          (unary negation, only - is supported)
dst = src2             (simple assignment)
```

- `dst` is a single lowercase letter (`a`–`z`) or a temporary variable (`t` followed by digits, e.g. `t1`, `t23`)
- `src1`, `src2` are variables, temporaries, or integer literals
- `op` is one of `+`, `-`, `*`, `/`

**The last line must be the live-on-exit declaration:**

```
live: <comma-separated variable list>
```

The live list can be empty (`live:`) or contain variables and temporaries separated by commas, with no spaces.

**Full example (`test2.txt`):**

```
a = a + 1
t1 = a * 4
t2 = t1 + 1
t3 = a * 3
b = t2 - t3
t4 = b / 2
d = c + t4
live: d
```

**Rules:**

- Whitespace within code lines is ignored during parsing (spaces are stripped before tokenizing)
- Variable names are single alphabetic characters only (e.g. `a`, `b`, `d`)
- Temporary names start with `t` followed by one or more digits (e.g. `t1`, `t23`)
- Literals are non-negative integers
- Every variable listed in `live:` must appear somewhere in the code
- Blank lines are ignored

---

## Output

When the program runs successfully, it prints two tables to stdout and writes an assembly file.

**Stdout example:**

```
a: t1, t3, b, ...
...
Coloring succeeded: [0, 1, ...]

Register assignment Table:
R0: a, t2
R1: t1, t3
R2: b, t4, d
...

Wrote assembly to: test2.txt.s
```

**Assembly file** (`<inputfile>.s`):

The generated assembly uses a simple two-operand format:

```
MOV    src, dst
ADD    src, dst
SUB    src, dst
MUL    src, dst
DIV    src, dst
```

Variables live on entry are loaded first (`MOV varname, Rx`). Variables live on exit that were modified are stored at the end (`MOV Rx, varname`). All other variables are kept in registers throughout.

---

## Limitations and known issues

- **No spill support.** If the graph cannot be coloured with the number of registers you provide, the program exits with:
  ```
  Error: Not enough registers to allocate without spilling.
  ```
  There is no spill code generation — increase `<num_regs>` and rerun.

- **Single basic block only.** The program does not handle control flow, branches, loops, or function calls. Input must be a straight-line block.

- **Variable names are single characters.** Multi-character variable names (other than temporaries) are not supported. `a`–`z` only.

- **No negative literals.** Negative constants in the source (e.g. `a = -5`) are parsed as unary negation applied to a variable/temp, not as a literal. Writing `a = -5` where `5` is meant as a literal will cause a parse error.

- **Temporary variable naming.** Temporaries must start with `t` followed by digits (`t1`, `t2`, etc.). A lone `t` with no digits is treated as a regular variable named `t`, not a temporary.

- **No type checking.** The program does not validate types or ranges of literals. Very large integers are accepted without warning.

- **Output file location.** The `.s` file is always written to the same directory as the input file, named `<inputfile>.s`. If that path is not writable, the program will report an error and exit.

- **Whitespace in live line.** The `live:` line parser strips all whitespace, so `live: a, b` and `live:a,b` are equivalent. However, `live :` (space before colon) will fail to parse.

---

## Project structure

| File | Description |
|------|-------------|
| `main.py` | Main driver, pipeline |
| `commandLine.py` | Handles command line input |
| `graph.py` | Class definition of an adjacency matrix of a graph data type |
| `graphColor.py` | Class definition used to color the graph |
| `interference.py` | Function to create interference graph |
| `intermediateLine.py` | Class definition representing a line of input code |
| `livenessAnalysis.py` | Functions to get and check liveness of variables |
| `targetCode.py` | Functions to generate machine code |
| `tokenizing.py` | Class definition representing a single token |
| `testLivenessAnalysis.py` | Small module to run testing on liveness|
| `test(1-4).txt` | Sample input files
