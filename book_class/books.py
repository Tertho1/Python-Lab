class book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}, Price: {self.price}"

    def discount(self, percentage):
        return self.price * percentage / 100.0
    def is_expensive(self):
        return self.price > 500
    def get_details(self):
        attributes = ['title', 'author', 'price']
        details = [f"{attr.capitalize()}: {getattr(self, attr, 'N/A')}" for attr in attributes]
        return ', '.join(details)


book1 = book("Atomic Habits", "James Clear", 1000)
print(book1.get_details())
discount = book1.discount(10)
print(f"Discounted Price: {discount}")
print(f"Expensive : {book1.is_expensive()}")
del book1.author
print(book1.get_details())
