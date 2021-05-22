"""
This program shows how indexing and slicing can be used with lists.
"""

# Creating an empty list:
my_list = []
print my_list

# Creating a list with things in it:
list_of_things = ["hi", 3, 4.8]

thing_zero = list_of_things[0]
thing_one = list_of_things[1]
thing_two = list_of_things[2]


print thing_zero
print thing_one
print thing_two

print list_of_things

print len(list_of_things)

# Unlike with a tuple, you can change a particular element in a list!
list_of_things[0] = 2

print list_of_things

# Get everything starting at thing 0 and going up to BUT NOT INCLUDING thing 2
print list_of_things[0:2]

# This gets things 1 and 2
print list_of_things[1:3]

# This gets everything from thing 1
# to the end.
print list_of_things[1:]

# This gets everything from the beginning up to but not including
# thing 2
print list_of_things[:2]

# This gets the last thing.
print list_of_things[-1]

# This gets the last two things.
print list_of_things[-2:]

# This gets everything but the last thing.
print list_of_things[:-1]