"""
This program determines if a rider reaches the height requirement for the
roller coaster.
"""

height = 5.5
height_requirement = 5.0

# You must be at least 5.0 feet tall to ride the roller coaster.
can_ride_roller_coaster = height >= height_requirement

if can_ride_roller_coaster:
    print "You are tall enough to ride this roller coaster!"
else:
    print "Sorry, you aren't tall enough."