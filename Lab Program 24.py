# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 26/8/21
#A binary file book.dat has structure ["Book No, Book_name, Author, Price"]
# Write a user defined function to input and add records.
# Count no of nooks by the given author. MAke a user defined function called count() that accepts the author and returns the count

import pickle
def createfile():
    f = open("book.dat","ab")
    BookNo = int (input("Book no:"))
    BookName = input("Book name:")
    Author = input("Authour name:")
    Price = int(input("Book price:"))
    rec = [BookNo,BookName,Author,Price]
    pickle.dump(rec,f)
    f.close()

def count(Authour):
    f = open("book.dat","rb")
    num = 0
    try:
        while True:
            rec = pickle.load(f)
            if Authour == rec[2]:
                num += 1
                for x in rec:
                    print(x)
            
    except:
        print("No file")
    print("Total number of books:",num)

def main():
    more_entries = True
    while more_entries:
        createfile()
        if ask_if_more_entries():
            pass
        else:
            break
        def ask_if_more_entries():
            question = input("Do you want to continue? (Y/N)")
            if question == "Y":
                return True
            elif question == "N":
                return False
            else:
                print("You entered a invalid response. You can only enter in Y or N. Have another chance.")
                ans = ask_if_more_entries()
                return ans
    Authour = input("Enter the Authour's name whose book count I need to find:")
    count(Authour)
main()





