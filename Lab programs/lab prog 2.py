# enter a postive number and find cube and square root of that number 
#Name:
#Date of exceution:
#Grade:
import math
def pos():
    a=int(input("enter positive number"))
    if a>=0:
         print("cube",a**3)
         print( "square root",math.sqrt(a))
    else:
        print("oops!")

   

pos()

