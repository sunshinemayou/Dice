#! usr/bin/env python

import random
import specialInput
dice = specialInput.int_input("How many dice would you like to roll? ")
sides = specialInput.int_input("How many sides on your dice?")
for i in range(1, dice+1):
	number = random.randint(1, sides)
	print("dice" + str(i) + " shows " +str(number))