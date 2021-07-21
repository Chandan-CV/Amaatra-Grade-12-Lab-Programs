#WAP to shift the negative numbers to left and postitve numbers to right l=[-2, 1, -3, -15, 16, -17, 5, -3, -6 ]
list1=[-2,1,-3,-15,16,-17,5,-3,-6]

list2=[0]*9

a=len(list1)

a=a-1

j=0

for i in range(9):

  if list1[i]>0:

      list2[j]=list1[i]

      j+=1

     

  else:

      list2[a]=list1[i]

      a-=1

       

print(list2)

