class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __lt__(self, other):
        return self.year < other.year

    def __gt__(self, other):
        return self.year > other.year

    def __eq__(self, other):
        return self.year == other.year

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'
car=Car('Toyota', 'Corolla', 2019)
print(car)
