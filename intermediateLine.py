import tokenizing

# Class for building intermediate representation
# expected input
#   string in the form
#       var = number/var op number/var op number/var...
# expected output
#   For binary operations form is
#   dst 
#   src1 
#   op 
#   src2
#
#   For unary negation/operations form is
#   dst
#   op (-)
#   src2
#
#   For single assignment form is
#   dst
#   src2

#todo:
# error checking
#   completed multi digit
#   completed liveness/lines
#   completed equals sign
#   completed empty liveness
#   completed t multi digit
#   check unary
#   check single assignment
#   completed invalid temp variable
#   completed invalid var ! . %
#   completed invalid op


class intermediateLine:
    def __init__ (self, dst, src1, op, src2):
        self.dst = dst
        self.src1 = src1
        self.op = op
        self.src2 = src2
        self.liveness = set()
    
    def printIntermediateLine(self):
        print (self.dst) 
        print (self.src1) 
        print (self.op) 
        print (self.src2) 

    def printTokenizingdLine (self):
        self.dst.printToken()
        self.src1.printToken()
        self.op.printToken()
        self.src2.printToken()
        
    def getSRC1(self):
        return self.src1

    def getSRC2(self):
        return self.src2

    def getDST(self):
        return self.dst
        
    def printLiveness (self):
        for i in self.liveness:
            print(i.getValue())
        print(",")

  

# takes in a line and creates corresponding intermediateLine
# After each process each processed segment will be sliced out
def formLine(line):
    line = line.replace(" ", "")
    dst, line = checkVar(line)
    if (dst.getTag() == 7):
        return 0
    if (line[0] != '='):
        print ("Error: Line missing equals sign")
        return 0
    line = line[1:]
    
    src1, line = checkVar(line)
    if (src1.getTag() == 7):
        return 0
    op, line = checkOP(line)
    if (op.getTag() == 7):
        return 0
    #always go through src2
    src2, line = checkVar(line)
    if (src2.getTag() == 7):
        return 0
    return intermediateLine(dst, src1, op, src2) 

# takes the first character and checks if it is a temp or a var
# if temp check number identifier and assign it temp
# if var assign var
def checkVar(line):
    temp = line[0]
    #check if is not permitted
    if (temp == 't'):
        i = 1
        temp = ''
        while (i < len(line) and line[i].isnumeric()):
            temp = temp + line[i]
            i += 1
        line = line[i:]
        var = tokenizing.token(3, temp)
        if (temp == ''):
            print ("Error: Invalid Temporary Variable")
            var = tokenizing.token(7, 0)
    elif (temp.isalpha()):
        var = tokenizing.token(2, temp)
        line = line[1:]
    elif (temp.isnumeric()):
        i = 1   #start after temp
        while (i < len(line) and line[i].isnumeric()):
            temp = temp + line[i]
            i += 1
        var = tokenizing.token(1, temp)
        line = line[i:]
    else: 
        print ("Error: Invalid Operand")
        var = tokenizing.token(7, 0)
    return var, line

#a switch to check for which operator is being applied
def checkOP(line):
    match line[0]:
        case "+":
            op = tokenizing.token(0, 0)
        case "-":
            op = tokenizing.token(0, 1)
        case "*":
            op = tokenizing.token(0, 2)
        case "/":
            op = tokenizing.token(0, 3)
        case _:
            print ("Error: Invalid Operator")
            op = tokenizing.token(7, 0)
    return op, line[1:]