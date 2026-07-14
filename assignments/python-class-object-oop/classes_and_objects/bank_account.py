"""
## 2. Bank Account Class  *(Medium)*

=================================================
BANK ACCOUNT CLASS
=================================================

Problem Statement:
Write a Python CLASS called `BankAccount`
that represents a simple bank account. Each
account has an account holder's name, a
unique account number, and a balance that
starts at 0 unless an opening balance is
given.

The class must support deposits, withdrawals,
and balance checks. Reject invalid operations
(negative amounts, overdrafts) by printing a
clear message — do NOT crash.

-------------------------------------------------
Instructions:
1. Define a class:
      class BankAccount:
2. Constructor:
      def __init__(self, name, account_number,
                   opening_balance=0):
          - validate that opening_balance >= 0
          - store name, account_number, balance
            on `self`
3. Instance methods:
      - deposit(self, amount)
            * reject amount <= 0 with a message
            * otherwise add to balance
      - withdraw(self, amount)
            * reject amount <= 0
            * reject if amount > balance
            * otherwise subtract from balance
      - get_balance(self)
            * return the current balance
      - __str__(self)
            * return a friendly string like:
              "Account[001 - Alice]: $500"
4. In the driver code:
      - create AT LEAST TWO accounts
      - perform some valid deposits / withdraws
      - perform AT LEAST ONE invalid operation
        (negative amount or overdraft) on each
        account to show the rejection message
      - print each account using print(acc),
        which triggers __str__
5. Do NOT use:
   - class-level mutable defaults (e.g. a list
     as default argument)
   - global variables

-------------------------------------------------
Input Example:
a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob",   "002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)   # overdraft -> rejected
a2.deposit(-50)     # invalid   -> rejected
a2.deposit(300)

Output Example:
Insufficient funds for Alice (balance=600, asked=2000)
Deposit amount must be > 0 (got -50)
Account[001 - Alice]: $600
Account[002 - Bob]:   $300

-------------------------------------------------
Explanation:
- `self.balance` is independent for every
  object, so Alice and Bob keep separate
  balances.
- Validation in `deposit` and `withdraw` shows
  how methods use `self` to read AND update
  state on the same object.
- `__str__` returns the human-readable form
  used by print().
=================================================

"""


class BankAccount:

    def __init__(self, name, account_number, balance = 0):

        self.acc_name = name
        self.acc_number = account_number

        if balance < 0:
            print("Balance can not be negative.")
            self.acc_balance = 0
        else:
            self.acc_balance = balance

    def deposit(self, amount):

        if amount < 0:
            print("Deposite amount can not be negative.")
        else:
            self.acc_balance += amount

    def withdraw(self, amount):

        if amount < 0:
            print("Withdraw amount can not be negative.")
        elif amount > self.acc_balance:
            print("Not enough balance.")
        else:
            self.acc_balance -= amount
    
    def get_balance(self):

        return self.acc_balance
    
    def __str__(self):

        return f"Account{self.acc_number} - {self.acc_name}: ${self.acc_balance}"
    

n = int(input("Enter the number of accounts: "))

account_records = []

for i in range(n):
    name = input("Enter your name: ")
    account_number = int(input("Enter your account number: "))
    balance = int(input("Enter the balance in $: "))

    account_records.append({
        "name": name,
        "account_number": account_number,
        "balance": balance,
    })

accounts = []

for i in account_records:
    accounts.append(BankAccount(**i))

for acc in accounts:
    print(f"Processing for account name: {acc.acc_name}")

    dep_amount = int(input("Enter the deposite amount in $: "))
    acc.deposit(dep_amount)

    withdraw_amount = int(input("Enter withdrawal amount in $: "))
    acc.withdraw(withdraw_amount)

print("Final Account Details: ")
for acc in accounts:
    print(acc)
