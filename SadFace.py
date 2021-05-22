def happy_face():
    left(90)
    forward(100)
    pendown()
    pensize(5)
    circle(40, 180)
    
def sad_face():
    left(90)
    forward(100)
    pensize(5)
    circle(40, 180)
    pendown()
    circle(40, 180)
    
def draw_face():
    speed(10)
    
    penup()
    left(90)
    backward(100)
    right(90)
    color("yellow")
    pendown()
    begin_fill()
    circle(100)
    end_fill()
    penup()
    left(90)
    color("black")
    forward(155)
    left(90)
    backward(40)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()
    forward(80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    penup()


draw_face()
happy = input("Are you happy? Please enter 'YES' or 'NO': ")
    
if happy == "YES":
    happy_face()
else:
    sad_face()