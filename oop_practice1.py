class myclass:
    x = 5


obj = myclass()
print(obj.x)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


p1 = person("John", 36)
print(f"Name: {p1.name}, Age: {p1.age}")
print(p1)
print(p1.greet())


class student:
    def __init__(sillyguy, name, age, grade):
        sillyguy.name = name
        sillyguy.age = age
        sillyguy.grade = grade

    def __str__(sillyguy):
        return f"Name: {sillyguy.name}, Age: {sillyguy.age}, Grade: {sillyguy.grade}"

    def greet(silly):
        return f"Hello, my name is {silly.name} and I am {silly.age} years old. I am in grade {silly.grade}."


st1 = student("John", 36, "A")
print(st1)
print(st1.greet())
st1.name = "Tertho"
print(st1)
del st1.age
print(st1.name)


class Animal:
    pass


a = Animal()
print(a)


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book Title : {self.title}, Author:{self.author}, Price:{self.price}, Expensive: {self.is_expensive()}"

    def discount(self, percentage):
        if self.price > 200:
            self.price = self.price - (self.price * percentage / 100)
        return self.price

    def is_expensive(self):
        return self.price > 500

    def get_details(self):
        return f"Book title : {self.title}, Author : {self.author}, Price : {self.price} Expensive: {self.is_expensive()}"


b1 = Book("Python Programming", "John Doe", 500)
print(b1)
print(b1.discount(10))
print(b1.get_details())
b1.price = 200
print(b1.get_details())
print(b1.discount(10))
del b1.author
print(b1.title)
del b1
