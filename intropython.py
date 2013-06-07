""" Variables """
x = "hi"
print x

""" Functions """
def print_arg(a):
	print a

print_arg(x)

""" Lists """
x = ["hi", "whatup", "bye"]
print x[0]

""" Conditionals """
def findGoodTeams(s):
	if s == "Yankees":
		print "keep looking"
	if s == "Red Sox":
		print "found it"
findGoodTeams("Red Sox")

""" For loops """
def findGoodTeams(teams):
	for team in teams:
		if team == "Yankees":
			print "keep looking"
		if team == "Red Sox":
			print "found it"
baseball_teams = ["Yankees", "Red Sox"]
findGoodTeams(baseball_teams)