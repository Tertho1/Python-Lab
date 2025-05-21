
n = int(input("Enter How many Products: "))
products = []
stock = []

print("Enter Product Names:")
for i in range(n):
    products.append(input())

print("Enter Product stock:")
for i in range(n):
    stock.append(int(input()))  

print("\nProducts with stock less than 5 but greater than 0:")
for i in range(n):
    if 0 < stock[i] < 5:
        print(products[i])

print("\nProducts with zero stock:")
for i in range(n):
    if stock[i] == 0:
        print(products[i])

total_stock = sum(stock)  
print(f"\nTotal Stock: {total_stock}")
