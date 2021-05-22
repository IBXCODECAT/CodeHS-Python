"""
This program simulates a single transaction -
either a deposit or a withdrawal - at a bank.
"""

money = 1000

mode = input("deposit or withdrawl: ")

if mode == "deposit":
    deposit_amount = int(input("Enter amount: "))
    money = money + deposit_amount
        
    print("")
    print("final: " + str(money))
    print("")

elif mode == "withdrawl":
    withdraw_amount = int(input("Please enter the amount: "))
    if withdraw_amount > 1000:
        print("You cannot have a negative balance!")
    else:
        money = money - withdraw_amount
        print("")
        print("final: " + str(money))
        print("")
else:
    print("Invalid Transaction!")