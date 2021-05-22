'''
Tackle this problem one shape at a time. You should write four different functions to keep your code as readable as possible!
To draw a circle, do not use extended parameters. Ideally our circle would have an infinite number of points, and the only way to simulate this is to leave point values off completely.
Your end result does not have to exaclty match the given solution, but should include all of the same features.
'''

speed(0)
penup()

def draw_square():
    setposition(-100, 50)
    print("setposition: -100, 50")
    color("red")
    #left(45)
    pendown()
    begin_fill()
    circle(60, 360, 4)
    end_fill()
        
def draw_circle():
    pendown()
    color("blue")
    begin_fill()
    circle(60)
    end_fill()
    
def draw_pentigon():
    pendown()
    color("green")
    begin_fill()
    circle(60, 360, 5)
    end_fill()
    
def draw_moon():
    pendown()
    color("yellow")
    begin_fill()
    circle(60,180)
    left(90)
    forward(120)
    end_fill()
    
draw_square()
penup()
forward(200)
draw_circle()
penup()
right(90)
forward(200)
left(90)
draw_pentigon()
penup()
backward(200)
draw_moon()