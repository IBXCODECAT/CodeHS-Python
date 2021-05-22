"""
This program computes the area
of a trapezoid.
"""

# Ask for the length of the two
# parallel sides - base and top
base = int(input("Base: "))
top = int(input("Top: "))

# Ask for the height
height = int(input("Height: "))

# Compute and print the area of the
# trapezoid.
area = 0.5 * (base + top) * height
print "Area: " + str(area)