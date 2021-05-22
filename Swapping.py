"""
This program shows how to swap variables using unpacking.
"""

first = 10
second = 20

print "Before swap: first is " + str(first) + ",  second is " + str(second)

# Swap using unpacking
first, second = second, first

print "After swap: first is " + str(first) + ",  second is " + str(second)