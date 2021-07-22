#wap to accept values from the user and create a tuple
def prac():
    t=tuple()
    n=int(input("enter total number to beinputed"))
    for i in range(n):
        a=input("enter a number")
        t=t+(a,)
    print("output is",t)

prac()