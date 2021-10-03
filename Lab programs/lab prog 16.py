#WAP to read the contents of a file and replace all space characters with #
#Name:
#Date of exceution:
#Grade:
#27 july
f=open("demo.txt","r")
n=" "
while n:
    n=f.readline()
    for i in n.split():
        print(i,end='#' )
    print()