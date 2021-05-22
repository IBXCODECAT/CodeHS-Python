def remove_all_from_string(char, word):
    
    word.find(char)
    
    final_string = word.replace(char, "")
    return final_string
    
printString = remove_all_from_string("l", "hello")

print printString