# write a program to read a file, count and print the total words starting with A in the file

f = open("Lab programs/program15/textfile.txt","r")
s = f.read()
s = s.lower()
s = s.split()
def count(s):
    l =[]

    for ch in s:
        if(ch[0]=="a"):
            l.append(ch)
    return l

print("the number of words beginning with a is", len(count(s)))
print("the words are: ", str(count(s)))