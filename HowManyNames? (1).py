def Input():
    
    invalid = True
    
    while(invalid):
        try:
            nameCount = int(input("Enter how many names you have: "))
            invalid = False
        except ValueError:
            print "Input must be of type int32\n"
    
    _names = ""
    for i in range(nameCount):
        _name = input(str(i + 1) + ". Enter name: ")
        _names = _names + " " + _name.strip()
    
    return _names.split()
    
names = Input()

print "First name: " + names[0]

names.remove(names[0])

middleNames = ""

for i, item in enumerate(names):
    if(i == len(names) - 1): break
    middleNames = middleNames + item + " "    
    
print "Middle names: " + middleNames

print "Last name: " + names[len(names) - 1]