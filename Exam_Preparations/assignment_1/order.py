def place_order(customer_id,book_title,quantity,orders=[]):
    orders.append([customer_id,book_title,quantity])
    return orders
def list_orders(orders):
    for order in orders:
        print(f"Customer ID: {order[0]}, Book Title: {order[1]}, Quantity: {order[2]}")
