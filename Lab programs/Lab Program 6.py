# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to check if an inputted number is a perfect number
#Perfect numbers are numbers whose sum of multiples (excluding itself) is the number. Example: 6

n = int(input("enter the number"))
sum=0

def func():
    global sum
    for x in range(1,n):
        if (n%x==0):
            sum+=x
    print ("sum =", sum)

func()
if (sum == n):
    print("its a super Perfect number")
else:
    print("its not a super number")