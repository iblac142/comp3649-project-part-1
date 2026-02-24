import token

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
#   check liveness/lines
#   check equals sign
#   check unary
#   check single assignment
#   check invalid var ! . %
#   check invalid op


class intermediateLine:
    def __init__ (self, dst, src1, op, src2):
        self.dst = dst
        self.src1 = src1
        self.op = op
        self.src2 = src2
    
    def printIntermediateLine(self):
        print (self.dst) 
        print (self.src1) 
        print (self.op) 
        print (self.src2) 

    def printTokenizedLine (self):
        self.dst.printToken()
        self.src1.printToken()
        self.op.printToken()
        self.src2.printToken()


# takes in a line and creates corresponding intermediateLine
# After each process each processed segment will be sliced out
def formLine(line):
    line = line.replace(" ", "")
    dst, line = checkVar(line)
    #check for equals
    line = line[2:]
    #check sign
    src1, line = checkVar(line)
    line = line[1:]
    op, line = checkOP(line)
    #always go through src2
    src2, line = checkVar(line)
    return intermediateLine(dst, src1, op, src2) 

#takes the first character and checks if it is a temp or a var
# if temp check number identifier and assign it temp
# if var assign var
def checkVar(line):
    temp = line[0]
    #check if is not permitted
    if (temp == 't'):
        var = token.token(3, line[1])
        line = line[1:]
    elif (temp.isalpha()):
        var = token.token(2, temp)
    elif (temp.isnumeric()):
        i = 1   #start after temp
        while (i < len(line) and line[i].isnumeric()):
            temp = temp + line[i]
            i += 1
        var = token.token(1, temp)
        i -= 1
        line = line[i:]
    return var, line

#a switch to check for which operator is being applied
def checkOP(line):
    match line[0]:
        case "+":
            op = token.token(0, 0)
        case "-":
            op = token.token(0, 1)
        case "*":
            op = token.token(0, 2)
        case "/":
            op = token.token(0, 3)
    return op, line[1:]
