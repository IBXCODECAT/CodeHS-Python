"""
This program visualizes nested for loops by printing number 0 through 3
and then 0 through 3 for the nested loop.
"""

for i in range(4):
    print "Outer for loop: " + str(i)
    for j in range(4):
        print "    Inner for loop: " + str(j)