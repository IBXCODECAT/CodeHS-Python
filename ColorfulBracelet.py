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
speed(10)
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
    
def multiple_of(x):
    if x % 3 == 0:
        return 0
    if x % 2 == 0:
        return 1
    if x % 1 == 0:
        return 2
    
for i in range(36):
    print(i)
    begin_fill()
    if multiple_of(i) == 0:
        color("blue")
        print("blue")
    if multiple_of(i) == 1:
        color("red")
        print("red")
    if multiple_of(i) == 2:
        color("purple")
        print("purple")
    draw_circle(10, 10, 20)
    end_fill()