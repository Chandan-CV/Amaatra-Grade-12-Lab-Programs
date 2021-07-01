# 5. prime numbers upto a certain limit

def primo(n):
    primeNubers =[]
    for i in range (1,n+1):
        count =0
        for x in range(1,i+1):
            if (i%x==0):
                count+=1
        if(count==2):
            primeNubers.append(i)
    return primeNubers

print(primo(int(input("enter the range"))))
