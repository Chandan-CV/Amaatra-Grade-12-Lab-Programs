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