num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

def Add():
    answer = num1 + num2
    print "\n" + str(num1) + " + " + str(num2) + " = " + str(answer)
def Sub():
    answer = num1 - num2
    print "\n" + str(num1) + " - " + str(num2) + " = " + str(answer)
def Mult():
    answer = num1 * num2
    print "\n" + str(num1) + " * " + str(num2) + " = " + str(answer)

ops = input("Please select an operation (add, subtract, multiply): ")

if(ops != "add" and ops != "subtract" and ops != "multiply"):
    print("\nInvalid operation!")
else:
    if(ops == "add"):
        Add()
    elif(ops == "subtract"):
        Sub()
    else:
        Mult()