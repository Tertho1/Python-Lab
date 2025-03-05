class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer Name: {self.name}, Email: {self.email}, Phone: {self.phone}\n"

    def place_order(self, order):
        return order


class Product:
    def __init__(self, product_name, price, stock_quantity):
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product Name: {self.product_name}, Price: {self.price}, Stock Quantity: {self.stock_quantity}"

    def update_stock(self, quantity):
        self.stock_quantity += quantity


class Order:
    def __init__(self, order_id, customer, products=None, total_price=0):
        self.order_id = order_id
        self.customer = customer
        self.products = products if products is not None else []  
        self.total_price = total_price

    def __str__(self):
        product_details = "\n".join([str(product) + f", Order_Quantity: {quantity}" for product, quantity in self.products])
        return f"Order ID: {self.order_id}\n\nCustomer:\n{self.customer}\nProducts:\n{product_details}\nTotal Price: {self.total_price}"

    def add_products(self, product, quantity):
        self.products.append((product, quantity))

    def calculate_total(self):
        self.total_price = sum(product.price * quantity for product, quantity in self.products) 
        return self.total_price


class Transaction:
    def __init__(self, transaction_id, order, payment_method, payment_status="Pending"):
        self.transaction_id = transaction_id
        self.order = order
        self.payment_method = payment_method
        self.payment_status = payment_status

    def __str__(self):
        return f"Transaction ID: {self.transaction_id} Order: {self.order.order_id} Payment Method: {self.payment_method} Status: {self.payment_status}"
    def process_payment(self):
        self.payment_status = "Success"
        print(f"Payment Completed")
        


def main():
    product1 = Product("Laptop", 50000, 10)
    product2 = Product("Mobile", 2000, 20)

    customer1 = Customer("Tertho", "tertho12345@gmail.com", "01712345678")
    order1 = Order(1, customer1)
    order1.add_products(product1, 2)
    order1.add_products(product2, 3)
    order1.calculate_total()
    print(order1, "\n") 

    transaction1 = Transaction("t1", order1, "Cash")
    print(transaction1)
    transaction1.process_payment()
    print(transaction1, "\n")

    product1.update_stock(-order1.products[0][1])
    product2.update_stock(-order1.products[1][1])
    print(product1)
    print(product2)
    print(customer1)


if __name__ == '__main__':
    main()
