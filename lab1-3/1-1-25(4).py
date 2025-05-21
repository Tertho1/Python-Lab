sales = [250, 400, 150, 700, 300, 500, 600]
sales.append(500)
print("Sales:", sales)

total_sales = sum(sales)
print(f"Total Sales: {total_sales}")
print(f"Max Sale: {max(sales)}")
print(f"Min Sale: {min(sales)}")
print(f"Average Sale: {total_sales / len(sales):.2f}")
sales.remove(min(sales))
print("Updated Sales :", sales)

count= sum(1 for sale in sales if sale > 500)
print(f"Count of sales > 500: {count}")

sales.sort()
print("Sales in ascending order:", sales)
sales.reverse()
print("Sales in descending order:", sales)
