# speed up the turtle ( waiting is hard)
speed(10)

# setup

'''
# pen is up so we can set the position of the turtle
#
# the setposition command takes in two parameters
# which are the x and y coordinates of where the turtle
# should be placed on the canvas. For the x position
# we have inputed 50 + 50 / 2 because the circles radius
# must be 50 because of the instructions and we are two
# and one half circles away from the 0 coordiante. So one
# half of 50 + 50 is equal to how far away we must go on
# the x axis. This number is multiplied by negitive one
# so we can move to the left side of the canvas instead
# of the right side.
#
# the y axis position is simply - 200 because the size
# of the canvas is 400 x 400 with the dimensions of
# -200, -200, 200, 200.
#
# we then put our pen back down so we can start drawing
# this new position.
'''

penup()
setposition((50 + (50 / 2) * 2) * -1, -200)
pendown()

# end setup

# draw circles

# there are three circles on the bottom
for x in range(3):
    pendown()
    circle(50)
    penup()
    forward(50 * 2)
    
# setup for next row

setposition((50 + 50) * 0.5 * -1, -200 + 100)

# draw next row of circles (Same reasoning as before)
for y in range(2):
    pendown();
    circle(50)
    penup()
    forward(50 * 2)
    
setposition(0, 0)
pendown()
circle(50)