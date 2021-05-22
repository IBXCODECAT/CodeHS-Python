"""
This code will have Tracy draw an x and y-axis on our screen with
hash marks every 25 pixels.
"""

speed(5)

# This function will draw a line with hash marks at every 25 pixels.
def draw_hashed_axis():
    pendown()
    for i in range(16):
        forward(25)
        right(90)
        forward(10)
        backward(20)
        forward(10)
        left(90)
       
# Move Tracy to top of canvas and call draw hash marks function for y-axis.
# Then move Tracy to left of canvas and call hash marks function for x-axis.
penup()
setposition(0,200)
right(90)
draw_hashed_axis()
penup()
setposition(-200,0)
left(90)
draw_hashed_axis()