
#Write a program to compute distance between two points accepted from the user.
print("Enter the coordinates of two points A(x1,y1) and B(x2,y2) to calculate the distance between them")
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))

distance=((x2-x1)**2+(y2-y1)**2)**0.5
print("The distance between A and B is:",distance)

