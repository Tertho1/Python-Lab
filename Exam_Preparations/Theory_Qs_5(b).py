class Resturant:
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name=resturant_name
        self.cuisine_type=cuisine_type
    def describe_resturant(self):
        print(f"Resturant name : {self.resturant_name} , Cuisine type : {self.cuisine_type}")
    def open_resturant(self):
        print(f"{self.resturant_name} is open")
        
resturant=Resturant("Pizzaburg", "Italian")
print(resturant.resturant_name)
print(resturant.cuisine_type)
resturant.describe_resturant()
resturant.open_resturant()