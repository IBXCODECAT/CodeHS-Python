"""
This program uses the count method which does not change the list. It returns
an integer that represents how many instances of a particular thing were
found in the list.
"""

# List of numbers
my_list = [1, 4, 2, -4, 10, 0, 4, 2, 1, 4]
print my_list

# Find how many of each number are in the list
print "There are " + str(my_list.count(4)) + " 4's in this list."
print "There are " + str(my_list.count(1)) + " 1's in this list."
print "There are " + str(my_list.count(-4)) + " -4's in this list."
print "There are " + str(my_list.count(700)) + " 700's in this list."

print "-----------------"

# List of strings
list_of_strings = ["hi", "hello", "hi", "hi", "hello"]
print list_of_strings

# Find how many of each word are in the list
print "There are " + str(list_of_strings.count("hi")) + " hi's in this list."
print "There are " + str(list_of_strings.count("hello")) + " hello's in this list."