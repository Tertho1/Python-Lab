from datetime import datetime


class vehicle:
    def __init__(
        self,
        brand,
        model,
        year,
    ):
        self.brand = brand
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


class car(vehicle):
    def __init__(self, brand, model, year, fuel_type, doors):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def vehicle_info(self):
        return (
            f"{super().vehicle_info()}, Fuel_Type:{self.fuel_type} Doors: {self.doors}"
        )

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"

    def calculate_age(self):
        return datetime.now().year - self.year


my_car = car("Tesla", "Model S", 2022, "electric", 4)
print(my_car.vehicle_info())
print(my_car.start_engine())
print(my_car.stop_engine())
car_age = my_car.calculate_age()
print(f"The car is {car_age} years old.")
