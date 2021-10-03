# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
# Write a random number generator for a dice
import random 
def roll_dice():
    randomNumber = random.randint(1,6)
    return randomNumber
    
    
while True:
    n = input("Enter \"Y\" to run the dice or \"N\" to exit.")
    if n in ["Y","y"]:
        randomNumber = roll_dice()
        print("Your number is",randomNumber)
    elif n in ["N","n"]:
        break