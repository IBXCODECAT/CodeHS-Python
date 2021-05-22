"""
This program uses the remove method to remove a particular thing from a list.
"""

my_list = ["apple", "banana", "orange", "grapefruit"]
print my_list

my_list.remove("apple")
print my_list

# Note that it ONLY removes the first occurrence of something.

my_list = ["apple", "banana", "orange", "grapefruit", "apple"]
print my_list

my_list.remove("apple")
print my_list