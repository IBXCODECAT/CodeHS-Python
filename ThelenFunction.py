"""
This program shows how to use the len function to determine the length of
a string.
"""

print len("hello")
print len("")
print len("a b c d e")

my_string = "hello"
bad_index = len(my_string)

# This line causes an error.
print my_string[bad_index]