if __name__ == "__main__":
    from payment import calculate_bonus, calculate_tax, calculate_total_payment

    try:
        salary = float(input("Enter the employee's base salary: "))

        bonus = calculate_bonus(salary)
        tax = calculate_tax(salary)
        total_payment = calculate_total_payment(salary,bonus,tax)

        print(f"Base Salary: {salary:.2f}")
        print(f"Bonus (10%): {bonus:.2f}")
        print(f"Tax Deduction (15%): {tax:.2f}")
        print(f"Total Payment: {total_payment:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the salary.")