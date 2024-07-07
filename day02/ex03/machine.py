

import random
import beverages


class CoffeeMachine:
	def __init__(self):
		self.water_level = 100
		self.beans_level = 100
		self.cups = 100
	
	class EmptyCup(beverages.HotBeverage):
		name = "empty cup"
		price = 0.90
		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			return super().__init__("This coffee machine has to be repaired.") # ?
		
	def repair(self):
		self.water_level = 100
		self.beans_level = 100
		self.cups = 10
		print("The coffee machine has been repaired.")
	
	def serve(self, beverage):
		if self.water_level < 10:
			raise self.BrokenMachineException()
		if self.beans_level < 5:
			raise self.BrokenMachineException()
		if self.cups < 1:
			raise self.BrokenMachineException()
		
		self.water_level -= 10
		self.beans_level -= 5
		self.cups -= 1
		
		if random.randint(0, 1):
			return beverage()
		else:
			return self.EmptyCup()
		

if __name__ == "__main__":
	try:
		machine = CoffeeMachine()
		print(machine.serve(beverages.Coffee))
		print()
		print(machine.serve(beverages.Tea))
		print()
		print(machine.serve(beverages.Chocolate))
	except CoffeeMachine.BrokenMachineException as e:
		print()
		print(e)
		machine.repair()
		print(machine.serve(beverages.Coffee))
		print(machine.serve(beverages.Tea))
	except Exception as e:
		print(e)