# wap to remove all the odd numbers from the list

def remOdd(l): 
    i =0
    while (i<len(l)):
        if (l[i]%2!=0):
           l.pop(i)
        else:
            i+=1
    return l
print(remOdd([1,2,3,5,7,9,19,13,100,333,54,5,18,28]))
