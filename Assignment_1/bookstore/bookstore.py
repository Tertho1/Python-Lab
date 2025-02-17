if __name__ == "__main__":
    from book import add_book, list_books
    from customer import add_customer, list_customers
    from orders import place_order, list_orders
    from data_manager import load_data, save_data
    from state import books, customers, orders

    load_data(books, customers, orders)

    while True:
        save_data(books, customers, orders)
        print("\n--- Online Bookstore Management System ---")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Add a new customer")
        print("4. List all customers")
        print("5. Place a new order")
        print("6. List all orders")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            price = float(input("Enter book price: "))
            add_book(title, author, genre, price)
            print("Book added successfully.")
        elif choice == "2":
            books = list_books()
            if books:
                print("\nBooks in Inventory:")
                for book in books:
                    print(
                        f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Price: ${book['price']:.2f}"
                    )
            else:
                print("No books in inventory.")
        elif choice == "3":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            add_customer(name, email, phone)
            print("Customer added successfully.")
        elif choice == "4":
            customers = list_customers()
            if customers:
                print("\nCustomers:")
                for customer in customers:
                    print(
                        f"Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}"
                    )
            else:
                print("No customers found.")
        elif choice == "5":
            customers = list_customers()
            if not customers:
                print("No customers available. Please add a customer first.")
                continue

            print("\nSelect a customer:")
            for idx, customer in enumerate(customers):
                print(
                    f"{idx}. Name: {customer['name']}, Email: {customer['email']}, Phone: {customer['phone']}"
                )

            try:
                customer_id = int(
                    input("Enter the number corresponding to the customer: ")
                )
                if customer_id < 0 or customer_id >= len(customers):
                    print("Invalid customer selection. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            books = list_books()
            if not books:
                print("No books available. Please add a book first.")
                continue

            print("\nSelect a book:")
            for idx, book in enumerate(books):
                print(
                    f"{idx}. Title: {book['title']}, Author: {book['author']}, Price: ${book['price']:.2f}"
                )

            try:
                book_index = int(input("Enter the number corresponding to the book: "))
                if book_index < 0 or book_index >= len(books):
                    print("Invalid book selection. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            quantity = int(input("Enter quantity: "))
            customer_name = customers[customer_id]["name"]
            book_title = books[book_index]["title"]
            place_order(customer_name, book_title, quantity)
            print("Order placed successfully.")
        elif choice == "6":
            orders = list_orders()
            if orders:
                print("\nOrders:")
                for order in orders:
                    print(
                        f"Customer Name: {order['customer_name']}, Book Title: {order['book_title']}, Quantity: {order['quantity']}"
                    )
            else:
                print("No orders placed.")
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
