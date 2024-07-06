import sys

def check_exist(states, state):
	for state in states.values():
		if state == sys.argv[1]:
			for key in states.keys():
				if states[key] == state:
					return key
	return False

def starto():
	if len(sys.argv) != 2:
		return
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	varo = check_exist(capital_cities, sys.argv[1])
	if (varo != False):
		for key in states.keys():
			if states[key] == varo:
				print(key)
	else:
		print("Unknown state")

if __name__ == '__main__':
	starto()