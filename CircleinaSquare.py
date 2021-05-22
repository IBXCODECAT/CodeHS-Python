left(90)
penup()
backward(100)

radius = int(input("Rad"))

def draw(r, d, s):
    pendown()
    circle(r, d,s)

right(90)
begin_fill()
color("Red")
for i in range(4):
    forward(radius * 2)
    left(90)
end_fill()
color("Blue")
penup()
forward(radius)
begin_fill()
circle(radius)
end_fill()