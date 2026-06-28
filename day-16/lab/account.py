'''
Create a parent class named BankAccount with attributes account holder and balance. 
Add a method withdraw(amount) that subtracts money from the balance if funds are 
sufficient. Create a child class named SavingsAccount that inherits from BankAccount. 
Add a new attribute called interest_rate. Add a method to SavingsAccount called 
add_interest () that calculates interest based on the current balance and adds it 
to the account
'''


class BankAccount:

    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            self.balance -= withdraw_amount
            return f"Current balance is {self.balance}/- rupees"
        else:
            return "Not sufficient balance"
        
class SavingsAccount(BankAccount):

    def __init__(self, acc_holder, balance, int_rate):
        super().__init__(acc_holder, balance)
        self.int_rate = int_rate

    def add_int(self):
        self.balance += self.balance * self.int_rate / 100
        return self.balance
    

name = input("Enter the account holder name: ")
balance = int(input("Enter the balance in rupees: "))
int_rate = int(input("Enter the interest rate in %: "))
withdraw = int(input("Enter the withdraw amount: "))

obj = SavingsAccount(name, balance, int_rate)

res1 = obj.add_int()

print(f"Current balance after adding interest is: {res1}/- rupees")

res2 = obj.withdraw(withdraw)

print("After withdraw:")
print(res2)
