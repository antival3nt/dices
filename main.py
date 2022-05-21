# This program will let you choose between 1 or 2 dices
# Depending on the input the dices will roll a random number between 1-6 or 1-12

# Libraries
import sys
import random

# Vars

# Functions
def random_numDice():
	num = random.randint(1, 6)
	print("Rolling with one dice\n")
	print("Your roll is: " + str(num))
	return

def random_numDices():
	num = random.randint(2, 12)
	print("Rolling with 2 dices\n")
	print("Your roll is: " + str(num))
	return


diceChoice = input("Choose between 1 or 2 dices: ")

if diceChoice == '1':
	random_numDice()
elif diceChoice == '2':
	random_numDices()
else:
	print("Nice try, not gonna work... Exitting...")
	sys.exit(0)
