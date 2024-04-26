A=list(input("enter the number containing 0 and 1:"))
#make a program that will count the number of 0 and 1 in the given numberand convert all 0 and 1 in either all 1 or 0  and if possible in one flip all bits convert to either 0 or 1 print yes else no
count0=0
count1=0
for i in A:
    if i=="0":
        count0+=1
    else:
        count1+=1
if count0==1 or count1==1:
    print("yes")
else:
    print("no")
