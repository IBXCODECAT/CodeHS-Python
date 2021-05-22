"""
This program asks for the test scores for multiple people, and reports the average
test score for each person.
"""

# Try changing these, and see what happens!
num_people = 3
tests_per_person = 3

# For each person, get name and test scores
for i in range(num_people):
    name = input("Enter name: ")
    sum = 0
    
    # Add up the test scores
    for j in range(tests_per_person):
        score = int(input("Enter a score: "))
        sum = sum + score
        
    # Calculate and print average score
    average = float(sum) / tests_per_person
    print "Average for " + name + ": " + str(average)