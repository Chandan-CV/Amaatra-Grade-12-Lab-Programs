# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program which returns frequency of all elements in a list.

def func():
    L=[3,21,5,6,3,8,21,6]
    d={}
    for i in L:
        if i not in d:
            d[i]=L.count(i)
    print("Count for each elment is:")
    for x in d:
        print(" ", x ,":",d[x])
func()
