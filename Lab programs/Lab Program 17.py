# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to read data from a file and show the various file functions.

f=open("abc.txt","r")
print(f.name)

f_contents=f.read()
print(f_contents)

f_contents=f.readline()
print(f_contents)

f_contents=f.readlines()
print(f_contents)

f_contents=f.read(5)
print(f_contents)

for line in f:
    print(line,end="")

print(f.tell())



