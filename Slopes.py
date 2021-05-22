coords, NUMCOORDS = [], 5

for i in range(NUMCOORDS): #For each coord...
    while(True): #Always do the following
        try: coords.append(tuple((int(input(str(i + 1) + '. Enter \'x\'>>>')), int(input(str(i + 1) + '. Enter \'y\'>>>'))))) #Get and convert input to tuple
        except ValueError: continue #If exception occurs, try again!
        break #Otherwise, breakout of loop

   
for k in range(len(coords) - 1):
    x1, x2 = coords[k][0], coords[k + 1][0]
    y1, y2 = coords[k][1], coords[k + 1][1]
    
    
    if(x1 - x2 == 0):
        print 'Undefined slope'
    else:
        result = float(y2 - y1) / (x2 - x1)
        print 'Slope between ' + str(coords[k]) + ' and ' + str(coords[k + 1]) + ' is ' + "{:.2f}".format(result)