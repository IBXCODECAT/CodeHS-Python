"""
This program shows how changing an outside variable from within a function
makes another variable!

In this program, print_something has its own variable called z. It can no longer
access the outer variable called z.
"""

z = 6.5

def print_something():
    z = "hi"
    print z * 3

print_something()

print z * 3