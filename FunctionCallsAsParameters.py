# The return value of one function can be used as the parameter of another. This
# is called function composition.

def add_two(x):
    return x + 2

def multiply_by_three(x):
    return x * 3

def my_function(x):
    return add_two(multiply_by_three(x))

print my_function(5)