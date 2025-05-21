def add_customer(name, email, phone, customers=[]):
    customers.append([name, email, phone])
    return customers


def list_customers(customers):
    for customer in customers:
        print(f"Name: {customer[0]}, Email: {customer[1]}, Phone: {customer[2]}")
