class BankAccount:

    bank_name = "First National Dojo"
    all_accounts = []
    int_rate = 0.01
    balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print(f"Insufficient Funds: Charging a $5 fee.")
            self.balance - 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest-rate: {self.int_rate}%")
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print(f"Account balance is $0 or Negative, not earning any interest")
        else:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

savings_account = BankAccount(0.03, 1)
checking_account = BankAccount(0.01, 25)
moneymarket_account = BankAccount(0,0)
cd_account = BankAccount(0.05,15000)

savings_account.deposit(10).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()

checking_account.deposit(200).deposit(5).withdraw(100).withdraw(50).withdraw(25).withdraw(500).yield_interest().display_account_info()

moneymarket_account.deposit(10000).deposit(500).deposit(3000).yield_interest().display_account_info()

cd_account.deposit(10000).yield_interest().display_account_info()

print("BONUS!")

BankAccount.display_all_accounts()