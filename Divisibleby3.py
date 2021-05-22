booleanList = [False, False, False, False, False, False, False, False, False, False, ]
numbers = [x % 3 for x in range(1, 10)]

for i in range(len(numbers)):
    if(numbers[i] == 0):
        booleanList[i] = True

print booleanList