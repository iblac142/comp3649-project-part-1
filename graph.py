class graph:
    def __init__(self, size):
        self.matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertices = [0] * size
        
    def addEdge(self, i, j):
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1
        
    def defineVertex(self, i, token):
        self.vertices[i] = token;
    
    def idOf(self, token):
        return self.vertices.index(token)
        
    def displayAdjacencies(self):
        for i in range(self.size):
            print(self.vertices[i].value + ": ", end="")
            for j in range(self.size):
                if self.matrix[i][j] == 1:
                    print(self.vertices[j].value, end = " ")
            print()
            
        