"""
This code will draw a square swirl from the center of the canvas.
"""

speed(5)

# Move forward and turn left 10 times. Move 10 pixels further every iteration
for i in range(10,101,10):
    forward(i)
    left(90)