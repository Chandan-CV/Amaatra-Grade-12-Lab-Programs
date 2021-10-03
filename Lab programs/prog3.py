# WAP to accept lower limit and upper limit and print the even and odd numbers between those
#Name:
#Date of exceution:
#Grade:
def oddEven(ll,ul):
    odd =[]
    even = []
    for x in range (ll,ul):
        if (x % 2==0):
            even.append(x)
        else:
            odd.append(x)
    return even,odd

ll = int(input("enter the lower limit"))
ul = int(input("enter the upper limit"))
even, odd = oddEven(ll,ul)
print("even = ",  even)
print ("odd = ", odd)