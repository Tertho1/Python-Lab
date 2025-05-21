def calculate_bonus(salary):
    return salary * .10
def claculate_tax(salary):
    return salary * .15
def calculate_total(salary):
    return salary + calculate_bonus(salary) - claculate_tax(salary)