import graph
import token
import itertools

# takes a list of intermediateLines which have liveness applied
#
# lines: the list of lines
# varSet: a list of every variable and temp variable token used in lines
#
# returns the interference graph of the variables
def createInterferenceGraph(lines, varSet):
    # create an empty graph
    intGraph = graph.graph(len(varSet))
    # assign each variable to a different vertex
    i = 0
    for v in varSet:
        intGraph.defineVertex(i, v)
        i += 1
    # go through every line
    for l in lines:
        # add an edge between each pair of variables in the current line's liveness
        for pair in list(itertools.combinations(l.liveness, 2)):
            intGraph.addEdge(intGraph.idOf(pair[0]), intGraph.idOf(pair[1]))
    # return the finished graph
    return intGraph