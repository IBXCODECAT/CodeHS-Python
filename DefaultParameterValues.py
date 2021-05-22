# This function prints the numbers given as parameters and uses a
# default value for y if none is given.
def print_two_numbers(x, y = 10):
    print "First number: " + str(x)
    print "Second number: " + str(y)

print_two_numbers(5)
print_two_numbers(7, 8)