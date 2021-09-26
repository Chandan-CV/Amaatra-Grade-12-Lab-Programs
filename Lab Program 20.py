# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to remove the lines with the letter 'a' in a file and write it to another file.

f=open("Text Files/Lab Program 20/input.txt","r")
readlist=f.readlines()

def func(readlist):
    newlist=[]
    for x in readlist:
        if "a" not in x.lower():
            newlist.append(x)
    return newlist
newlist=func(readlist)

fw=open("Text Files/Lab Program 20/output.txt","w")
fw.writelines(newlist)

    

