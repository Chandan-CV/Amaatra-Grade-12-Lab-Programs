f = open("Class Illustrations/demo.txt","a")

# case 1
f.write("yooo")
f = open("Class Illustrations/demo.txt","r")
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
