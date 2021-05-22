"""
This code will draw 9 shapes in a line, increasing from 0 points to 9.
"""
speed(5)

# Send Tracy to starting position
penup()
setposition(-180,0)

# Draw shapes where i controls the number of points and then move forward
for i in range(10):
    pendown()
    circle(20,360,i)
    penup()
    forward(40)