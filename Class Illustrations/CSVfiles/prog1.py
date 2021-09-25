import csv
from os import write
f = open ("Class Illustrations/CSVfiles/file.csv", "w")
writeobj = csv.writer(f)
writeobj.writerows([["hi", "there", "I am", "chandan here"],["this is the second row", "this should prolly work"],["this is the third row"]])