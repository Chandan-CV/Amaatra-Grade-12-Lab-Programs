# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to count the number of words in a file
f=open("Text Files/Lab Program 14/Lab Program 14.txt","r")
string=f.read()
count = len(string.split())

if len(string) == 0:
    print("The text file is empty.")
else:
    print(f"The number of words in the text file are {count}.")
    

