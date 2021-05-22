magic_number = 3

while True:
    x = int(input("guess a number: "))
    
    if(x == magic_number):
        print "Correct!"    
        break
    
    if(x > magic_number):
        print "Too High!"
        continue
    else:
        print "Too Low!"
        continue
    
        
    print "Try Again!"