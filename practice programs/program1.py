#Wap to compute x^n of given 2 integers , using user defined functions


def calc (x,n):
    return x**n

x= int(input("enter the value of x"))
n= int(input("enter the value of n"))
print (x,"^",n,"=",calc(x,n))

