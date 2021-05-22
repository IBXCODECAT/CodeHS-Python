"""
This program shows how strings can be turned into lists and lsits into strings.
"""

my_string = "abcde"
print my_string

# Turn string into a list
my_list = list(my_string)
print my_list

# Turn list into a string
my_other_string = "".join(my_list)
print my_other_string