#INSTRUCTIONS
'''
The bracelet should follow these specifications:

There must be 36 beads
Each bead should have a radius of 10 pixels
The bracelet must have a diameter of 200
Hints:

You will need to use a function and a loop in your code!
You will need to turn Tracy 10 degrees after drawing each bead
You should return to the middle of the bracelet circle between drawing each bead
'''
#End INSTRUCTIONS

#Early Setup
speed(0)
penup()
left(90)
backward(100)
right(90)
    
#Bracelet
    
def draw_circle(rad, deg, dist):
    pendown()
    circle(rad)
    left(deg)
    penup()
    forward(dist)
    
for i in range(36):
    draw_circle(10, 10, 20)