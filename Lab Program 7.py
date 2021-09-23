# Name: Shriyans Gandhi
# Class:12
# Date of executiom: 29/6/21
# Write a Program which accepts a list having even number of elements and swpas the elments at adjacent posotion using user-defined functions.
# Example: A= [10,20,30,40,50,60] >>> [20,10,40,30,60,50]

def swap(swap_list):
    for x in range(0,len(swap_list)-1,2):
        swap_list[x],swap_list[x+1]=swap_list[x+1],swap_list[x]
    print("The swapped list is",swap_list)
        
swap_list=list(eval(input("Enter the list:")))

if (len(swap_list)%2) != 0:
    print("List doesn't have even number of elements.")
else:
    swap(list=swap_list)

