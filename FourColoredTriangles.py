"""
Have sides of different colors (red, green and blue!)
Have sides that are 50 pixels long
Are centered around the y-axis
Have sides drawn with a thickness of 5 pixels
Hints:

Tracy is drawing 4 triangles, which means that 2 should be left of center and 2 should be right of center. Each triangle has a width of 50. This should help you figure out where to place Tracy to center your triangles!
Try to figure out how you can use a for loop to shorten your code!
"""
color("red")
pensize(5)
forward(100)
backward(200)

def draw_triangle_hump():
    color("green")
    left(60)
    forward(50)
    right(120)
    color("blue")
    forward(50)
    left(60)

for x in range(4):
    draw_triangle_hump()