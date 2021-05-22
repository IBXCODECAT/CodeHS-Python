"""
This program asks the user for their name and age. It handles the case where the
user fails to enter a valid integer for their age.
"""

# Ask user for name and age.
# Enter default value for age in case they do not enter an integer
name = input("Enter your name: ")
age = -1

try:
    age = int(input("Enter your age: "))
except:
    print "That wasn't an integer."

# Print name and age, using default age if user did not enter an integer
print "Name: " + name
print "Age: " + str(age)