# fibonacci series
#0 1 1 2 3 5 8 
def fibo (n):
    a=0
    b=1
    for x in range(n):
        c=a+b
        print(a, end=" ")
        a=b
        b=c
n = int(input("enter the range")) 
fibo(n)
