def calculate_area(side_length = 10):
    area = side_length * side_length
    print "The area of a square with sides of length " + str(side_length) + " is " + str(area)
    
size = int(input("How big is the square: "))

if(size > 0):
    calculate_area(size)
else:
    calculate_area()