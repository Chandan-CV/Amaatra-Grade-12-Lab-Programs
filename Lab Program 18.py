# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to read data a text file and use it in aappend mode. Show the working of writelines()

f=open("Text Files/Lab Program 18/Lab Program 18.txt","a")
content=("\nThis is the first line.",
        "\nThis is the second line.",
        "\nThis is the third line",)

f.writelines(content)
f.close()


