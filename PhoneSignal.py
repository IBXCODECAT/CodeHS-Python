for i in range(5):
    for x in range(2):
        forward(10)
        left(90)
        forward((i + 1) * 10)
        left(90)
    penup()
    forward(25)
    pendown()