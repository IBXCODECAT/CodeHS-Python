# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!


def F2C(temp):
    return (1.8 * temp) + 32
    
def C2F(temp):
    return (temp - 32) / 1.8
    

# Now write your function for converting Fahrenheit to Celsius.




# Now change 0C to F:
print C2F(0)

# Change 100C to F:
print C2F(100)

# Change 40F to C:
print F2C(30)

# Change 80F to C:
print F2C(80)