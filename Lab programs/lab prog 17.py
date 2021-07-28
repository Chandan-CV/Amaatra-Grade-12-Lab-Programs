#wap to read data from a text file and show file handling functions
#july 27
f=open("lab.txt",'r')
print(f.name)
fcontents=f.read()
print(fcontents)
fcontents=f.readlines()
print(fcontents)
fcontents=f.readline()
print(fcontents)
for line in f:
    print(line,end=' ')

fcontents=f.read(5)
print(fcontents)
print(f.tell())
