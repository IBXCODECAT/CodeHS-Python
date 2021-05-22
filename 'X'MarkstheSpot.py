# increase the speed of the turtle (I hate waiting)
speed(5)

#setup
left(45)

for x in range(4):
    '''
    # the toatal length of the X must be 200 pixels
    # so the length of each prong must be 200 / 2
    # because there is two prongs that make up the
    # diamitor of the x
    '''
    
    forward(200 / 2)
    backward(200 / 2)
    
    # left 90 to make next prong
    left(90)