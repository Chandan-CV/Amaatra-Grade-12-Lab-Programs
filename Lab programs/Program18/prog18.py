#open a file and use it in append mode, show the working of writelines()
f = open("Lab programs/Program18/text.txt","a")



def app(content):
    f.writelines(content)

app(("hii ", "there \n", "this ", "is ", "is the code ", "which is used to append values", "to the TextFile!!!!","\n","\n","\n","\n","\n","\n","\n","\n","\n","10 lines later"))
f.close()