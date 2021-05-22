speed(0)
secret_number = 5
user_number = "null"

while (user_number != secret_number):
    user_number = int(input("Please guess a number 1-10: "))    

print("Congradulations! You won")
color("green")
penup()
left(90)
backward(50)
right(90 + 45)
pendown()
pensize(10)
backward(50)
forward(50)
left(90)
forward(10)