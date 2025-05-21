class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
class Boat:
    def __init__(self, brand, model, year):
        self.brand= brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Boat Make: {self.brand}, Model: {self.model}, Year: {self.year}")
class Plane:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Plane Make: {self.manufacturer}, Model: {self.model}, Year: {self.year}")
c=Car("Toyota", "Camry", 2020)
b=Boat("Yamaha", "242X", 2021)
p=Plane("Boeing", "747", 2019)
c.display_info()
b.display_info()
p.display_info()