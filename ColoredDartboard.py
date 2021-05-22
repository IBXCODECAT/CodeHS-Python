"""
Consists of 4 concentric circles
Has the center circle placed in the middle of the canvas with a radius of 25
Has three circles surrounding the middle, that each increase in radius by 25 pixels
"""

penup()
left(90)
backward(80)
right(90)
pendown()

def fill_circle(r):
    begin_fill()
    color_choice = input("Enter a hexidecimal for next color:")
    color(color_choice)
    circle(r)
    end_fill()
    
def calc_circle(a, rad):
    if a == 0:
        return rad * 4
    if a == 1:
        return rad * 3
    if a == 2:
        return rad * 2
    if a == 3:
        return rad
        
def offset_turtle():
    penup()
    left(90)
    forward(25)
    right(90)
    pendown()
    
for i in range(4):
    radius = calc_circle(i, 25)
    fill_circle(radius)
    offset_turtle()