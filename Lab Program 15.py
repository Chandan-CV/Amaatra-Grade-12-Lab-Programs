# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to print the words starting with "a"
f=open("Text Files/Lab Program 15/Lab Program 15.txt","r")
count=0
for x in f.read().split():
    if x[0] in ["a","A"]:
        print(x)
        count+=1
print("Number of words starting from A are:",count)

    

