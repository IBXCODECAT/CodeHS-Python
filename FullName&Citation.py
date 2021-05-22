firstName = input('Enter your first name>>>').strip()
lastName = input('Enter your last name>>>').strip()

print "FUll name: " + firstName + ' ' + lastName

firstName, lastName = lastName, firstName

print "Citation: " + firstName + ', ' + lastName