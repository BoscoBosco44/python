class BankAccount:
    all_accounts = []

    def __init__(self, amount, interest_rate):
        self.balance = amount
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    all_accounts = []

    @classmethod
    def printAllAccounts(cls):
        for account in cls.all_accounts:
            print(account.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yeild_interest(self):
        self.balance = (self.balance) * (self.interest_rate)
        return self

acc1 = BankAccount(500, 0.06).deposit(22).deposit(55).deposit(432).withdraw(333).yeild_interest().display_account_info()
acc2 = BankAccount(6500, 0.06).deposit(333).withdraw(222).withdraw(111).withdraw(8).withdraw(123).yeild_interest().display_account_info()
BankAccount.printAllAccounts()