def calculate_bonus(salary):
    return salary * 0.10

def calculate_tax(salary):
     return salary * 0.15

def calculate_total_payment(salary,bonus,tax):
    return salary + bonus - tax