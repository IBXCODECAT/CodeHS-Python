"""
This code will draw hash marks at 25, 50, 100, and 200 pixels.
"""

# Set initial value of length variable to 25
speed(5)
length = 25

# This function will draw a hash mark
def draw_hash_mark():
    left(90)
    forward(25)
    backward(50)
    forward(25)
    right(90)

# Send Tracy to starting position
penup()
setposition(-200,0)
pendown()

# Move Tracy forward by the value of 'length' and draw a hash mark
# Repeat this 4 times, doubling the length each time
for i in range(4):
    forward(length)
    draw_hash_mark()
    length = length * 2