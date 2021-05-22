speed(10)
rad = 15
penup()
backward(150)

def draw_circle(r):
    pendown()
    begin_fill()
    circle(r)
    end_fill()
    penup()

for i in range(8):
    color_choice = input("Enter A Color Name Or Hexidecimal:")
    print color_choice
    
    color(color_choice)
    
    draw_circle(rad)
    
    forward(rad * 2)