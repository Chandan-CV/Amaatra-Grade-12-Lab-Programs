# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 15/6/21
# Write a Program to accept two strings and concatenate them using user-defined functions.

def join(a,b):
    c= a+b
    return c

a=str(input("Eneter the first String:"))
b=str(input("Enter the second String:"))
c=join(a,b)
print("Concatenated string is:",c)