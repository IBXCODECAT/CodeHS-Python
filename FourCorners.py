speed(10)
penup()
setposition(-200, -200)

square_length = int(input("Square Size: "))

def draw(d):
    pendown()
    for x in range(4):
        forward(d)
        left(90)
    penup()
        
draw(square_length)
setposition(200, 200)
right(180)
draw(square_length)
setposition(200, -200)
right(90)
draw(square_length)
setposition(-200, 200)
right(180)
draw(square_length)