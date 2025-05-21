items = ["Apples", "Bananas", "Oranges", "Milk", "Eggs"]
quantity = [10, 2, 15, 0, 4]

for item, qty in zip(items, quantity):
    if qty < 5 and qty > 0:
        print(f"Low stock for {item}. Please restock.")
for item, qty in zip(items, quantity):
    if qty == 0:
        print(f"Out of stock for {item}. Please restock.")
print(f"Total items in stock: {sum(quantity)}")
