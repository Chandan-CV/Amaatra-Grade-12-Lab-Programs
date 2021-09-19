# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
# Write a random number generator for a dice
import random 
def roll_dice():
    counter = 0
    myList = []
    while(counter<=6):
        randomNumber = random.randint(1,6)
        myList.append(randomNumber)
        if counter > 6 : 
            pass
        else:
            return myList
    
n= 1
while (n == 1):
    n = int(input("Enter 1 to run the dice"))
    if n == 1:
        roll_dice()