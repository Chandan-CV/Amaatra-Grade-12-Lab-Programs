f = open("Class Illustrations/seekFunction/TextFile.txt","rw")
print(f.tell())
f.seek(0)
print(f.read(3))
print(f.tell())