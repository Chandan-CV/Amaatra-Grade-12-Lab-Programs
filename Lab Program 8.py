# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program which returns first letter of each word in capital


def capitalize_func(s):
    capital_string = ""
    for a in s.split():
        capital_string += a.capitalize() + " "
    return capital_string.rstrip()

s=str(input("Enter a string:"))
print(capitalize_func(s))

# def func(l):
#     for x in l[::-1]:
#         print(x,x%2 !=0)
#         if (x%2 !=0) :
#             l.remove(x)
#     print(l)



# l=list(eval(input("Enter a list:")))
# func(l)
