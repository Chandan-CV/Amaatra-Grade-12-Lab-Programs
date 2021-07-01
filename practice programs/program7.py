# 7. WAP to print the sum of series 1+ x/1! + x^2/2!+...........+ x^n/n! 

def fact(n):
    if(n==0):
        return 1 
    else:
        fact = 1
        for i in range (1,n+1):
            fact= fact*i
        return fact

x = int(input("enter the number"))
n= int(input("enter the range"))
sum =0
for i in range(n+1):
    sum += x**i/fact(i)
print(sum)
    

