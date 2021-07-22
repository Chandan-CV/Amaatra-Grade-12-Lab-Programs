f = open("Class Illustrations/seekFunction/TextFile.txt","rb")
print(f.tell()) #0
f.seek(3) 
print(f.read(5))  #come
print("current postition:",f.tell())  #8
f.seek(2,1)
print(f.read(5)) #amaa
print("current position",f.tell()) #15
