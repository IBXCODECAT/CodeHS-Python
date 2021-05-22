"""
This program determines if Yelena can clear the bar in the high jump event
"""

# Set the bar
height_of_bar = 1.9
print "The bar is " + str(height_of_bar) + " meters off the ground."

# Yelena jumps!
yelena_jump = 2.0
print "Yelena's jump: " + str(yelena_jump) + " meters."
if yelena_jump > height_of_bar:
    print "Yelena cleared the bar!"
else:
    print "Yelena didn't clear the bar."