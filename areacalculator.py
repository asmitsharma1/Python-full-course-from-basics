#area calculator
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
r=int(input("Enter the radius:"))
side=int(input("Enter the side:"))
print("Enter the shape:")
print("1.Rectangle")
print("2.Circle")
print("3.Square")
print("4.Triangle")
print("5.Exit")
choice=int(input())
if choice==1:
    print("Area of rectangle is:",l*b)
elif choice==2:
    print("Area of circle is:",3.14*r*r)
elif choice==3:
    print("Area of square is:",side*side)
elif choice==4:
    print("Area of triangle is:",1/2*l*b)
elif choice==5:
    print("Exit")
else:
    print("Invalid choice")