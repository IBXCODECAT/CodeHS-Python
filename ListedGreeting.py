info = input("Enter name, age, sport: ")

info = list(info.split())

print "Hello, " + "".join(info[0]) + "! I also enjoy " + "".join(info[2]) + "!"