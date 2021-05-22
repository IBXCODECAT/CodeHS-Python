total = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))

for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    total = total + next

print("Sum: " + str(total))