# A binary file "book.dat" has structure [ book number book name author and proce]
#[A] user defined function createfile() to input and add records 
# [B] createrec() and return count no of books by the given author 
#date: 26 8  21 
import pickle
def createfile()
f=open("book.dat", 'ab')
bookNo = int(input("bookNo"))
book_name= (input("book name"))
author= input("author")
price=int(input("book price"))
rec=[bookNo,book_name,author,price]
pickle.dump(rec,f)
f.close 

def countrec(author):
    f=open("book.dat",'rb')
    num=0
    try:
        while True:
            rec= pickle.load(f)
            if author==rec[2]
            num=num+1
            print(rec[0],rec[1],rec[2],rec[3])

    except:
        fobj.close()
        return num
count=int(input("enter total number of books"))
for i in range(count):
    createfile()
n=countrec("james")
print("total rec", n)