"""
This code will have Tracy draw circles from the bottom of the canvas. The first 
circle will have a radius of 10 and the radii will increase by 10 for each. The 
code will stop when the circle reaches a radius value of 200.
"""

#Set radius value to 10
speed(10)
radius = 10

#Send Tracy to starting position at bottom middle of canvas
penup()
setposition(0,-200)
pendown()

#While the radius value is less than or equal to 200, draw circles. Increase 
#the radius value by 10 on each iteration.
while radius <= 200:
    circle(radius)
    radius = radius + 10