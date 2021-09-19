# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to count the number of vowels in a text file

f=open("abc.txt","r")
string=f.read().lower()
count=0
for x in string:
    if x in ["a","i","e","o","u"]:
        count+=1
if len(string) == 0:
    print("The text file is empty.")
else:
    print(f"The number of vowels in the text file are {count}.")
    

