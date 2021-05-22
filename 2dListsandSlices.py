"""
This program shows how slicing and the append method can be used in a 2d list.
"""

my_list = []

# Append 3 lists to my_list.
for i in range(3):
    my_list.append([i * 1, i * 2, i * 4])

print my_list

# Take a slice of the outer list.
print my_list[0:2]

# Take a slice of an inner list.
print my_list[0][0:2]