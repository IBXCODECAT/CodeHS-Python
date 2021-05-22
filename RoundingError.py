x = 0.0037 / 100
y = 0.000037

# These numbers look equal!
print x
print y

# ... But they aren't exactly equal!
if x == y:
    print "Equal!"
else:
    print "Unequal!"

# ... But they are approximately equal (to five decimal places)!
if round(x, 5) == round(y, 5):
    print "Approximately equal!"
else:
    print "Not approximately equal!"