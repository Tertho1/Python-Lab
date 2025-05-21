from payment import calculate_bonus,calculate_total,claculate_tax
salary=float(input("Enter your salary: "))
print("Your bonus is: ",calculate_bonus(salary))
print("Your tax is: ",claculate_tax(salary))
print("Your total is: ",calculate_total(salary))