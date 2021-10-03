#Remove all the lines that contain the character 'a' in a file and write it to another file.
#july 27
#Name:
#Date of exceution:
#Grade:
fo=open("lab.txt","w")
fo.write("hi lithika ")
fo.write ("\na, an and the articles")
fo.write("\nlithi you are studying at the amaatra academy")
fo.close()
fo=open("lab.txt","r")
fi=open("demo.txt",'w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        fi.writelines("")
    else:
        fi.write(i)
fi.close()
fo.close()