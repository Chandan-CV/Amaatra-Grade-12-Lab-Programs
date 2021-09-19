# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to count the number of characters in a file
f=open("abc.txt","r")
string=f.read()
string.strip()
count=len(string)

if len(string) == 0:
    print("The text file is empty.")
else:
    print(f"The number of characters in the text file are {count}.")
    

