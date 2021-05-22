"""
This program shows how it is possible to index a list inside a list.
"""

my_list = []
my_list.append([1, 2, 3])
my_list.append([4, 5, 6])

print my_list

# Indexing into myList gives you a list of numbers
print my_list[0]

# Indexing into THAT gives you a number
print my_list[0][1]