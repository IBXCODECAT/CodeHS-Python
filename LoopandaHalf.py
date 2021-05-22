"""
This program continually asks a user to guess a number until they have guessed
the magic number.
"""

magic_number = 10

# Ask use to enter a number until they guess correctly
# When they guess the right answer, break out of loop
while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print "You got it!"
        break
    print "Try again!"

# Print this sentence once number has been guessed
print "Great job guessing my number!"