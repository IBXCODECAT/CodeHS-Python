#Instructions
#End Instructions

w = 50
h = 50

#Early Setup
speed(0)
pensize(2)
bgcolor("black")
color("white")
penup()
setposition(-w / 2, -200)
pendown()
left(90)

def draw_square(dist):
    for i in range(4):
        forward(dist)
        right(90)
    
def draw_circle(rad):
    circle(rad)
    penup()
    backward(rad)
    left(90)
    forward(h)
    pendown()
    
def next_shape_circle_prep():
    right(90)
    forward(w / 2)
    left(90)
    penup()
    forward(h)
    pendown()
    right(90)

for x in range(4):
    draw_square(h)
    next_shape_circle_prep()
    draw_circle(h / 2)