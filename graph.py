# a representation of an undirected, unweighted graph as an adjacency matrix
#
# size: how many vertices are in the graph
#
# addEdge: creates an edge between two vertices
# defineVertex: assign an index number to a token
# idOf: get the corresponding vertex index for a token
# displayAdjacencies: print the adjacencies for each vertex
class graph:
    def __init__(self, size):
        # matrix initialized with no edges
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertices = [0] * size
    
    # adds an edge between two vertices given their ids
    def addEdge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1
    
    # assigns a given token to a certain index
    def defineVertex(self, i, token):
        self.vertices[i] = token;
    
    # given a token, return the corresponding vertex index
    def idOf(self, token):
        return self.vertices.index(token)
    
    # print out the adjacencies of each vertex in the graph
    def displayAdjacencies(self):
        for i in range(self.size):
            print(self.vertices[i].value + ": ", end="")
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    print(self.vertices[j].value, end = " ")
            print()
            
        