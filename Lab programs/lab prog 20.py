#wap to read a particular data from text file and count the occurance of a partiular word 
#july27
f=open("abc.txt",'r')
read=f.readlines()
f.close()
t=0
t1=0
s=input("enter the word to be searched ")
c=0
for sentence in read:
    line=sentence.spilt()
    t+=1
for each in line:
    line2=each
    t1+=1
    if s==line2:
        c=c+1

print("\n the occurance of string=", c)
