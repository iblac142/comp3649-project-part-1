import intermediateLine
import livenessAnalysis

def main():
    #need to implement input
    file = open("test.txt")
    content = file.read()
    file.close()
    content = content.splitlines()

    liveness = content.pop()
    livenessCheck = liveness[:5]
    liveness = liveness[5:]
    if (livenessCheck != "live:"):
        print ("Error: Last line is not in form live: 'var'")
        return
    liveness = liveness.replace(" ", "")
    operation = liveness.split(',')
    liveness = []
    for var in operation:
        token, empty = intermediateLine.checkVar(var)
        liveness.append(token)

    tokenizedContent = []
    for line in content:
        temp = intermediateLine.formLine(line)
        tokenizedContent.append(temp)
        
    livenessAnalysis.setLiveness(tokenizedContent)

#   for l in tokenizedContent:
#        print(l.printLiveness())
main()