radius = 25
speed(10)

def drawCircle():
    for i in range(4):
        
        rad = radius * i + radius
        new_rad = radius + rad
        
        penup()
        left(90)
        backward(radius)
        right(90)
        pendown()
        
        circle(rad)

drawCircle()