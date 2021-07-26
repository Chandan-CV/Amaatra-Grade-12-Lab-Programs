#wap to display second largest element of a given list
def prac():
    L=[41,6,9,13,4,23,12]
    m=max(L)
    secmax=min(L)
    for i in range(0,len(L)):
        if L[i]>secmax and L[i]<m:
            secmax=L[i]
    print(secmax)

prac()