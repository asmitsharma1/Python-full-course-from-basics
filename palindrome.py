num=int(input("enter the number:"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("Palindrome")
else:
    print("not a Palindrome")
