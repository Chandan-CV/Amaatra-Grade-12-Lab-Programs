# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
# Write a Program to write roll no, name and marks of a student in a data file marks.dat

count = int(input("Number of student:"))
fileout = open("Marks.dat","a")
for i in range (count):
    print("Enter details of student",(i+1,"below"))
    rollno= int(input("Enter roll no:"))
    name = input("name")
    marks = float(input("marks"))
    rec = str(rollno) + ", " + name + ", " + str(marks) + "\n "
    fileout.write(rec)
fileout.close()