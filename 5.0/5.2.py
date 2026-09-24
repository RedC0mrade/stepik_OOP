class BankAccount:
    
    def __init__(self, balance: int | float = 0):
        
        self._balance = balance
        
    def deposit(self, amount: int):
        
        self._balance += amount

    def get_balance(self):

        return self._balance

    def withdraw(self, amount):

        if amount > self._balance:

            raise ValueError("На счете недостаточно средств")

        self._balance -= amount

    def transfer(self, account: "BankAccount", amount):

        self.withdraw(amount=amount)

        account._balance += amount


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)