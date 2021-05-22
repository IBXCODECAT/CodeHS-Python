my_string = input("Enter a string of lowercase letters: ")

vowel = False

for letter in my_string:
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        vowel = True
        
if(vowel):
    print "contains a vowel"
else:
    print "does not contain a vowel"