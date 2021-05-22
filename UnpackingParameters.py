"""
This program shows how unpacking can be used to assign parameters to a function.
"""

def sum_three_numbers(x, y, z):
    return x + y + z

my_list = [1, 2, 3]

# Split list into respective pieces using asterisk
sum = sum_three_numbers(*my_list)
print sum