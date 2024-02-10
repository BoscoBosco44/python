class BankAccount:
    all_accounts = []

    def __init__(self, amount, interest_rate, name=""):
        self.balance = amount
        self.interest_rate = interest_rate
        self.name = name
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

class user(BankAccount):
    def __init__(self, first_name, last_name, email, age):
        accList = []
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        BankAccount.all_accounts.append(self)
        self.accList = BankAccount.all_accounts.append(self)

    def display_info(self):
        print("Name: ", self.first_name)
        print("Last-name: ", self.last_name)
        print("Email: ", self.email)
        print("Age: ", self.age)
        print("Rewards Member: ", self.is_rewards_member)
        print("Points: ", self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if 0 < (self.gold_card_points - amount):
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("User needs ", (self.gold_card_points - amount) * (-1), " more points")
        return self
            
    def make_deposit(self, numDeposit):
        BankAccount.deposit(numDeposit)

    def make_withdraw(self, numWithdraw):
        BankAccount.withdraw(numWithdraw)

    def addAccount(self, acc):
        BankAccount.accList.append(acc)

    def displayUser(self):
        print("Name: ", self.first_name, self.last_name)
        print(BankAccount.all_accounts[0])

        print("Num Accounts: ", len(self.all_accounts))
        numAcc = len(self.all_accounts)
        for x in BankAccount.all_accounts:
            print("Account ", x, " ballence: ", self.all_accounts[0].balance)




acc1 = BankAccount(500, 0.06, "acc11").deposit(22).deposit(55).deposit(432).withdraw(333).yeild_interest().display_account_info()
acc2 = BankAccount(6500, 0.06, "acc22").deposit(333).withdraw(222).withdraw(111).withdraw(8).withdraw(123).yeild_interest().display_account_info()
BankAccount.printAllAccounts()

user1 = user("Belle", "Weiler", "rondaRonda@gmail.com", 55)
user1.displayUser()