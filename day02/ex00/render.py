import sys
import os
import re
import settings



def starto():
	args = sys.argv
	if len(args) != 2:
		print("Error")
		return
	if not os.path.exists(args[1]):
		print("Error")
		return
	if not os.path.isfile(args[1]):
		print("Error")
		return
	if not args[1].endswith(".template"):
		print("Error")
		return
	with open(args[1], "r") as f:
		data = f.read()
	data = re.sub("{" + "name" + "}", settings.name, data)
	print(data)

if __name__ == "__main__":
	starto()

