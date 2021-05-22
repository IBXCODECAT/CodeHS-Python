"""
This code will draw concentric circles of any size input as parameters.
"""

speed(5)

# This function moves Tracy to the bottom position of a circle based on the radius
# and then draws the circle around the center before moving back to the center
def draw_circle(radius):
    right(90)
    forward(radius)
    left(90)
    pendown()
    circle(radius)
    penup()
    setposition(0,0)
    
# Ask the user for 3 radiaii and call the draw_circle function with these values
penup()

first_radius = int(input("What is the first circle's radius?: "))
second_radius = int(input("What is the second circle's radius?: "))
third_radius = int(input("What is the third circle's radius?: "))

draw_circle(first_radius)
draw_circle(second_radius)
draw_circle(third_radius)