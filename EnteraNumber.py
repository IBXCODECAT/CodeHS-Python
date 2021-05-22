"""
This program tries to retrieve an integer from the user. If the user enters
something other than an integer, the program handles it by printing an error.
"""

try:
    my_number = int(input("Enter an integer: "))
    print "Your number: " + str(my_number)
except ValueError:
    print "That wasn't an integer!"