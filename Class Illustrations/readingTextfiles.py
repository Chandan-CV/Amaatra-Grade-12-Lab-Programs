f = open("Class Illustrations/demo.txt","a") # note I use linux, so I need to use a forward slash, for windows its backlash

# case 1
f.write("yooo")
f = open("Class Illustrations/demo.txt","r") # note I use linux, so I need to use a forward slash, for windows its backlash
n = f.readlines()
print(n)
for i in n:
    print(i)
# case 2
# n= f.readlines()
# print(n)
# # case 3
# n= f.readlines()
# print(n)
# # case 4
# n= f.readlines()
# print(n)




f.close()
