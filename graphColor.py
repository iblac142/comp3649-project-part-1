# a class which contains a graph which needs to be colored using a certain number of colors
# 
# size: the number of variables (and temp variables) used in the graph
# regNum: the number of registers
# adjMat: the adjacency matrix containing the vertices and edges of the graph
#
# solve: recursively colors the graph, returning True if successful and false if not
class graphColor:
    def __init__(self, size, regNum, adjMat):
        # -1 represents no color
        self.variableColors = [-1] * size
        self.n = regNum
        self.solved = False
        self.adjMat = adjMat
        self.size = size
        
        # if more registers than variables, color graph trivially
        if regNum >= size:
            solved = True
            for i in range(len(self.variableColors)):
                self.variableColors[i] = i
    
    # recursively colors the graph
    def solve(self):
        if self.solved:
            return True
        else:
            # find first uncolored vertex
            i = 0
            while i < len(self.variableColors) and self.variableColors[i] != -1:
                i += 1
            # if no uncolored vertices, graph is successfully colored
            if i >= len(self.variableColors):
                return True
            # record all colors of adjacent vertices
            # (-1 is counted, but this doesn't matter)
            takenColors = set()
            for j in range(self.size):
                if self.adjMat.matrix[i][j] == 1:
                    takenColors.add(self.variableColors[j])
            # attempt to color the vertex with an unused color
            for k in range(self.n):
                if not k in takenColors:
                    self.variableColors[i] = k
                    # continue solving recursively with this choice
                    self.solved = self.solve()
                    # if successful, return True
                    if self.solved:
                        return True
                    # otherwise, undo the change
                    self.variableColors[i] = -1
            # dead end reached must go back and make a different choice
            # if this is last possible choice, initial function call returns False
            return False