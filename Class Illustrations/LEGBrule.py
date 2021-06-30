# LEGB
# L -> local 
# E -> Enclosed 
# G -> Global
# B -> built-in
from math import pi
import math

pi =" Hiii! this is the global pi"

def fun1():
    pi = "this is the enclosed pi"
    def nestedfun():
        pi ="this is the local pi"
        print(pi)
    #   running nonlocal pi will assign pi's value to the enclosed pi
    #   running glbal pi will assign pi's value to the global pi
    nestedfun() # calling the inner function
    print(pi)
fun1() # calling the outer function
print(pi) # this will print the global pi
print(math.pi) # this will print the built in pi



