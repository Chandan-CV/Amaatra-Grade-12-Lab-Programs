# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 27/7/21
# Write a Program to count the total number of vowels/consonants/uppercase alphabets/lowercase alphabets in a file.


def count():
    f=open("Lab programs/prog19/txt19.txt","r")
    vowels=["a","e","i","o","u"]
    vowels_count,consonants_count,lowercase_count,uppercase_count=0,0,0,0
    for x in f.read():
        if x in vowels:
            vowels_count+=1
        elif x.isalpha() and x not in vowels:
            consonants_count+=1
        if x.isupper():
            uppercase_count+=1
        elif x.islower():
            lowercase_count+=1
    print("Number of vowels:",vowels_count)
    print("Number of consonants:",consonants_count)
    print("Number of lowercase alphabets:",lowercase_count)
    print("Number of uppercase alphabets:",uppercase_count)


count()