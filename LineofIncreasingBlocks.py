#sets position
penup()
speed(5)
setposition(-150,0)
pendown()

#defines the function to draw one square
def draw_square():
    for i in range(4):
        forward(sidelength)
        left(90)
   
#changes the distance in between each sidelength everytime
def move():
        forward(sidelength*2)
sidelength= 10

#repeats drawing the square and moving
for i in range (5):
    draw_square()
    penup()
    move()
    sidelength= sidelength + 10
    pendown()