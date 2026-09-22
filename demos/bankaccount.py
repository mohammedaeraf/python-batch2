class BankAccount:

    def __init__(self, account_number, holder, balance):

        self.account_number = account_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):

        self.balance = self.balance + amount

    def display_balance(self):

        print("Balance =", self.balance)


account1 = BankAccount(101, "Ahmed", 5000)

account1.deposit(2000)

account1.display_balance()