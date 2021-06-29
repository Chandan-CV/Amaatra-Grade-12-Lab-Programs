
# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 15/6/21
#Write a Program to perform all arithmetic operations on 2 numbers

def arithmetic(a,b):
    sum= a+b
    product= a*b
    difference= a-b
    quotient= a/b
    remainder= a%b
    return sum, product, difference, quotient, remainder
 
a= int(input("Enter number 1:"))
b= int(input("Enter number 2:"))
sum,product,difference,quotient,remainder=arithmetic(a,b)
print("Sum:",sum,"\nProduct:",product,"\nDifference:",difference,"\nQuotient:",quotient,"\nRemainder:",remainder)