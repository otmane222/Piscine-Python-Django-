import sys

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
	if sys.argv[1] in states:
		print(capital_cities[states[sys.argv[1]]])
	else:
		print("Unknown state")

if __name__ == "__main__":
	starto()