import random
import json
from datetime import datetime

class AuthSystem:
    def __init__(self):
        self.loggedIn = None # store the account that is logged in
        self.accounts = [] # store account to avoid global variable

    def register_account(self,acc_num, name, pin, balance ):

        new_account = Account(acc_num, name,pin, balance)
        self.accounts.append(new_account)
        self.save_accounts()
        print(f"Account created for {name}. acc#: {acc_num}")

    def login(self, acc_num, pin):
        for acc in self.accounts:
            if acc.account_number == acc_num and acc.checkPin(pin):
                self.loggedIn = acc
                print(f"Successfully loggedin")
                return True
        print("Invalid credentials")
        return False
    
    def save_accounts(self):
        with open("bank_accounts.json", "w") as file:
            json.dump([{
                "account_number" : account.account_number,
                "name": account.name,
                "pin" : account._pin, # create like this instead of account.__dict__ to rename the _pin as pin
                "balance" : account.balance,
                "transaction_record": [t.to_dict() for t in account.transaction_record]
            }
            for account in self.accounts], file, indent=4)

    def delete_account(self, pin):
        if self.loggedIn and self.loggedIn.checkPin(pin):
            print(f"Successfully delete an account {self.loggedIn.account_number}")
            self.accounts.remove(self.loggedIn)
            self.loggedIn = None
            self.save_accounts()
            return True
        else:
            print("Invalid pin!")
            return False

    def edit_account(self, new_name, new_pin):
        if self.loggedIn:
            if new_name.strip() != "":
                self.loggedIn.name = new_name
            if new_pin.strip() != "":
                if len(new_pin) == 4:
                    self.loggedIn._pin = new_pin
                else:
                    print("Pin must be 4 digits")
                    return
            if new_name.strip() == "" and new_pin.strip() == "":
                print("Your details remain to it's original value")
                return
            self.save_accounts()
            print("Successfully updated!")

    def load_Accounts(self):
        try:
            self.accounts.clear() # clear the list to avoid duplicates
            with open("bank_accounts.json", "r") as file:
                accounts = json.load(file)
                for acc in accounts:
                    new_account = Account(**acc)
                    self.accounts.append(new_account)

        except FileNotFoundError:
            print("File not found. Create an account first")

class Account:
    def __init__(self, account_number, name,pin, balance):
        self.account_number = account_number
        self.name = name
        self._pin = str(pin) # private pin
        self.balance = balance
        self.transaction_record = []

    def checkPin(self, pin): # encapsulation
        return self._pin == str(pin)


    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction("Deposit", amount, self.balance)
        self.transaction_record.append(transaction)
        print(f"Deposited {amount}. Updated balance: {self.balance}")

    def withdraw(self, amount):
        
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            transaction = Transaction("Withdraw", amount, self.balance)
            self.transaction_record.append(transaction)
            print(f"Withdrew {amount}. Updated balance: {self.balance}")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            other_account.balance += amount
            transaction = Transaction("Deposit", amount, self.balance, other_account)
            self.transaction_record.append(transaction)
            print(f"Transferred {amount} to {other_account.name}")

    def transaction_record(self):
        for transaction in self.transaction_record:
            print(f"Type: {transaction.type}, Date: {transaction.date}, Amount: {transaction.amount}, Updated amount: {transaction.balance}, Receiver: {transaction.receiver}")

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"

class Transaction:
    def __init__(self, type, amount,balance_after, receiver = None):
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.receiver = receiver
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "type" : self.type,
            "amount" : self.amount,
            "balance" : self.balance_after,
            "reciever" : self.receiver,
            "date" : self.date
        }

    def __str__(self):
        if self.receiver:
            return f"[{self.date}] {self.type}: {self.amount}, Balance: {self.balance_after}, Receiver: {self.receiver}"
        return f"[{self.date}] {self.type}: {self.amount}, Balance: {self.balance_after}"

# create global auth
auth = AuthSystem()

def generate_random_number(length):

    lower_bound = 10 ** (length - 1) 
    upper_bond = (10 ** length) - 1

    return random.randint(lower_bound, upper_bond)

def custom_input(prompt: str):
    # input wrapper that cancels if * is enterred
    value = input(prompt)
    if value.strip() == "*":
        print("Operation cancelled")
        return None
    return value

