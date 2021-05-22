# You can also nest for loops with
# while loops. Check it out!

for i in range(4):
    print "For loop: " + str(i)
    x = i
    while x >= 0:
        print "    While loop: " + str(x)
        x = x - 1