#Write a program to create a CSV file which stores username and password
#Write contents into the file
#Read contents of the file
#Depending on the user name prinbt the password
import csv



def input_entries():
    f = open("passwords.csv","w",newline = "")
    writer = csv.writer(f)
    data = ["Username","Password"]
    writer.writerow(data)
    rec = []
    print("Inputting Entries")
    print("-----------")
    while True:
        username = input("Enter the username:")
        password = input("Enter the password:")
        data = [username,password]
        rec.append(data)
        more_entries = input("Do you want to enter more records?(Y/N)")
        if more_entries in ["N","n"]:
            break
    print("-----------")
    writer.writerows(rec)
    print("Written to the CSV file succesfully.")
    f.close()
    


def read_entries():
    f = open("passwords.csv","r")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()

def search ():
    f = open("passwords.csv","r")
    reader = csv.reader(f)
    username = input("Enter the username to be searched:")

    print(next(reader))# To skip the first row
    for i in reader:
        if i[0].lower() == username.lower():
            print(f"Password of the user,{i[0]} is: {i[1]}")
            break
    else:
        print("Username is not found.")
    f.close()
    
#input_entries()
#read_entries()
search()
