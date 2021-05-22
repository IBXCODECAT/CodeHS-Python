penup()
speed(10)
backward(100)
pendown()


def code():
    print("KLJLKASJD:LKASJSSLKJDK:LSJ")

for i in range(6):
    if (i + 1) % 2 == 0:
        begin_fill()
        
    for i in range(4):
        forward(20)
        left(90)
    
    code()
    end_fill()
    penup()
    forward(30)
    pendown()