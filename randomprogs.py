fo = open("data.txt",'w+')
print ("Name of the file: ", fo.name)
# Assuming that the file contains these lines
# TechBeamers
# Hello Viewers!!
seq="TechBeamers\nHello Viewers!!"
fo.writelines(seq )
fo.seek(0,0)
for line in fo:
    print("brrr")
    print (line)
fo.close()