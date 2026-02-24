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

# takes in a line and creates corresponding intermediateLine
def formLine (line):
    line = line.replace(" ", "")
    dst = line.pop[0]
    if (dst == 't') {
        dst.append(line.pop[0])
    }
    src1 = line[4]
    op = line[6]
    src2 = line[8]
    return intermediateLine(dst, src1, op, src2)


# ranlist = []
# line = "a = a + 1"
# ranlist.append(formLine(line))

# line = "b = v + 1"
# ranlist.append(formLine(line))

# for item in ranlist:
#     item.printIntermediateLine()