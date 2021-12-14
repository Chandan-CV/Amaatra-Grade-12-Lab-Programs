# Create a binary file with name and roll number. Search for
# a given roll number and display the name, if not found
# display appropriate message.
import pickle

f = open("practical programs/pg4/file.dat", "rb+")
record = [["Harry Potter", 18601741], ["Elon musk",123456789] , ["Mark Zuck",420000] ,["Fevicol",10]]

pickle.dump(record, f)
while True:
    f.seek(0)
    r = int(input("enter the roll number you want to search"))
    notfound = True
    for a in pickle.load(f):
        if (a[1] == r ):
            print(a[0])
            notfound= False
    if(notfound):
        print("the given roll number does not exist")

