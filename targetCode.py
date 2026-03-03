# targetCode.py
import token as tokmod

# Map token OPERATION values to assembly mnemonics
OP_TO_MNEMONIC = {
    tokmod.ADD: "ADD",
    tokmod.SUB: "SUB",
    tokmod.MUL: "MUL",
    tokmod.DIV: "DIV",
}

def _token_to_operand(t, regMap):
    """
    Convert a token into assembly operand string.
    - NUMBER -> #<value>
    - VARIABLE/TEMP -> R<reg>
    """
    tag = t.getTag()
    val = t.getValue()

    if tag == tokmod.NUMBER:
        return f"#{val}"

    # VARIABLE or TEMP
    if t in regMap:
        return f"R{regMap[t]}"

    # fallback (should not happen if coloring includes all vars/temps)
    return str(val)

def buildRegMap(intGraph, colorList):
    """
    intGraph.vertices[i] is the token stored at vertex i
    colorList[i] is the register number assigned (0..k-1)
    """
    regMap = {}
    for i, vtok in enumerate(intGraph.vertices):
        regMap[vtok] = colorList[i]
    return regMap

def generateAssembly(irLines, regMap):
    """
    Convert intermediateLine objects into assembly lines.
    Format:
      ADD Rdst, Rsrc1, Rsrc2
      MOV Rdst, #imm   (if we ever support no-op lines later)
    Current intermediateLine always stores: dst, src1, op, src2
    """
    asmLines = []

    for line in irLines:
        dst = _token_to_operand(line.getDST(), regMap)
        src1 = _token_to_operand(line.getSRC1(), regMap)
        src2 = _token_to_operand(line.getSRC2(), regMap)

        opTok = line.op  # token.token(OPERATION, <0..3>)
        mnemonic = OP_TO_MNEMONIC.get(opTok.getValue(), "ADD")

        asmLines.append(f"{mnemonic} {dst}, {src1}, {src2}")

    return asmLines

def writeAssemblyFile(inputFilename, asmLines):
    outName = inputFilename + ".s"
    with open(outName, "w") as f:
        for a in asmLines:
            f.write(a + "\n")
    return outName

def printColoringTable(intGraph, colorList, numRegs):
    """
    Prints:
      R0: a,t1
      R1: b
    based on graph.vertices tokens
    """
    regBuckets = [[] for _ in range(numRegs)]
    for i, vtok in enumerate(intGraph.vertices):
        r = colorList[i]
        if r != -1:
            regBuckets[r].append(str(vtok.getValue()))

    for r in range(numRegs):
        print(f"R{r}: " + ",".join(regBuckets[r]))
