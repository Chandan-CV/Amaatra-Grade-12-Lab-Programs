# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 15/6/21
#Write a Program to accept a positive number and find square, cube and root
def function(a):
    square=a**2
    cube=a**3
    root=a**1/2
    return square,cube,root
a=int(input("Enter the number:"))
square,cube,root=function(a=a)
print("Square:",square,"Cube:",cube,"Square Root:",root)