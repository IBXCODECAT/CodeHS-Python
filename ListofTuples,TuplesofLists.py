"""
This program displays the rules of modifying lists and tuples.
"""

# Here we have a list with a tuple embedded
my_list = ["a", "b", "c", (1, 2, 3)]
print my_list

# You can alter the list this way because you are allowed to replace a tuple
# and you are allowed to change a list.
my_list[3] = (10, 2, 3)
print my_list


# Here we have a tuple with a list embedded
my_tuple = ("a", "b", "c", [1, 2, 3])
print my_tuple

# You can alter the tuple by changing the element inside the list because
# you are allowed to change a list.
my_tuple[3][0] = 10
print my_tuple