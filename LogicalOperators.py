x = True
y = False

print "x: " + str(x)
print "y: " + str(y)

print "x and y"
print x and y

print "x or y"
print x or y

print "x and not y"
print x and not y

# This means "It is not the case
# that x is true, and it is the
# case that y is true."
print "not x and y"
print not x and y

# Notice that you can use parentheses
# to force (x and y) to be evaluated
# before the "not" keyword is applied.
#
# This means "It is not the case that
# both x and y are true."
print "not (x and y)"
print not (x and y)