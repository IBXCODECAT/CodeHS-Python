"""
This program asks a user for the size of their bike frame and determines
if the size fits into the available constraints.
"""
# Continue asking user for a bike frame size until the size fits into constraints
while True:
    bike_frame_size = int(input("Enter bike frame size, in cm: "))
    if bike_frame_size > 60:
        print "That bike is too big!"
    elif bike_frame_size < 55:
        print "That bike is too small!"
    else:
        print "That bike is the right size!"
        break

print "Hooray, I found a bike."