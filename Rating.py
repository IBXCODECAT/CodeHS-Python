
rating = (int(input()))

def draw():
    right(180)
    color("green")
    left(45)
    forward(100)
    right(90)
    forward(50)
   
if (rating == 9):
    draw()
elif (rating >= 6):
    color("yellow")
    pensize(5)
    forward(50)
    
elif (rating >= 1):
    left(45)
    pensize(5)
    color("red")
    forward(50)
    backward(100)
    forward(50)
    left(90)
    forward(50)
    backward(100)
else:
    print("HUH?")