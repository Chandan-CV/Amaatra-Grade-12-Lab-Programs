#WAP to interchange the consecutive elements of an array eg [1,2,3,4] should become [2,1,4,3]
#Name: Chandan
#Date of excecution: June 29, 2021
#Grade: 12
def fun(A):
    l=len(A)
    for i in range(0,l,2):
        tmp=A[i]
        A[i]=A[i+1]
        A[i+1]=tmp
    print(A)

A=eval(input("Enter a list: "))
if(len(A)%2==0):
    fun(A)