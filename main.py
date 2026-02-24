import intermediateLine

#need to implement input
file = open("test.txt")
content = file.read()
file.close()

content = content.splitlines()
liveness = content.pop()
#liveness error
for line in content:
    

print (content)
print (liveness)