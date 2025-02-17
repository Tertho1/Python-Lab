from state import customers

def add_customer(name, email, phone):
    customers.append({"name": name, "email": email, "phone": phone})

def list_customers():
    return customers
