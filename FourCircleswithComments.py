"""
This program will draw four circles in a square formation at the center of the
canvas. Each circle will have a radius of 50.
"""
speed(5)

# Move to bottom left of circle group at position (-50,-100)
penup()
setposition(-50,-100)

# Draw two circles next to each other
for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)

# Move to top of circle row at position (-50, 0)
setposition(-50,0)

# Draw two circles next to each other
for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)