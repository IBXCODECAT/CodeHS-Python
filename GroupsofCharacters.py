"""
This program shows how index values are assigned and utilized to isolate
multiple characters in a string.
"""

# indices:           0   1   2   3   4   5   6   7   8   9  10  11
#                    h   e   l   l   o       w   o   r   l   d   !
# negative indices: -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
my_string = "hello world!"

print "my_string[1:3] is " + my_string[1:3]
print "my_string[1:] is " + my_string[1:]
print "my_string[:3] is " + my_string[:3]

print my_string[3:5] + my_string[2] + my_string[5:9] + my_string[-2:]