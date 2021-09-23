import csv



def input_entries():
    f = open("test.csv","w",newline = "")
    writer = csv.writer(f)
    data = ["Number","Name","Price"]
    writer.writerow(data)
    rec = []
    print("Inputting Entries")
    print("-----------")
    while True:
        number = int(input("Enter the number of the product:"))
        name = input("Enter the name of the product:")
        price = input("Enter the price of the product:")
        data = [number,name,price]
        rec.append(data)
        more_entries = input("Do you want to enter more records?(Y/N)")
        if more_entries in ["N","n"]:
            break
    print("-----------")
    writer.writerows(rec)
    print("Written to the CSV file succesfully.")
    f.close()
    


def read_entries():
    f = open("test.csv","r")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()

def search ():
    f = open("test.csv","r")
    reader = csv.reader(f)
    number = int(input("Enter the item number to be searched:"))

    def check():
        print(next(reader))# To skip the first row
        for i in reader:
            if (i[0]) == number:
               print("Item found:")
               print(i)
               break
        else:
            print("Item number not found")
    check()
    f.close()
    
#input_entries()
#read_entries()
search()

   
    
    
