import graph
import token
import itertools

def createInterferenceGraph(lines, varSet):
    intGraph = graph.graph(len(varSet))
    i = 0
    for v in varSet:
        intGraph.defineVertex(i, v)
        i += 1
    for l in lines:
        for pair in list(itertools.combinations(l.liveness, 2)):
            intGraph.addEdge(intGraph.idOf(pair[0]), intGraph.idOf(pair[1]))
            
    return intGraph