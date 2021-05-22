"""
This program demonstrates how append and extend can be used to add to a list.
"""

# Start with an empty list
my_list = []
print my_list

# Append things to the end of the list.
# Each call to append changes the list.
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print my_list

# Extend adds a list to a list!
my_list.extend([5, 6, 7])
print my_list

# This line will not actually change the value of the variable 'my_list'
print my_list + [10, 12, 14]
print my_list