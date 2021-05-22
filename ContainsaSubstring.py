"""
Ask the user for a string and something to look for within the string. Output whether
the second string is, in fact, in the first string.
"""

big_string = input("Enter a string: ")
string_to_find = input("Enter what to look for: ")

if string_to_find in big_string:
    print "Found it!"
else:
    print "Didn't find it."