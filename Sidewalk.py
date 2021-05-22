penup()
speed(10)

dist = 35

setposition(-200 + dist, -200)

def draw_squares():
    for i in range(8):
        pendown()
        left(45)
        circle(dist - 5, 360, 4)
        right(45)
        penup()
        forward(dist + 10)

for i in range(4):     
    draw_squares()
    left(90)
    forward(dist + 7)