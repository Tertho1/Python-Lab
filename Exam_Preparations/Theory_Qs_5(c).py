class animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        print(f"{self.name} is speaking")

class Dog(animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        print(f"{self.name} is barking")

d=Dog("Tommy", "Labrador")
d.speak()
a=animal("Tom")
a.speak()