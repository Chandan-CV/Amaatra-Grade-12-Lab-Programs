# 2 . WAP to find if a no. is odd or even. 

def check(n):
    if n%2==0:
        return "even"
    else :
        return "odd"
n = int(input("enter the number"))
print (n,"is",check(n))