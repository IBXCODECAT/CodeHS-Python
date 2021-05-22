"""
This program asks the user for three ingredients,
three amounts, and a number of servings, and
determines how much of each ingredient is needed
to serve the specified number of servings.

The names of three ingredients for a salad recipe.
The number of ounces of each ingredient required for 
one serving (these should just be floats, like 2.5).
The number of servings desired (this should be an 
integer). You should only ask for the number of 
servings once.
"""

ingredient_one = ""
ingredient_two = ""
ingredient_three = ""

ingredient_one_amount = 0
ingredient_two_amount  = 0
ingredient_three_amount = 0

for i in range(3):
        
    x = input("What is the name of ingredient number " + str(i + 1) + "? ")
    y = float(input("What is the amount of ingredient " + str(i + 1) + " (oz)? "))
    
    if i == 0:
        ingredient_one = x
        ingredient_one_amount = y
        print("0")
    elif i == 1:
        ingredient_two = x
        ingredient_two_amount = y
        print("1")
    else:
        ingredient_three = x
        ingredient_three_amount = y
        print("2")
        
s = int(input("How many servings? "))

tot1 = ingredient_one_amount * s
tot2 = ingredient_two_amount * s
tot3 = ingredient_three_amount * s

print("You will need:")
print(str(tot1) + " times the amount of " + ingredient_one)
print(str(tot2) + " times the amount of " + ingredient_two)
print(str(tot3) + " times the amount of " + ingredient_three)