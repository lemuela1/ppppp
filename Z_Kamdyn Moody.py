# Bear Bank
# Kamdyn Moody, kamdyn.moody@gmail.com
# Parishrut Rajak, pr8428s@missouristate.edu
# Dingzen Yu, dy4874s@missouristate.edu

from datetime import datetime


class SystemAdministrator:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully.")

    def create_official_login(self, bank_system, username, password):
        bank_system.add_official(username, password)
        print(f"Bank official {username} created.")
        bank.administrator.admin_menu(bank)

    def enable_official_login(self, bank_system, username):
        if username in bank_system.officials:
            bank_system.officials[username].enabled = True
            print(f"Bank official {username}'s login enabled.")
            bank.administrator.admin_menu(bank)
        else:
            print(f"Bank official {username} not found.")
            bank.administrator.admin_menu(bank)

    def disable_official_login(self, bank_system, username):
        if username in bank_system.officials:
            bank_system.officials[username].enabled = False
            print(f"Bank official {username}'s login disabled.")
            bank.administrator.admin_menu(bank)

        else:
            print(f"Bank official {username} not found.")
            bank.administrator.admin_menu(bank)

    def change_user_password(self, bank_system, full_name, date_of_birth, new_password):
        for username, account_holder in bank_system.accounts.items():
            if account_holder.full_name == full_name and account_holder.date_of_birth == date_of_birth:
                account_holder.password = new_password
                print(f"Password changed for {full_name}'s account.")
                return
        print("User not found.")

    def admin_menu(self, bank_system):
        print("1. Create Bank Official")
        print("2. Enable Bank Official Login")
        print("3. Disable Bank Official Login")
        print("4. Change User Password")
        print("5. Go Back to Home")
        choice = input("What would you like to do? Choose a number(1-5): ")

        if choice == "1":
            username = input("Enter new Bank Official username: ")
            password = input("Enter new Bank Official password: ")
            self.create_official_login(bank_system, username, password)
        elif choice == "2":
            username = input("Enter Bank Official username to enable login: ")
            self.enable_official_login(bank_system, username)
        elif choice == "3":
            username = input("Enter Bank Official username to disable login: ")
            self.disable_official_login(bank_system, username)
        elif choice == "4":
            full_name = input("Enter full name of the user whose password needs to be changed: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD) of the user: ")
            new_password = input("Enter new password: ")
            self.change_user_password(bank_system, full_name, date_of_birth, new_password)
        elif choice == '5':
            pass
        # insert location for home where option to choose user(AccountHolder, BankOfficial, Administrator)
        else:
            print("Invalid choice.")


# insert bank official code
class BankOfficial:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.enabled = True


# insert account holder
class AccountHolder:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.enabled = True


# bring together users
class BankSystem:
    def __init__(self):
        self.administrator = None
        self.officials = {}
        self.accounts = {}

    def add_administrator(self, username, password):
        self.administrator = SystemAdministrator(username, password)
        print("System administrator created.")

    def add_official(self, username, password):
        self.officials[username] = BankOfficial(username, password)
        print(f"Bank official {username} created.")

    def create_account_holder(self, username, password, full_name, date_of_birth, phone_number, address,
                              initial_balance=0):
        new_account_holder = AccountHolder(username, password, full_name, date_of_birth, phone_number, address,
                                           initial_balance)
        return new_account_holder

    def authenticate(self, username, password):
        if username in self.officials and self.officials[username].password == password and self.officials[
            username].enabled:
            return "BankOfficial"
        elif username in self.accounts and self.accounts[username].password == password:
            return "AccountHolder"
        elif self.administrator.username == username and self.administrator.password == password:
            return "Administrator"
        else:
            return None


# Sample usage:
bank = BankSystem()

# Adding users
admin_username = input("Enter administrator username: ")
admin_password = input("Enter administrator password: ")
bank.add_administrator(admin_username, admin_password)

# Authentication and operations
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

user_type = bank.authenticate(username_input, password_input)
if user_type == "Administrator":
    print("You are logged in as an Administrator.")
    bank.administrator.admin_menu(bank)  # Invoke admin_menu for admin actions
elif user_type == "BankOfficial":
    print("You are logged in as a Bank Official.")
    # Perform bank official operations here
elif user_type == "AccountHolder":
    print("You are logged in as an Account Holder.")
    # Perform account holder operations here
else:
    print("Invalid username or password.")