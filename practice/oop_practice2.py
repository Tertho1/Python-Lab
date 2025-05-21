class person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printname(self):
        print(f"Name : {self.firstname +" "+ self.lastname}")
p1 = person("John","Doe")
p1.printname()

class student(person):
    def __init__(self,fname,lname,roll):
        super().__init__(fname,lname)
        self.roll = roll
    def printname(self):
        print(f"Name : {self.firstname +" "+ self.lastname}, Roll : {self.roll}")
s1=student("Tertho","Ghosh","2003")
s1.printname()

class vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def vehicleinfo(self):
        print(f"Brand : {self.brand}, Model : {self.model}, Year : {self.year}")
v1 = vehicle("Toyota","Corolla","2015")
v1.vehicleinfo()

from datetime import datetime
class car(vehicle):
    def __init__(self,brand,model,year,fueltype,door):
        super().__init__(brand,model,year)
        self.fueltype = fueltype
        self.door = door
    def vehicleinfo(self):
        super().vehicleinfo()
        print(f", Fuel Type : {self.fueltype}, Door : {self.door} Age: {self.calculateage()}")
    def startengines(self):
        print("Engine Started")
    def stopengines(self):
        print("Engine Stopped")
    def calculateage(self):
        return datetime.now().year - int(self.year)
       
c1 = car("Toyota","Corolla","2015","Petrol","4")
c1.vehicleinfo()
c1.startengines()
c1.stopengines()


