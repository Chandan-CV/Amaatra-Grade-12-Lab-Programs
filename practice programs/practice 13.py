# WAP to dispslay cumulative elemens
def prac():
    l=[1,3,5,7,8]
    fl=[l[0]]
    for i in range (1,len(l)):
        fl+=[fl[i-1] + l[i]]
    print(fl)

prac()