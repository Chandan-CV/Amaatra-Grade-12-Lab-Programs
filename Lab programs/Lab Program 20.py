# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to remove the letter 'a' in a file and write it to another file.

f=open("abc.txt","r")
readlist=f.readlines()
#print(readlist)

def func(readlist):
    newlist=readlist
    for x in readlist:
        if "a" in x.lower():
            newlist.remove(x)
    return newlist
newlist=func(readlist)

fw=open("abc2.txt","w")
fw.writelines(newlist)

    

