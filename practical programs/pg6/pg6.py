# Create a CSV file by entering user-id and password, read
# and search the password for given userid.

import csv
from os import error
f = open("practical programs/pg6/file.csv","r+")
writer = csv.writer(f)
reader = csv.reader(f)
def addData():
    rec =[]
    while True:
        uid = input("enter user id")
        pas = input("enter password")
        rec.append([uid,pas])
        if (input("do you want to enter more? Y/N") in ["N",'n']):
            break
    try:
        writer.writerows(rec)
    except(error):
        print("oops. something went wrong", error)

def search(uid):
    f.seek(0)
    for x in reader:
        if (x[0]== uid):
            return x

addData()
f.seek(0)
while True:
    uid = input("enter the user you want to search for")
    print(search(uid))
    if (input("do you want to search more? Y/N") in ["n","N"]):
        break

