"""
This program draws three shapes from the same position. Each shape is a 
different color.
"""

speed(5)

# Draws a red circle
color("red")
begin_fill()
circle(75)
end_fill()

# Draws a blue square due to 4 steps
color("blue")
begin_fill()
circle(75,360,4)
end_fill()

# Draws a yellow triangle due to 3 steps
color("yellow")
begin_fill()
circle(75,360,3)
end_fill()