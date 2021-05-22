nameList = []
lastNames = []

for i in range(5):
    name = input("Enter your full name: ")
    nameList.append(name)
    
for i in range(5):
    lastNames.append(nameList[-1])

lastNames.sort()

print lastNames