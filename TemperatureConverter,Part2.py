# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!


def F2C(temp):
    try:
        return (1.8 * temp) + 32
    except:
        print "ValueError"
def C2F(temp):
    try:
        return (temp - 32) / 1.8
    except:
        print "ValueError"

# Now write your function for converting Fahrenheit to Celsius.




# Now change 0C to F:
print C2F("farglebartgle")

# Change 100C to F:
print C2F(100)

# Change 40F to C:
print F2C(30)

# Change 80F to C:
print F2C(80)