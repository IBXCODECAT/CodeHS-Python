"""
This program shows how keys are used in dictionaries.
"""

# Create an empty dictionary
my_dictionary = {}

# Set particular keys and values directly
my_dictionary["Jonathan"] = 100
my_dictionary["Karel"] = 200
my_dictionary[100] = 2

print my_dictionary

# Use the keys to print the associated values
print my_dictionary["Jonathan"]
print my_dictionary["Karel"]

# Can you guess what this line will print??
print my_dictionary[my_dictionary["Jonathan"]]