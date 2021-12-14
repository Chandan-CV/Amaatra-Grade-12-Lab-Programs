# . Read a text file line by line and display each word
# separated by a #.

f = open("practical programs/pg1/file.txt") # change / to \ if you are running the program on windows
a= f.readlines()
for x in a:
    print(x.replace(" ","#"),end="")

