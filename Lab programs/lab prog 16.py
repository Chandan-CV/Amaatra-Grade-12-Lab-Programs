#WAP to read the contents of a file and replace all space characters with #
#27 july
f=open("demo.txt","r")
n=" "
while n:
    n=f.readline()
    for i in n.split():
        print(i,end='#' )
    print()