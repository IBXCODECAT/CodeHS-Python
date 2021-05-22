def count_occurrences(line, char):
    found = 0
    
    for letter in line:
        if(letter == char):
            found = found + 1
    
    return found

text = input("please enter a string: ")

char = input("Enter a second string I guesss: ")   

print count_occurrences(text, char)