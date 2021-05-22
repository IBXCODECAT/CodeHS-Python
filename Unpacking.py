"""
This program shows how unpacking can be used to separate out elements in 
a list or tuple.
"""

# Assign multiple variables at a time, like this:
x, y, z = 1, 2, 3
print "x: " + str(x)
print "y: " + str(y)
print "z: " + str(z)

# Assign multiple variables to a list (only if the number of variables
# is the SAME as the number of elements in the list.)
my_list = [10, 20, 30]
x, y, z = my_list
print "x: " + str(x)
print "y: " + str(y)
print "z: " + str(z)

# A tuple can also be used
my_tuple = (1.0, 2.0, 3.0)
x, y, z = my_tuple
print "x: " + str(x)
print "y: " + str(y)
print "z: " + str(z)