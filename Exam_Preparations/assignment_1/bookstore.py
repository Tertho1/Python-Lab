from book import add_book, list_books
from customer import add_customer, list_customers
from order import place_order, list_orders
books = []
customers = []
orders = []
while True:
    print("Welcome to the Bookstore Management System")
    print(
        """Available Options:
        1. Add Book
        2. List Books
        3. Add Customer
        4. List Customers
        5. Place Order
        6. List Orders
        7. Exit"""
    )
    op = int(input("Enter your choice (1-7) : "))
    if op == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        price = float(input("Enter book price: "))
        books = add_book(title, author, genre, price, books)
    elif op == 2:
        list_books(books)
    elif op == 3:
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        customers = add_customer(name, email, phone, customers)
    elif op == 4:
        list_customers(customers)
    elif op == 5:
        customer_id = int(input("Enter customer ID: "))
        book_title = input("Enter book title: ")
        quantity = int(input("Enter quantity: "))
        orders = place_order(customer_id, book_title, quantity, orders)
    elif op == 6:
        list_orders(orders)
    elif op == 7:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")


