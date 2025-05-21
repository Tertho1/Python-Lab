class InvalidTransactionError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise ValueError("Invalid amount. Please enter a numeric number.")
            elif amount <= 0:
                raise InvalidTransactionError("The user attempts to deposit or withdraw a non-positive amount")
            else:
                self.balance += amount
                print(f"Deposit successful. New balance: {self.balance}")
        except (InvalidTransactionError, ValueError,Exception) as e:
            print(f"Deposit failed: {e}")
        
    def withdraw(self, amount):
        try:
            if not isinstance(amount, (int, float)):
                raise ValueError("Invalid amount. Please enter a numeric number.")
            if amount <= 0:
                raise InvalidTransactionError("The user attempts to deposit or withdraw a non-positive amount")
            elif amount > self.balance:
                raise InsufficientFundsError("The user attempts to withdraw more than the available balance")
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        except (InvalidTransactionError, InsufficientFundsError, ValueError,Exception) as e:
            print(f"Withdrawal failed: {e}")
        

# Testing the Bank class
user = Bank(1000)
user.deposit(500)       # Should succeed
user.withdraw(200)      # Should succeed
user.withdraw(-100)     # Should be caught and handled
user.deposit(-50)       # Should be caught and handled
user.deposit("abc")     # Should be caught and handled
user.deposit(1450)