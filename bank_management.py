import random

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance        

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Updated balance: {self.balance}")

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Updated balance: {self.balance}")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} to {other_account.name}")

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

# storage for accounts
bank_accounts = []

def generate_random_number(length):

    lower_bound = 10 ** (length - 1) 
    upper_bond = (10 ** length) - 1

    return random.randint(lower_bound, upper_bond)

def create_account():
    random_account_num = generate_random_number(10)
    name = input("Enter your name: ")
    balance = float(input("Enter your balance: "))

    new_account = Account(random_account_num, name, balance)
    bank_accounts.append(new_account)

    print("Successfully created an account!")
    print(f"Your Account number is {random_account_num}")

def deposit():

    account_number = int(input("Enter your account number: "))

    if not bank_accounts:
        print("No account created yet")
        return
    
    for acc in bank_accounts:
        if acc.account_number == account_number:
            deposit_input = float(input("Enter amount to deposit: "))
            acc.deposit(deposit_input)
            return
    print("Account not found!")

def withdraw():

    account_number = int(input("Enter your account number: "))

    if not bank_accounts:
        print("No account created yet")
        return

    for acc in bank_accounts:
        if acc.account_number == account_number:
            withdraw_amount = float(input("Enter amount to withdraw"))
            acc.withdraw(withdraw_amount)
            return
        
    print("Account number not found!")

def transfer_fund():
    if not bank_accounts:
        print("No account created yet")
        return
    
    account_number = int(input("Enter your account number: "))

    sender = None

    for acc in bank_accounts:
        if acc.account_number == account_number:
            sender = acc
            break

    if sender is None:
        print("Sender number not found!")
        return
    
    receiver_number = int(input("Enter receiver account: "))
    receiver = None

    for acc in bank_accounts:
        if acc.account_number == receiver_number:
            receiver = acc
            break
    
    if receiver is None:
        print("Receiver not found!")
        return
    
    amount = float(input("Enter amount to transfer: "))

    sender.transfer(receiver, amount)

def view_details():
    if not bank_accounts:
        print("No account created yet")
        return
    
    account_number = int(input("Enter your account number: "))

    for acc in bank_accounts:
        if acc.account_number == account_number:
            print(str(acc))
            return
        
def view_all_account():
    if not bank_accounts:
        print("No account created yet")
        return
    
    for index, acc in enumerate(bank_accounts, 1):
        print(f"{index}. {str(acc)}")


while True: 
    print("""

=== YourBank MyBank ===
          1. Create Account
          2. Deposit Money
          3. Withdraw Money
          4. Transfer Money
          5. View Account Details
          6. View All Account
          7. Exit
""")
    
    user_choice = input("Enter your choice: ")

    match user_choice:
        case "1" :
            create_account()
        case "2":
            deposit()
        case "3":
            withdraw()
        case "4":
            transfer_fund()
        case "5":
            view_details()
        case "6":
            view_all_account()
        case "7":
            print("Thank you for trusting YourBank MyBank.")
            print("Exiting the program....")
            break
        case _:
            print("Invalid input. Please choose between 1 -7")
            


            
            
            

        