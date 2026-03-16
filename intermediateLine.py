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

INCLUDE_NONLITERAL = 0
INCLUDE_LITERAL = 1

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


# Takes in a line and creates corresponding intermediateLine
# Input: a string in one of the forms:
#       dst = src + src
#       dst = -src
#       dst = src 
# Output: a intermediate line structure filled with corresponding tokens
# After each process each processed segment will be sliced out
# Return error code 0 in the case that syntax is incorrect
def formLine(line):
    line = line.replace(" ", "")
    dst, line = checkVar(line, INCLUDE_NONLITERAL)
    if (dst.getTag() == tokenizing.ERROR):
        return 0
    if (line[0] != '='):
        print ("Error: Line missing equals sign")
        return 0
    line = line[1:]
    #if (line[0] != '-'):
    src1, line = checkVar(line, INCLUDE_LITERAL)
    if (src1.getTag() == tokenizing.ERROR):
        return 0
    #else:
    #src1 = 0
    op, line = checkOP(line)
    if (op.getTag() == tokenizing.ERROR):
        return 0
    #always go through src2
    src2, line = checkVar(line, INCLUDE_LITERAL)
    if (src2.getTag() == tokenizing.ERROR):
        return 0
    return intermediateLine(dst, src1, op, src2) 

# Takes the first character and checks if it is a temp or a var
# If temp check number identifier and assign it temp
# If var assign var
# Input: a string of one or more characters
# Output: a token that corresponds to the characters given
# Return token error in the case syntax is incorrect
def checkVar(line, literal):
    temp = line[0]
    #check if is not permitted
    if (temp == 't'):
        i = 1
        temp = ''
        while (i < len(line) and line[i].isnumeric()):
            temp = temp + line[i]
            i += 1
        line = line[i:]
        var = tokenizing.token(tokenizing.TEMP, temp)
        if (temp == ''):
            print ("Error: Invalid Temporary Variable")
            var = tokenizing.token(tokenizing.ERROR, 0)
    elif (temp.isalpha()):
        var = tokenizing.token(tokenizing.VARIABLE, temp)
        line = line[1:]
    elif (temp.isnumeric() and literal == INCLUDE_LITERAL):
        i = 1   #start after temp
        while (i < len(line) and line[i].isnumeric()):
            temp = temp + line[i]
            i += 1
        var = tokenizing.token(tokenizing.NUMBER, temp)
        line = line[i:]
    else: 
        print ("Error: Invalid Operand")
        var = tokenizing.token(tokenizing.ERROR, 0)
    return var, line

# A switch to check for which operator is being applied
# Reads only the first character of a string
# Checks if character is a valid operation
# If invalid return token error
# Otherwise return corresponding operation token
def checkOP(line):
    match line[0]:
        case "+":
            op = tokenizing.token(tokenizing.OPERATION, tokenizing.ADD)
        case "-":
            op = tokenizing.token(tokenizing.OPERATION, tokenizing.SUB)
        case "*":
            op = tokenizing.token(tokenizing.OPERATION, tokenizing.MUL)
        case "/":
            op = tokenizing.token(tokenizing.OPERATION, tokenizing.DIV)
        case _:
            print ("Error: Invalid Operator")
            op = tokenizing.token(tokenizing.ERROR, 0)
    return op, line[1:]