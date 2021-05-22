"""
This program gives several examples of creating strings out of two other
strings, or out of pieces of those strings.
"""

string_one = "abcde"
string_two = "fghij"

print "string1: " + string_one
print "string2: " + string_two

string_three = string_one + string_two
print "string3: " + string_three

string_four = string_two + string_one
print "string4: " + string_four

string_five = string_one + " " + string_two
print "string5: " + string_five

string_six = string_one[0] + " " + string_two[1:]
print "string6: " + string_six