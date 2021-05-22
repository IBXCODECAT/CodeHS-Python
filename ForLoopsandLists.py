"""
This program will use for loops to go through elements in a list in
multiple ways.
"""

my_list = ["hi", 5, 4.7]

# Print each element in the list
for thing in my_list:
    print "The next thing is: " + str(thing)

# Use the len function to control the range value in your for loop
for index in range(len(my_list)):
    print "The thing at index " + str(index) + \
          " is " + str(my_list[index])
    
# Keep track of the index value as well as the element stored there
for index, value in enumerate(my_list):
    print "The thing at index " + str(index) + \
          " is " + str(value)