class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def move(self):
        print("Car is moving")
class truck:
    def __init__(self, make, model, year, cargo_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.cargo_capacity = cargo_capacity
    def move(self):
        print("Truck is moving")
class plane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def move(self):
        print("Plane is flying")
class boat:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def move(self):
        print("Boat is sailing")
c1 = car("Toyota","Corolla","2015")
t1 = truck("Toyota","Corolla","2015","5000")
p1=plane("Toyota","Corolla","2015","500")
b1=boat("Toyota","Corolla","2015","100")
for x in (c1,t1,p1,b1):
    x.move()