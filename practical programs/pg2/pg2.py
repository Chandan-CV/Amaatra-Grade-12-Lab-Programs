# Read a text file and display the number of
# vowels/consonants/uppercase/lowercase characters in the
# file.

f = open("practical programs/pg2/file.txt") # change / to \ if you are running on windows (PS. I run Linux)
s = f.read()
vovels = ["a","e","i","o","u","A","E","I","O","U"]
v,c,u,l=0,0,0,0
for x in s:
    if (x in vovels):
        v+=1
    else:
        c+=1
    if (x.isupper()):
        u+=1
    else:
        l+=1

print("vovels =", v,"\n","consonants = ",c,"\n","Uppercase = ",u,"\n","Lowercase = ",l )

