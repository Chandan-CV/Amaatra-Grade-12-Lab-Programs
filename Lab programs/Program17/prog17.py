#wap to show all the functions of read
#Name:
#Date of exceution:
#Grade:
f = open("Lab programs/Program17/text.txt","r")
print(f.name)

print(f.read())

f.seek(0)
print(f.readline())

f.seek(0)
print(f.readlines())

f.seek(0)
print(f.read(1))

f.seek(0)
for x in f:
    print(x,end = "")
print()
print(f.tell())