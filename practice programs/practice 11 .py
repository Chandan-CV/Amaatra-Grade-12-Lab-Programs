#WAP to remove all odd numbers from the given list
def pract():
    L=[2,3,55,67,89,23,56,78]
    for i in L:
        if i%2!=0:
            L.remove(i)
    print(L)

pract()