#Instantiation of initial variables

#Length (Diamiter of each square)
l = 40
#Offset (Distance between squares)
o = 40

#shift (Color patern shift per row)
s = 0

#Shifts the turtle up a row
def row_shift():
    penup()
    backward(400)
    left(90)
    forward(l)
    right(90)
    pendown()

color_value = input("Please enter a color: ")

speed(0)

penup()
setposition(-200, -200)
pendown()


for i in range(10):
    if (i % 2 == 0):
        s = 1
    else:
        s = 0
        
        
    for x in range(10):
        
        if ((x + 1 + s) % 2 == 0):
            color(color_value)
        else:
            color("black")
        
        
        begin_fill()
        
        
        for y in range(4):
            
            forward(l)
            left(90)
        
            
        end_fill()
        
        penup()
        forward(o)
        pendown()
        
    row_shift()