# 3. accept % of the student and display grade accordingly
#     >85 A
#     >70 and <=85 B
#     >60 and <=70 C
#     >45 and <=60 D
# <=45 E

def grade(per):
    if (per>85):
        return "A"
    elif (per >70 and per <=85):
        return "B"
    elif (per >60 and per <=70):
        return "C"
    elif (per >45 and per <=60):
        return "D"
    else:
        return "E"
per = int(input("enter the percentage"))
print("your grade is",grade(per))


