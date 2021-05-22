"""
This program creates a list of booleans from the original list, where True
is given if the number is even and False otherwise.
"""

original_list = [10, 6, -43, 4, 3, 4, 0, 50]
print [x % 2 == 0 for x in original_list]