# wap to count the number of words in the text file.
#Name:
#Date of exceution:
#Grade:
f = open("Lab programs/prog14/textFIle.txt","r")
s = f.read()
def countWords(s):
    s =str(s)
    l = s.split()
    return len(l) 
print("the number of words is", countWords(s))