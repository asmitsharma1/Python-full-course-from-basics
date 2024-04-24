#program to make a simple calculator using python
#take input from the user
print("Select operation.")
print("1.Add")
print("2.substract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Modulus")
print("7.Floor Division")
print("8.Exit")
choice=input("Enter choice(1/2/3/4/5/6/7/8):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice=='1':
    print(num1,"+",num2,"=",num1+num2)
elif choice=='2':
    print(num1,"-",num2,"=",num1-num2)
elif choice=='3':
    print(num1,"*",num2,"=",num1*num2)
elif choice=='4':
    print(num1,"/",num2,"=",num1/num2)
elif choice=='5':
    print(num1,"**",num2,"=",num1**num2)
elif choice=='6':
    print(num1,"%",num2,"=",num1%num2)
elif choice=='7':
    print(num1,"//",num2,"=",num1//num2)
elif choice=='8':
    
    exit()

else:
    print("Invalid input")
# Output:
print("thank you for using my calculator")
