

def calc():
    printString = ""
    index = 0
    
    
    for letter in name.upper():
        if(letter.find("A") > -1 or letter.find("E") > -1 or letter.find("I") > -1 or letter.find("O") > -1 or letter.find("U") > -1):
            printString = printString + "\n There is an " + letter.lower() + " in your name, first found at index " + str(index) + "" 
        
        index = index + 1
    
    return printString

name = input("Please enter your first name: ")

print ""

print calc()