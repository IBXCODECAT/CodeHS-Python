num_people = int(input("How many people are playing?: "))
num_teams = int(input("How many teams?: "))

people_per_team = num_people/ num_teams
left_over = num_people % num_teams

print "If there are " + str(num_teams) + " teams, there will be " + \
str(people_per_team) + " on each team, with " + str(left_over) + " left over."