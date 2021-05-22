"""
This code will print out a greeting based on the time of day.
"""

# This function will print a greeting for the morning
def morning_greeting():
    print "Good morning! It will be a lovely day!"
    
# This function will print a greeting for the afternoon
def afternoon_greeting():
    print "Good afternoon! I hope you are having a lovely day!"
    
# This function will print a greeting for the evening
def evening_greeting():
    print "Good evening! I hope you had a lovely day!"
    

# Get input from the user and print matching greeting
# If other option, print that it is invalid
time_of_day = input("What time of day is it? (morning, afternoon, evening): ")

if time_of_day == "morning":
    morning_greeting()
elif time_of_day == "afternoon":
    afternoon_greeting()
elif time_of_day == "evening":
    evening_greeting()
else:
    print "Invalid option."