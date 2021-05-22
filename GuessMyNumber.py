"""
This program repeatedly asks a user to guess a number. The program ends
when they're guessed correctly.
"""

# Secret number
my_number = 10

# Ask the user to guess
guess = int(input("Enter a guess: "))

# Keep asking until the guess becomes equal to the secret number
while guess != my_number:
    print "Guess again!"
    guess = int(input("Enter a guess: "))

print "Good job, you got it!"