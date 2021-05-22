#This function draws a checkmark
def draw_checkmark():
    color("green")
    pensize(10)
    penup()
    backward(50)
    right(45)
    pendown()
    forward(50)
    left(90)
    forward(100)

   
#This function draws the up arrow
def draw_up():
    left(90)
    forward(100)
    left(45)
    backward(50)
    forward(50)
    right(90)
    backward(50)
    forward(50)
    left(45)
    backward(100)

#This function draws the down arrow
def draw_down():
    right(90)
    forward(100)
    left(45)
    backward(50)
    forward(50)
    right(90)
    backward(50)
    forward(50)
    left(45)
    backward(100)
    

#===========MAIN CODE============

user_number = 0

while user_number != 5:
    
    input("Press enter to continue...")
    
    reset()
    speed(0)
    
    user_number = int(input("Guess a number 1-10 only: "))
    
    if user_number > 5:
        draw_down()
    elif user_number < 5:
        draw_up()

draw_checkmark()
print("You won!!! Now go do something productive!")