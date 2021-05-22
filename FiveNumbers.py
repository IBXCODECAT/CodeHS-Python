numList = []
result = 0

for i in range(5):
    num = int(input("Enter a number: "))
    numList = numList + [num]
    print numList

for i, item in enumerate(numList):
    result = result + item
    
print "\n\nAddition Result: " + str(result)