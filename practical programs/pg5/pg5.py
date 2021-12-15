# Create a binary file with roll number, name and marks.
# Input a roll number and update the marks.

from os import error
import pickle
f =open("practical programs/pg5/data.dat", "rb+")

def addData():
    rec =[]
    while (True):
        rn= int(input("enter the roll number"))
        name = input("enter the name of the student")
        marks = int(input("enter the marks of the student"))
        rec.append([rn, name, marks])
        if(input("do you want to add more? Y/N") in ["N",'n']):
            break
    print("writing data...")
    try:
        pickle.dump(rec,f)
    except:
        print("oops something went wrong")
    print("data written on the file!")

def search(rn):
    f.seek(0)
    a = pickle.load(f)
    for x in a:
        if (x[0] == rn):
            return x
    f.seek(0)

def modify():
    while True:
        f.seek(0)
        data = pickle.load(f)
        f.seek(0)
        rn = int(input("enter the roll number to be modified"))
        a = search(rn)
        a2 = eval(input(("please enter what you want to modify {} to").format(a)))
        data.remove(a)
        print(data)
        data.append(a2)
        print(data)
        print("writing data...")
        try:
            f.seek(0)
            pickle.dump(data,f)
        except(error):
            print("oops. something went wrong")
            print(error)
        if (input("do you want to modify more? Y/N") not in ["Y,y"]):
                break

addData()
f.seek(0)
print(pickle.load(f))
modify()
f.seek(0)
print(pickle.load(f))





