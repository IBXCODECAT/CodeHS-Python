"""
This program shows the different elements that can be found within a tuple.
"""

my_tuple = (0, 1, "hi", (2, 3))

print my_tuple[0]
print my_tuple[1]
print my_tuple[2]

# my_tuple[3] is, itself, a tuple.
print my_tuple[3]

# The first square bracket accesses the tuple (2, 3) within the larger tuple.
# The second square bracket accesses the integers within this smaller tuple.
print my_tuple[3][0]
print my_tuple[3][1]