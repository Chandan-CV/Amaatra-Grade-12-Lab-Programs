r = open("Lab programs/prog12/provider.txt","r") # \ in windows
w = open("Lab programs/prog12/target.txt","w") # \ in windows

def move():
    w.write(r.read())

move()