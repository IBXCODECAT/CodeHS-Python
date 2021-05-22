"""
This program uses for loops to iterate through a list and uses the range
values in the for loop as the index values to print each list element.
"""

first_list = [1, 10, 3]
second_list = [2, 5, 6]

# This for loop uses the length of the list to determine the index values
for index in range(len(first_list)):
    print "Looking at index: " + str(index)
    thing_in_first_list = first_list[index]
    thing_in_second_list = second_list[index]
    
    print "   1st list has: " + str(thing_in_first_list)
    print "   2nd list has: " + str(thing_in_second_list)
    if (thing_in_first_list > thing_in_second_list):
        print "      thing in 1st list was bigger"
    elif (thing_in_second_list > thing_in_first_list):
        print "      thing in 2nd list was bigger"