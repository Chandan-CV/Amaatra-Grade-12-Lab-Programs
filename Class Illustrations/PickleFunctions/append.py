import pickle


f = open("Class Illustrations/PickleFunctions/file.dat","ab")
f.seek(0)
rec = pickle.load(f)
print(rec)
def append():
    while True:
        no = int(input("enter your roll number"))
        name = input("enter your name")
        marks = int(input("enter your marks"))
        data = [no, name, marks]
        rec.append(data)
        ch = input("Y/N")
        if ch in 'Nn':
            break
    f.seek(0)
    pickle.dump(rec,f)
    f.close()
