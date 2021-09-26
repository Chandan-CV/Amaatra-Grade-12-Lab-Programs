# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to read data from a file and show the various file functions.

f=open("Text Files/Lab Program 17/Lab Program 17.txt","r")
print(f.name)

print(f.read())

f.seek(0)
print(f.readline())

f.seek(0)
print(f.readlines())

f.seek(0)
print(f.read(1))

f.seek(0)
for x in f:
    print(x,end = "")
print()
print(f.tell())



