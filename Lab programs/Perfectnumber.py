n = int(input("enter the number"))
sum=0

def func():
    global sum
    for x in range(1,n):
        if (n%x==0):
            sum+=x
    print ("sum =", sum)

func()
if (sum == n):
    print("its a super Perfect number")
else:
    print("its not a super number")

