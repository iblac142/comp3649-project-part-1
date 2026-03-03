import intermediateLine
import livenessAnalysis

#need to implement input
file = open("test.txt")
content = file.read()
file.close()

content = content.splitlines()
liveness = content.pop()
#liveness error
tokenizedContent = []
for line in content:
    temp = intermediateLine.formLine(line)
    temp.printTokenizedLine()
    print ()
    tokenizedContent.append(temp)
    

#print (content)
livenessAnalysis.setLiveness(tokenizedContent)

for l in tokenizedContent:
    print(l.printLiveness())
#print (liveness)