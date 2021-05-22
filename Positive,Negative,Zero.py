"""
This program determines if a number is positive, negative, or and then communicates
that to the user by drawing a plus sign, minus sign, or 0.
"""

speed(5)

# This function draws a zero in the middle of the canvas
def draw_zero():
    penup()
    setposition(0,-150)
    pendown()
    circle(50)

# This function draws a minus sign in the middle of the canvas
def draw_minus():
    forward(50)
    backward(100)
    forward(50)

# This function draws a plus sign in the middle of the canvas    
def draw_plus():
    for i in range(4):
        forward(50)
        backward(50)
        left(90)    

# The user is asked to give a number. If they answer with a positive value,
# a plus sign appears. If they answer with a negative value, a minus sign
# appears and if they answer with a 0, a 0 appears.
number = int(input("Enter a number: "))

pensize(10)
color("blue")
if number > 0:
    draw_plus()
elif number < 0:
    draw_minus()
else:
    draw_zero()