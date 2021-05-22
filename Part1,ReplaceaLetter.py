def replace_at_index(old, index):
    
    string = list(old)
    
    string[index] = "-";
    
    returnString = ""
    
    for i in range(8):
        returnString = returnString + string[i]
    
    return returnString
        
print replace_at_index("eggplant", 3)