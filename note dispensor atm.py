#An ATM contains Indian Currency notes of 100,200,500 and 2000.
# Write a python program which calculates and displays the minimum number of notes required to be dispensed
# to meet the user’s requirement
print("Enter the amount you want to withdraw:")
amount=int(input())
notes=[2000,500,200,100]
noteCounter=[0,0,0,0]
i=0
while amount!=0:
    noteCounter[i]=amount//notes[i]
    amount=amount-noteCounter[i]*notes[i]
    i+=1
print("The notes are:")
for i in range(4):
    if noteCounter[i]!=0:
        print(notes[i],":",noteCounter[i])
print("Thank you for using our ATM")