"""
This program usees the keyword 'in' to determine if a certain character or
group of characters exists in a given string.
"""

word = "eggplant"

# Check if the letter 'e' is found in the given word
if "e" in word:
    print "Found an e in " + word
else:
    print "Didn't find an e in " + word

# Check if the letter 'a' is found in the given word
letter = "a"
if letter in word:
    print "Found " + letter + " in " + word
else:
    print "Didn't find " + letter + " in " + word
    
# Check if the phrase 'egg' is found in the given word
phrase = "egg"
if phrase in word:
    print "Found " + phrase + " in " + word
else:
    print "Didn't find " + phrase + " in " + word