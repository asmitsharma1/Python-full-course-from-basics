year=int(input("enter the year which you want to check:"))
if year%400==0 or(year%100!=0 and year%4==0):
    print("leap year",year)
else:
    print("not a leap year",year)