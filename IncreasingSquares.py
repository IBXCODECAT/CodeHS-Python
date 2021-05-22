length = 50
speed(0)

while length <= 400:
    penup()
    backward(25)
    right(90)
    backward(25)
    left(90)
    pendown()
    
  
    for i in range(4):
        forward(length)
        right(90)
    
    length = length + 50