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
	split_parts = sys.argv[1].split(',')

	processed_parts = []
	for part in split_parts:
		part = part.strip()

		if part:
			processed_parts.append(part)
	
	for dada in processed_parts:
		varoo = False
		capital = ""
		state = ""
		for key in states.keys():
			if key.lower() == dada.lower():
				varoo = True
				state = key
				capital = capital_cities[states[key]]
		for value in capital_cities.values():
			if value.lower() == dada.lower():
				for varo in capital_cities.values():
					if varo == value:
						for keyo in capital_cities.keys():
							if capital_cities[keyo] == varo:
								for kako in states.keys():
									if states[kako] == keyo:
										varoo = True
										state = kako
										capital = value
		if varoo:
			print(capital, "is the capital of", state)
		else:
			print(dada, "is neither a capital city nor a state")

if __name__ == "__main__":
	starto()
