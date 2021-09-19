# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program to count the total number of alphabets in that string.


def count_alpha():
    count=0
    f=open(r"Text Files/Lab Program 11/story.txt","r")
    content = f.read()
    for letter in content:
        if letter.isalpha():
            count=count+1
    print("Total Alphabets = ",count)

count_alpha()