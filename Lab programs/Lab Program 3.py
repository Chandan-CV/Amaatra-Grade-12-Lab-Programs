# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 15/6/21
#Write a Program to print even and odd numbers between certain limits

def print_numbers(lower_limit,upper_limit):
    
    print("Even numbers:")
    for x in range(lower_limit,upper_limit):
        if x%2 == 0:
            print(x)
    
    print("Odd numbers:")
    for x in range(lower_limit,upper_limit):
        if x%2 != 0:
            print(x)

upper_limit=int(input("Enter upper limit:"))
lower_limit=int(input("Enter lower limit:"))
print_numbers(lower_limit,upper_limit)