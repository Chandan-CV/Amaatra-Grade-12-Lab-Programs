#wap to accept a number and print ifit is a amstrong number or not
def practice():
    num=int(input("enter a number"))
    f=num
    sum=0
    while(f>0):
        a=f%10
        f=int(f/10)
        sum=sum + (a**3)
    if(sum==num):
        print("its an amstrong number")
    else:
        print("not an amstrong number")

practice()