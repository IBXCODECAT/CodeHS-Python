def sunny():
    print "On a sunny day, sandals are appropriate footware."

def rainy():
    print "On a rainy day, galoshes are appropriate footware."
    
def snowy():
    print "On a snowy day, boots are appropriate footware."
    
#====================MAIN CODE==============================

weather = input("Enter the weather (sunny, rainy snowy): ")

if(weather != "sunny" and weather != "rainy" and weather != "snowy"):
    print "\n" + str(weather) + " is not a valid response. :("
else:
    if(weather == "sunny"):
        sunny()
    elif(weather == "rainy"):
        rainy()
    else:
        snowy()