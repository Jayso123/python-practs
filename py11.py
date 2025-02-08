class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def get_name(self):
        return self.name

    def get_account(self):
        return self.account


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, name):
        for customer in self.customers:
            if customer.get_name() == name:
                return customer
        return None


account1 = BankAccount(1000)
customer1 = Customer("chhagan", account1)

account2 = BankAccount(1000)
customer2 = Customer("magan", account2)

bank = Bank("MyBank")
bank.add_customer(customer1)
bank.add_customer(customer2)

customer1.account.deposit(800)
customer1.account.withdraw(10)
print(customer1.account.get_balance())

customer2.account.deposit(1000)
customer2.account.withdraw(450)
print(customer2.account.get_balance())
