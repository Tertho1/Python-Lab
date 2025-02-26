import numpy as np

units_sold = np.array([
    [50, 60],
    [45, 55],
    [60, 70],
    [65, 75],
    [80, 90],
    [85, 95],
    [90, 100]
])

prices = np.array([15, 20])

total_revenue = np.sum(units_sold * prices, axis=0)
region_A_revenue = total_revenue[0]
region_B_revenue = total_revenue[1]

average_sales = np.mean(units_sold, axis=0)
average_sales_A = average_sales[0]
average_sales_B = average_sales[1]

highest_sales_A = np.max(units_sold[:, 0])
highest_sales_B = np.max(units_sold[:, 1])
highest_sales_day_A = np.argmax(units_sold[:, 0])
highest_sales_day_B = np.argmax(units_sold[:, 1])
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

total_company_revenue = region_A_revenue + region_B_revenue

print(f"Region A Total Revenue: {region_A_revenue}")
print(f"Region B Total Revenue: {region_B_revenue}")
print(f"Average Sales for Region A: {average_sales_A:.3f} units/day")
print(f"Average Sales for Region B: {average_sales_B:.3f} units/day")
print(f"Highest Sales Day for Region A: {days[highest_sales_day_A]}, {highest_sales_A} units")
print(f"Highest Sales Day for Region B: {days[highest_sales_day_B]}, {highest_sales_B} units")
print(f"Total Company Revenue: ${total_company_revenue}")
