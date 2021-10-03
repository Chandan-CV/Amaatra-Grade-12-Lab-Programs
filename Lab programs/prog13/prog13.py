# count the number of vovels in the text file
#Name:
#Date of exceution:
#Grade:
f =open("Lab programs/prog13/progText.txt","r")

s = f.read()
def countVovels(s):
    s= s.lower()
    count =0
    for ch in s:
        if (ch=="a" or ch=="e"or ch=="i" or ch=="o" or ch=="u"):
                count+=1
    return count
print("number of vovels= ", countVovels(s))
