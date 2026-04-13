import intermediateLine
import livenessAnalysis
import interference
import graphColor
import targetCode
import commandLine

def main():
    content, numRegs, filename = commandLine.processCommandLine()
    if (content == 0):
        return

    try:
        liveness = content.pop()
        liveVar = livenessAnalysis.liveness_check(liveness)
    except IndexError:
        print ("Error: Empty File")
        return
    if (liveVar == 0):
        print ("Error: Liveness error")
        return

    tokenizedContent = []
    for line in content:
        temp = intermediateLine.formLine(line)
        if (temp == 0):
            return
        tokenizedContent.append(temp)

    varSet = livenessAnalysis.setLiveness(tokenizedContent, liveVar)
    
    if (varSet == 0):
        print("Error: At least one live variable does not occur in the code")
        return
        
    varSet = list(varSet)

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