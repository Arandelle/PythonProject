import random

class AuthSystem:
    def __init__(self):
        self.loggedIn = None # store the account that is logged in
        self.accounts = [] # store account to avoid global variable

    def register_account(self,acc_num, name, pin, balance ):

        new_account = Account(acc_num, name,pin, balance)
        self.accounts.append(new_account)
        print(f"Account created for {name}. acc#: {acc_num}")

    def login(self, acc_num, pin):
        for acc in self.accounts:
            if acc.account_number == acc_num and acc.checkPin(pin):
                self.loggedIn = acc
                print(f"Successfully loggedin")
                return True
        print("Invalid credentials")
        return False
    
class Account:
    def __init__(self, account_number, name,pin, balance):
        self.account_number = account_number
        self.name = name
        self._pin = pin # private pin
        self.balance = balance

    def checkPin(self, pin): # encapsulation
        return self._pin == pin


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

# create global auth
auth = AuthSystem()

def generate_random_number(length):

    lower_bound = 10 ** (length - 1) 
    upper_bond = (10 ** length) - 1

    return random.randint(lower_bound, upper_bond)

def create_account():
    random_account_num = generate_random_number(10)
    name = input("Enter your name: ")
    pin = int(input("Pin: "))
    balance = float(input("Enter your balance: "))

    auth.register_account(random_account_num, name, pin, balance)

    print("Successfully created an account!")
    print(f"Your Account number is {random_account_num}")

def login():
    acc_num = int(input("Account Number: "))
    acc_pin = int(input("PIN: "))
    auth.login(acc_num, acc_pin)

def deposit():
    deposit = float(input("Amount: "))
    auth.loggedIn.deposit(deposit)
    return

def withdraw():
    withdraw_amount = float(input("Enter amount to withdraw: "))
    auth.loggedIn.withdraw(withdraw_amount)
    return

def transfer_fund():
    receiver = None
    receiver_number = int(input("Enter receiver account: "))
    
    for acc in auth.accounts:
        if acc.account_number == receiver_number:
            receiver = acc
            break
    
    if receiver is None:
        print("Receiver not found!")
        return
    
    amount = float(input("Enter amount to transfer: "))

    auth.loggedIn.transfer(receiver, amount)

def view_details():
    print(str(auth.loggedIn))
    return
        
def view_all_account():
    if not auth.accounts:
        print("No account created yet")
        return
    
    for index, acc in enumerate(auth.accounts, 1):
        print(f"{index}. {str(acc)}")


def logout():
    auth.loggedIn = None
    return

while True: 
    if auth.loggedIn != None:
        print("""

        === YourBank MyBank ===
                1. Deposit Money
                2. Withdraw Money
                3. Transfer Money
                4. View Account Details
                5. Logout
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
                print("Thank you for trusting YourBank MyBank.")
                print("Loggin out...")
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
        
        user_choice = input("Enter what you do: ")

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
                



            
            
            

        