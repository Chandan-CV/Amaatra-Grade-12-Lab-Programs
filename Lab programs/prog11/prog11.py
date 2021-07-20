# Wap to accept count the number of alphabets in story.txt

f = open("Lab programs/prog11/story.txt","r")# I use linux, so I use / if you use windows, use \
s = f.read() 
s =s.replace("\n","")
def count(s):
    s= str(s)
    count =0
    for ch in s:
        if (ch.isalpha()):
            count+=1
    return count
print(count(s))
