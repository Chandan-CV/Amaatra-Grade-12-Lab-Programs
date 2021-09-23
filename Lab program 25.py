# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21\
#Consider the following defination of a dictionary member {"member_no":_____, "member_name":_____}
#Write a program to enter the contents of this dictinary in a binary file

import pickle
f = open("test.dat","wb")
while True:
    d = {}
    no = int(input("Enter member no:"))
    name = input ("Enter name")
    d["member_no"] = no
    d["member_name"]= name
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