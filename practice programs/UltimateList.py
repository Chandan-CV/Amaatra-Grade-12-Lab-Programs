# negative to left and positive to right
# in =[-12, 11,-13,-5,6,-7]
#  out = [11,6,-7,-5,-13,-12]
l = list(map(int,input("enter the list").split()))

def pos():
    pos=[]
    neg=[]
    for x in l:
        if (x>=0) :
            pos.append(x)
        else:
            neg.append(x)
    neg.reverse()
    return pos+neg
print (pos())
   