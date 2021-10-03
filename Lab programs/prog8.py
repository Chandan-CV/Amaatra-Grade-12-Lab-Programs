# WAP to accept a string (a sentence ) and return a string having first letter of each word in capital letter
#Name:
#Date of exceution:
#Grade:
def capi (s):
    r =""
    
    for a in s.split():
        r += a.capitalize()+" "
    return r.strip()

print(capi("hello this is chandan here"))