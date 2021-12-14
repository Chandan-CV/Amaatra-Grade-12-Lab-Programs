# Remove all the lines that contain the character 'a' in a file
# and write it to another file.

f = open("practical programs/pg3/file.txt")

f2 = open("practical programs/pg3/targetfile.txt","w")
a = f.readlines()
af=[]
for x in range(0,len(a)):
    if ("a" not in a[x]):
        af.append(a[x])
            
f2.writelines(af)



