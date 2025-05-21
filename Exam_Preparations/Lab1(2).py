sales=[250,400,150,500,300,600,700]

sales.append(450)
print(f"Total sales : {sum(sales)}")
print(f"Highest sales : {max(sales)}")
print(f"Average Sales : {sum(sales)/len(sales)}")
sales.remove(150)
print(f"Corrected sales : {sales}")
sales.sort()
print(f"Sorted Sales : {sales}")
print(f"Sales greater than 500 : {len([x for x in sales if x>500])}")
sales.reverse()
print(f"Reversed sales : {sales}")