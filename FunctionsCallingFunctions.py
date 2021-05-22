# A function can call another function!

def add_two(x):
    return x + 2

def multiply_by_three(x):
    return x * 3

def my_function(x):
    return add_two(x) + multiply_by_three(x)

print my_function(12)