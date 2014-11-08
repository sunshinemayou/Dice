#! usr/bin/env python

import random
import specialInput
"""
	Asking the user to input how many dices they would like to use
"""
dice = specialInput.int_input("How many dice would you like to roll? ")

for i in range(1, dice+1):
	"""
		Asking the user to input the sides of each dice
	"""
	sides = specialInput.int_input("How many sides on dice #{}?".format(i))
	if sides <= 2:
		print("Each die has at least two sides")
		break
	elif sides > 2:
		number = random.randint(1, sides+1)
	else:
		"""
			If you see this sentence, it means that you have made a mistake when inputting the side of this dice
		"""	
		print("Sorry dude, I think you made a mistake")
		"""
			This is an output language
		"""
	print("Dice" + " " + str(i) + " shows: " + str(number))
	
	