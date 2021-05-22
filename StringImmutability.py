"""
This program shows the immutability of strings.
"""

my_string = "hello!"

my_string = "hi!"

my_other_string = my_string[:2]

# This line will cause an error because it tries to change a string.
my_string[0] = "H"