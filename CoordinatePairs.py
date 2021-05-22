import math

def distance(first_point, second_point):
    sqx = (first_point[0] - second_point[0]) ** 2
    sqy = (first_point[1] - second_point[1]) ** 2
    
    expTot = sqx + sqy
    
    return math.sqrt(expTot)


# This should print 5.0
print distance((1, 1), (4, 5))