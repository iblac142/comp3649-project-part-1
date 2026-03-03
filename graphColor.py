class graphColor:
    def __init__(self, size, regNum, adjMat):
        self.variableColors = [-1] * size
        self.n = regNum
        self.solved = False
        self.adjMat = adjMat
        self.size = size
        if regNum >= size:
            solved = True
            for i in range(len(self.variableColors)):
                self.variableColors[i] = i
    
    def solve(self):
        if self.solved:
            return True
        else:
            i = 0
            while i < len(self.variableColors) and self.variableColors[i] != -1:
                i += 1
            if i >= len(self.variableColors):
                return True
            takenColors = set()
            for j in range(self.size):
                if self.adjMat.matrix[i][j] == 1:
                    takenColors.add(self.variableColors[j])
            for k in range(self.n):
                if not k in takenColors:
                    self.variableColors[i] = k
                    self.solved = self.solve()
                    if self.solved:
                        return True
                    self.variableColors[i] = -1
            return False