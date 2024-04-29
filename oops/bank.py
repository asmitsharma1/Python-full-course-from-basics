class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model

    def get_brand(self):
        return self.__brand
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol"

class Electriccar(Car):
    def __inti__(brand,model,battery_size):
        super().__init__(brand,model)
        battery_size=battery_size
    def fuel_type(self):
        return "Electric"

tesla=Electriccar("Tesla","Model S",100)
print(tesla.get_brand)
print(tesla.full_name())
print(tesla.fuel_type())
