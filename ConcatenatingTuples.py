"""
This program shows how to concatenate tuples.
"""

x = (1, 2)
y = (5, 6)

my_tuple = x + (3, 4) + y

print my_tuple


my_tuple = x + (3,) + y

# This should print (1, 2, 3, 5, 6)
print my_tuple