# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to print the words starting with "a"
f=open("abc.txt","r")
string=f.read()
count=0
for x in string.split():
    if x[0] in ["a","A"]:
        print(x)
        count+=1
print("Number of words starting from A are:",count)

    

