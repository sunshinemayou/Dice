#! usr/bin/env python

import random
import specialInput

dice = specialInput.int_input("How many dice would you like to roll? ")

for i in range(1, dice+1):

	sides = specialInput.int_input("How many sides on dice #{}? ".format(i))
	if sides > 0:
		number = random.randint(1, sides+1)
	else:
		print("Sorry dude, I think you made a mistake")
	print("Dice" + " " + str(i) + " shows: " + str(number))
	
	
	