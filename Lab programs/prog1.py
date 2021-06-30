# 1wap to calc (a+b) or (a-b)^3 using user defined function. ask the choice from the user

def neg():
    a= int(input("enter the first number"))
    b= int(input("enter the first number"))
    print ("result =" , a**3 - (3*(a**2)*b) + (3*a*(b**2)) - b**3)
def pos():
    a= int(input("enter the first number"))
    b= int(input("enter the first number"))
    print ("result =" , a**3 + (3*(a**2)*b) + (3*a*(b**2)) + b**3)

choice = int (input ("enter 1 for (a-b)^3 \n  enter 2 for (a+b)^3"))
if (choice==1):
    neg()
else:
    pos()