def create_account():

    try:
        print("Enter * to cancel")

        random_account_num = generate_random_number(10)
        name = custom_input("Enter your name: ")
        if name is None: return

        pin = custom_input("Pin: ")
        if pin is None : return
        if len(pin) != 4:
            print("Pin must be 4 digits")
            return
        
        balance_input = custom_input("Enter your balance: ")
        if balance_input is None: return

        balance = float(balance_input)
        auth.register_account(random_account_num, name, pin, balance)

        print("Successfully created an account!")
        print(f"Your Account number is {random_account_num}")
    
    except ValueError :
        print("Invalid Input. Please try again")

def login():
    try: 
        print("Enter * to cancel")

        acc_num_input = custom_input("Account Number: ")
        if acc_num_input is None : return
        # convert the input to int 
        acc_num = int(acc_num_input)

        acc_pin = custom_input("PIN: ")
        if acc_pin is None : return
        auth.login(acc_num, acc_pin)

    except ValueError :
        print("Invalid input. Please try again")

def deposit():
    try:
        print("Enter * to cancel")
        deposit_input = custom_input("Amount: ")
        if deposit_input is None: return
        deposit = float(deposit_input)
        auth.loggedIn.deposit(deposit)
        auth.save_accounts()
        return
    except ValueError:
        print("Invalid input. Please try again")

def withdraw():
    try:
        print("Enter * to cancel")
        withdraw_input = custom_input("Amount to withdraw: ")
        if withdraw_input is None: return

        withdraw_amount = float(withdraw_input)
        auth.loggedIn.withdraw(withdraw_amount)
        auth.save_accounts()
        return
    except ValueError:
        print("Invalid input. Please try again")

def transfer_fund():
    try:
        print("Enter * to cancel")
        receiver = None
        receiver_input = custom_input("Enter receiver account: ")
        if receiver_input is None : return

        receiver_number = int(receiver_input)
        
        for acc in auth.accounts:
            if acc.account_number == receiver_number:
                receiver = acc
                break
        
        if receiver is None:
            print("Receiver not found!")
            return
        amount_input = custom_input("Amount to transfer: ")
        if amount_input is None: return

        amount = float(amount_input)

        auth.loggedIn.transfer(receiver, amount)
        auth.save_accounts()
    except ValueError:
        print("Invalid input. Please try again.")

def view_details():
    print(str(auth.loggedIn))
    return

def view_transaction():
        for t in auth.loggedIn.transaction_record:
            print(t)

def view_all_account():
    if not auth.accounts:
        print("No account created yet")
        return
    
    for index, acc in enumerate(auth.accounts, 1):
        print(f"{index}. {str(acc)}")

def delete_account():
    print("Enter * to cancel")
    pin_input = custom_input("Enter your pin: ")
    if pin_input is None: return
    auth.delete_account(pin_input)

def edit_account():
    print("Enter * to cancel")
    print("Enter to keep the current value")
    new_name = custom_input("Enter your name: ")
    if new_name is None: return
    new_pin = custom_input("Enter your new pi: ")
    if new_pin is None: return
    auth.edit_account(new_name, new_pin)

def logout():
    auth.loggedIn = None
    print("Thank you for trusting YourBank MyBank.")
    print("Logged out!")
    return


# load accounts from the json, so the accounts list will have the data
auth.load_Accounts()

while True: 
    if auth.loggedIn != None:
        print(f"""
        === YourBank MyBank ===
        Welcome {auth.loggedIn.name}
        1. Deposit Money
        2. Withdraw Money
        3. Transfer Money
        4. View Account Details
        5. Transaction Record
        6. Delete My Account
        7. Edit My Account
        8. Logout
        """)
            
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                deposit()
            case "2":
                withdraw()
            case "3":
                transfer_fund()
            case "4":
                view_details() 
            case "5":
                view_transaction()
            case "6":
                delete_account()
            case "7":
                edit_account()
            case "8":
                logout()
            case _:
                print("Invalid input. Please choose between 1 -7")
                    
    else:
        print("""
        Welcome to Mybank YourBank
        1. Login
        2. Create an Account
        3. Exit
    """)
        
        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                login()
            case "2":
                create_account()
            case "3":
                print("Exiting the program")
                break
            case _:
                print("Invalid input value")
                



            
            
            

        