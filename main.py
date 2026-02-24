import intermediateLine

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
    

print (content)
print (liveness)