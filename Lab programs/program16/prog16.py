#WAP to read the contents of a file and replace all space characters with #
#Name:
#Date of exceution:
#Grade:
f = open("Lab programs/program16/textfile.txt","r")
s = f.read()

def rp(string):
    s= list(string) 
    for i in range(len(s)):
        if(s[i]==" "):
            s[i]= "#"

    return("".join(s))
print(rp(s))
