#Wap to accept string list and print words starting with 'A' or 'a'

s = input("enter the list of words").split()

def Aword():
    for w in s:
        if w[0]=="A" or w[0]=="a":
            print(w)
    
Aword()