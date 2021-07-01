#pallindrome

def checlPal(s):
    rev =""
    for i in range (len(s)-1,-1,-1):
        rev += s[i]
    if (rev == s):
        return("Pallindrome")
    else:
        return("not a pallindrome")

print(checlPal(input("enter the string")))