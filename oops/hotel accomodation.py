class Accomodation:
    def __init__(self,Room_no,Room_type,rent):
        self.Room_no=Room_no
        self.Room_type=Room_type
        self.rent=rent
class Meal:
    def __init__(self,meal_type,meal_code,price):
        self.meal_type=meal_type
        self.price=price
        self.meal_code=meal_code
class Customer(Accomodation,Meal):
    def __init__(self,Room_no,Room_type,rent,meal_type,meal_code,price):
        Accomodation.__init__(self,Room_no,Room_type,rent)
        Meal.__init__(self,meal_type,meal_code,price)
    def display(self):
        print("Room no:",self.Room_no)
        print("Room type:",self.Room_type)
        print("Rent:",self.rent)
        print("Meal type:",self.meal_type)
        print("Meal code:",self.meal_code)

h=Customer(101,"ac",100,"veg","c101",1000)
h.display()

