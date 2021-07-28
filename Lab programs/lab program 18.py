#wap to read a text file and use it in appened mode show the working of write lines()
#july 27
f=open("lab.txt", "a")
content=("\n", "THIS IS FIRST LINE",\
    "\n THIS IS SECOND LINE",\
        "\n THIS IS THIRD LINE", "\n this is fourth line ")
f.writelines(content)
f.close()