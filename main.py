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
    liveness = liveness.split(',')

    tokenizedContent = []
    for line in content:
        temp = intermediateLine.formLine(line)
        temp.printTokenizedLine()
        print ()
        tokenizedContent.append(temp)
        
    livenessAnalysis.setLiveness(tokenizedContent)

    for l in tokenizedContent:
        print(l.printLiveness())

main()