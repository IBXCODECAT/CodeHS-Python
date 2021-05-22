"""
This code will have Tracy draw an x and y-axis on our screen. Every other hash
mark will be bolded.
"""

speed(5)

# This function will draw a line with hash marks at every 25 pixels. The variable
# 'count' increases each time the loop iterates and changes the thickness of the pen
# based on the count value.
def hash_marks():
    count = 0
    for i in range(16):
        pendown()
        forward(25)
        right(90)
        if count % 2 == 0:
            pensize(5)
        forward(10)
        backward(20)
        forward(10)
        pensize(1)
        left(90)
        penup()
        count = count + 1
       
# Move Tracy to starting position and then call hash marks function
penup()
setposition(0,200)
right(90)
hash_marks()
setposition(-200,0)
left(90)
hash_marks()