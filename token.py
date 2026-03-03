# token tag values
OPERATION = 0
NUMBER = 1
VARIABLE = 2
TEMP = 3
EQUALS = 4
LIVE = 5
NEWLINE = 6

# operation values
ADD = 0
SUB = 1
MUL = 2
DIV = 3

# a token containing information about a single element of the input file
#
# tag: represents the type of token; operation is one of the four operations,
# equals represents an equal sign, etc.
#
# value: is used based on the sort of tag;
# OPERATION (0): value is an int from 0-3 representing one of ADD, SUB, MUL, or DIV
# NUMBER (1):    value is an int representing what integer it is
# VARIABLE (2):  value is a string representing which variable it is
# TEMP (3):      value is an int representing which temporary variable it is
# EQUALS (4):    value is not used
# LIVE (5):      value is not used
# NEWLINE (6):   value is not used
#
# the class has no additional methods and is only used to store information
class token:
    # class 
    def __init__(self, tag, value):
        self.tag = tag
        self.value = value

    def printToken(self):
        print (self.tag) 
        print (self.value) 
        
    def getTag(self):
        return self.tag
        
    def getValue(self):
        return self.value