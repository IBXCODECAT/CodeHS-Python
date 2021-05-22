"""
This program shows how the in keyword can be used to determine whether or
not a particular key exists in a dictionary.
"""

my_dictionary = {
    "a": 1,
    "b": 2
}

# This key is in my_dictionary, so this will print True.
print "a" in my_dictionary

# This one isn't, so this will print False.
print "z" in my_dictionary

# 2 is not a key in my dictionary, so this will print False.
print 2 in my_dictionary

# You can also write a for loop that iterates
# over just the keys in the dictionary.
for key in my_dictionary:
    print "key: " + str(key)
    print "value: " + str(my_dictionary[key])