from datetime import datetime
from time import sleep


class Bank:
    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transactions = []

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}, Account Type: {self.account_type}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
            t = self.Transaction(
                len(self.transactions) + 1, "Deposit", amount, datetime.now()
            )
            self.add_transaction(t)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")
        else:
            print(
                "Withdrawal amount must be positive and less than or equal to the balance."
            )
        t = self.Transaction(
            len(self.transactions) + 1, "Withdraw", amount, datetime.now()
        )
        self.add_transaction(t)

    def get_balance(self):
        print(f"Current balance : {self.balance}")

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        print(
            f"Transaction {transaction.transaction_id} added to {self.account_holder}'s account."
        )

    class Transaction:
        def __init__(self, transaction_id, transaction_type, amount, date):
            self.transaction_id = transaction_id
            self.transaction_type = transaction_type
            self.amount = amount
            self.date = date

        def __str__(self):
            return f"Transaction ID: {self.transaction_id}, Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.date}"
user1=Bank("John Doe", "123456789", 1000, "Savings")
user1.deposit(500)
sleep(5)
user1.withdraw(200)
user1.get_balance()
for transaction in user1.transactions:
    print(transaction)