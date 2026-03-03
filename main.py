import intermediateLine
import livenessAnalysis
import interference
import graphColor
import targetCode
import sys

def main():
    # QUICK FIX: allow filename and reg count from command line
    # usage: python main.py <filename> <num_regs>
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> <num_regs>")
        return

    filename = sys.argv[1]
    numRegs = int(sys.argv[2])

    file = open(filename)
    content = file.read()
    file.close()
    content = content.splitlines()

    liveness = content.pop()
    livenessCheck = liveness[:5]
    liveness = liveness[5:]
    if (livenessCheck != "live:"):
        print ("Error: Last line is not in form live: 'var'")
        return

    liveness = liveness.replace(" ", "")
    operation = liveness.split(',')
    liveness = []
    for var in operation:
        t, empty = intermediateLine.checkVar(var)
        liveness.append(t)

    tokenizedContent = []
    for line in content:
        temp = intermediateLine.formLine(line)
        tokenizedContent.append(temp)

    varSet = list(livenessAnalysis.setLiveness(tokenizedContent, liveness))
    intGraph = interference.createInterferenceGraph(tokenizedContent, varSet)

    # print interference table
    intGraph.displayAdjacencies()

    colored = graphColor.graphColor(len(varSet), numRegs, intGraph)
    ok = colored.solve()

    if not ok:
        print("Not enough registers to allocate without spilling.")
        return

    print("Coloring succeeded:", colored.variableColors)

    # ---- YOUR PART: generate assembly ----
    regMap = targetCode.buildRegMap(intGraph, colored.variableColors)
    asmLines = targetCode.generateAssembly(tokenizedContent, regMap)
    outFile = targetCode.writeAssemblyFile(filename, asmLines)

    print("\nRegister assignment table:")
    targetCode.printColoringTable(intGraph, colored.variableColors, numRegs)

    print("\nWrote assembly to:", outFile)

main()
