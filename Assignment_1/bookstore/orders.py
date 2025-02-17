from state import orders
def place_order(customer_name, book_title, quantity):
    orders.append(
        {"customer_name": customer_name, "book_title": book_title, "quantity": quantity}
    )

def list_orders():
    return orders

