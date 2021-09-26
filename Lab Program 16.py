# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to read the contents of a file and replace all spaces with #
f=open("Text Files/Lab Program 16/input.txt","r")
string=f.read()

def replace(string):
    word=""
    for x in string:
        if x == " ":
            x="#"
        word+=x
    return word
word=replace(string)
fw=open("Text Files/Lab Program 16/output.txt","w")
fw.write(word)

    

