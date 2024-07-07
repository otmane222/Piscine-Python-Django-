

class Intern():
	def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
		self.name = name

	def __str__(self):
		return f"{self.name}"

	class Coffee():
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I'm just an intern, I can't do that...")

	def make_coffee(self):
		return self.Coffee()

def starto():
	diib = Intern()
	Mark = Intern("Mark")

	print(diib.name)
	print(Mark.name)
	print(Mark.make_coffee())
	print(diib.make_coffee())
	

if __name__ == "__main__":
	starto()