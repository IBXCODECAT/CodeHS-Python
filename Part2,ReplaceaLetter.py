def replace_at_index(old, new, index):
    
    string = list(old)
    
    string[index] = new;
    
    returnString = ""
    
    for i in range(len(old)):
        returnString = returnString + string[i]
    
    return returnString
        
phrase = input("Please enter a phrase: ")
index = int(input("Plase enter an index: "))
char = input("Please enter new char: ")

print replace_at_index(phrase, char[0], index)