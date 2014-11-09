#! usr/bin/env python

import random
import specialInput

print("This program simulates rolling several dice.\nThe user can choose how many dice are rolled")

# Asking the user to input how many dices they would like to use

dice = specialInput.int_input("How many dice would you like to roll? ")

for i in range(1, dice+1):
	sides = specialInput.int_input("How many sides on dice #{}?".format(i))
	if sides <= 2:
		print("Each die has at least two sides")
		break
	elif sides > 2:
		number = random.randint(1, sides+1)
	else:
		print("Sorry dude, I think you made a mistake")
	print("Dice" + " " + str(i) + " shows: " + str(number))
	
	