#wap to read and display contents of marks.dat


f= open("marks.dat", 'r')
while str:
    str= f.readline()
    print(str)
f.close()