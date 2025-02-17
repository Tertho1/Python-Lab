from datetime import date

dates = date.today()


class BankAccount:
    class Transaction:
        def __init__(self, transaction_id, transaction_type, amount, date):
            self.transaction_id = transaction_id
            self.transaction_type = transaction_type
            self.amount = float(amount)
            self.date = date

        def __str__(self):
            return (
                f"Transaction ID: {self.transaction_id}, "
                f"Type: {self.transaction_type}, "
                f"Amount: ${self.amount}, Date: {self.date}"
            )

    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = float(balance)
        self.account_type = account_type
        self.transactions = []

    def __str__(self):
        return (
            f"Account Holder: {self.account_holder}, "
            f"Account Type: {self.account_type}, "
            f"Balance: ${self.balance}"
        )

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        transaction = self.Transaction(
            len(self.transactions) + 1, "Deposit", amount, dates
        )
        self.add_transaction(transaction)
        return f"Deposited ${amount} successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.balance < amount:
            return "Insufficient Balance."
        self.balance -= amount
        transaction = self.Transaction(
            len(self.transactions) + 1, "Withdrawal", amount, dates
        )
        self.add_transaction(transaction)
        return f"Withdrew ${amount} successfully."

    def get_balance(self):
        return self.balance

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_history(self):
        if not self.transactions:
            return "No transactions found."
        return "\n".join(str(transaction) for transaction in self.transactions)


account = BankAccount("Tertho Ghosh", "123456789", 1000.0, "Checking")
print(account)
print(account.deposit(500))
print(account.withdraw(200))
print("Balance:", account.get_balance())
print("Transaction History:")
print(account.get_transaction_history())
