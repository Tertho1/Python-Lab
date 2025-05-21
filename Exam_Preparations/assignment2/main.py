class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.orders = []  # Optional: to track order history

    def __str__(self):
        return f"Customer Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

    def place_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} placed by {self.name}")


class Product:
    def __init__(self, product_name, price, stock_quantity):
        self.product_name = product_name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product: {self.product_name}, Price: ${self.price}, Stock Quantity: {self.stock_quantity}"

    def update_stock(self, quantity):
        self.stock_quantity += quantity


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []  # list of tuples: (Product, quantity)
        self.total_price = 0.0

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.products.append((product, quantity))
            product.update_stock(-quantity)
            print(f"Added {quantity} x {product.product_name} to Order {self.order_id}")
        else:
            print(f"Not enough stock for {product.product_name} (Available: {product.stock_quantity})")

    def calculate_total(self):
        self.total_price = sum(product.price * quantity for product, quantity in self.products)
        return self.total_price

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Total Price: ${self.total_price:.2f}"


class Transaction:
    def __init__(self, transaction_id, order, payment_method):
        self.transaction_id = transaction_id
        self.order = order
        self.payment_method = payment_method
        self.payment_status = "Pending"

    def process_payment(self):
        self.payment_status = "Completed"
        print(f"Transaction {self.transaction_id} completed for Order {self.order.order_id}")

    def __str__(self):
        return (f"Transaction ID: {self.transaction_id}, Order ID: {self.order.order_id}, "
                f"Payment Method: {self.payment_method}, Status: {self.payment_status}")


# Create customer
customer1 = Customer("Alice", "alice@example.com", "0123456789")
print(customer1)

# Create products
product1 = Product("Mouse", 10.99, 50)
product2 = Product("Keyboard", 25.50, 30)
print(product1)
print(product2)

# Create order
order1 = Order("ORD001", customer1)
customer1.place_order(order1)

# Add products to order
order1.add_product(product1, 2)  # 2 Mice
order1.add_product(product2, 1)  # 1 Keyboard

# Calculate total
order1.calculate_total()
print(order1)

# Create transaction
transaction1 = Transaction("TXN001", order1, "Credit Card")
print(transaction1)

# Process payment
transaction1.process_payment()
print(transaction1)

# Check updated product stock
print(product1)
print(product2)
