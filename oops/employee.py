class Employee:
    def __init__(self,number,name,designation,salary,address):
        self.number=number
        self.name=name
        self.designation=designation
        self.salary=salary
        self.address=address

    def getdata(self):
        self.number=int(input("Enter the employee number:"))
        self.name=input("Enter the employee name:")
        self.designation=input("Enter the employee designation:")
        self.salary=int(input("Enter the employee salary:"))
        self.address=input("Enter the employee address:")

    def display(self):
        print("Employee number:",self.number)
        print("Employee name:",self.name)
        print("Employee designation:",self.designation)
        print("Employee salary:",self.salary)
        print("Employee address:",self.address)

class Salary:
    def __init__(self,basic_pay,da,hra,net_salary):
        self.basic_pay=basic_pay
        self.da=da
        self.hra=hra
        self.net_salary=net_salary

    def getdatal(self):
        self.basic_pay=int(input("Enter the basic pay:"))
        self.da=int(input("Enter the da:"))
        self.hra=int(input("Enter the hra:"))
        self.net_salary=int(input("Enter the net salary:"))
    def display(self):
        print("Basic pay:",self.basic_pay)
        print("Da:",self.da)
        print("Hra:",self.hra)
        print("Net salary:",self.net_salary)

Employee(1,"John","Manager",50000,"Bangalore").display()
Salary(10000,1000,1000,10000).display()
# e=Employee(1,"John","Manager",50000,"Bangalore")