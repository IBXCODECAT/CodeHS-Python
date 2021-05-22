speed(10)
left(90)
penup()
backward(200)
right(90)

radius = int(input("Enter a scale factor: "))

def draw():

    color("gray")
    begin_fill()
    circle(radius)
    end_fill()
    left(90)
    forward(radius * 2)
    right(90)
    begin_fill()
    circle(radius / 2)
    end_fill()
    left(90)
    forward(radius)
    right(90)
    begin_fill()
    circle(radius / 4)
    end_fill()
    
draw()