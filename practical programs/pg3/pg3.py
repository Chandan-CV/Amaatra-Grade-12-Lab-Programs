# Remove all the lines that contain the character 'a' in a file
# and write it to another file.

f = open("practical programs/pg3/file.txt", "r+")

f2 = open("practical programs/pg3/targetfile.txt","w")
a = f.readlines()
a1=a
af=[]
for x in range(0,len(a)):
    if ("a" in a[x]):         
        af.append(a[x])
        a1[x]=""             # replaces 'a' with empty string
f.seek(0)
f2.writelines(af)
f = open("practical programs/pg3/file.txt", "w")
f.writelines(a1)           # writes edited text on original string



