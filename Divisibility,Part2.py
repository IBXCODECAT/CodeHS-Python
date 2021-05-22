numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

# If denominator is 0, this will result in a division-
# by-zero error! Add in code to solve this issue:

try:
    if(numerator / denominator * denominator == numerator):
        print "Divides evenly!"
    else:
        print "Doesn't divide evenly."
except:
    print "ZeroDivisionError Exception"