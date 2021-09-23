# Name: LITHIKA RAMESH
# Class:12
# Date of executiom: 27/7/21
# Write a Program to count the occurence of a particular word

f=open("abc.txt","r")
read=f.read()

def func(read):
    word=str(input("Enter the word to find the occurence of:"))
    count=read.count(word)
    print("The number of times that this word has been used is:",count)

func(read)
    
