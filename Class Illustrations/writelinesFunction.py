f= open("Class Illustrations/writeline.txt", "w")
l = ["hellooo ", "woah ", "this is ", " really cool ", "ta daaaaaa"] # it even works with tuple
f.writelines(l)
f.close()