f= open("Class Illustrations/writeline.txt", "w") # note I use linux, so I need to use a forward slash, for windows its backlash
l = ["hellooo ", "woah ", "this is ", " really cool ", "ta daaaaaa"] # it even works with tuple
f.writelines(l)
f.close()