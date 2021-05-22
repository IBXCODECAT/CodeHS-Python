"""
This code will fill the canvas with light blue circles.
"""
speed(0)

# This function will draw a row of 10 circles.
def draw_circle_row():
    for i in range(10):
        pendown()
        begin_fill()
        color("light blue")
        circle(20)
        end_fill()
        penup()
        forward(40)
        
def move_up_a_row():
    left(90)
    forward(40)
    right(90)
    backward(400)
    
# Send Tracy to starting position in bottom left corner.
penup()
setposition(-180,-200)

# Call circle drawing function
for i in range(10):
    draw_circle_row()
    move_up_a_row()