import json, getpass
from datetime import datetime


class BearBank:
    def __init__(self):
        self.accounts = []
        self.customers = {}
        self.logged_in_user = None

    def load_data(self):
        try:
            with open('bear_bank_data.json', 'r') as file:
                data = json.load(file)
                self.accounts = data.get('accounts', [])
                self.customers = data.get('customers', {})
        except FileNotFoundError:
            pass

    def save_data(self):
        data = {'accounts': self.accounts, 'customers': self.customers}
        with open('bear_bank_data.json', 'w') as file:
            json.dump(data, file, indent=2)

    def display_menu(self):
        print("1. Open Account (Bank Official Only)")
        print("2. Close Account (Bank Official Only)")
        print("3. Deposit Money")
        print("4. Search Accounts(Bank Official Only)")
        print("5. Change Password")
        print("6. Check Transactions")
        print("7. Quit")

    def is_bank_official(self):
        user_id = input("Enter your user ID: ")
        password = getpass.getpass("Enter your password: ")

        return user_id == "admin" and password == "adminpass"

    def open_account(self):
        if not self.is_bank_official():
            print("Only bank officials can open an account.")
            return

        account_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        opening_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        account_info = {
            'account_number': account_number,
            'customer_name': customer_name,
            'opening_date': opening_date,
            'closed': False,
            'transactions': []
        }
        self.accounts.append(account_info)
        customer_password = getpass.getpass("Enter customer password: ")
        self.customers[customer_name] = customer_password
        print(f"Account for {customer_name} opened successfully.")

    def close_account(self):
        if not self.is_bank_official():
            print("Only bank officials can close an account.")
            return
        account_number = input("Enter account number to close: ")
        for account in self.accounts:
            if account['account_number'] == account_number and not account['closed']:
                account['closed'] = True
                account['closing_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                account['closed_by'] = self.logged_in_user
                print(f"Account {account_number} closed successfully.")
                return

        print(f"Account {account_number} not found or already closed.")

    def deposit_money(self):
        account_number = input("Enter account number to deposit money: ")
        for account in self.accounts:
            if account['account_number'] == account_number and not account['closed']:
                amount = float(input("Enter the amount to deposit: "))
                customer_name = input("Enter your customer name: ")
                customer_password = getpass.getpass("Enter your customer password: ")
                if customer_name in self.customers and self.customers[customer_name] == customer_password:
                    transaction = {'type': 'deposit', 'amount': amount,
                                   'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    account['transactions'].append(transaction)
                    print(f"Successfully deposited {amount} into account {account_number}.")
                    return
                else:
                    print("Invalid customer name or password. Transaction aborted.")
                    return
        print(f"Account {account_number} not found or closed.")

    def search_accounts(self):
        if not self.is_bank_official:
            print("Only Bank official can search for accounts.")
            return
        search_term = input("Enter account number, customer name, or phone number: ")
        for account in self.accounts:
            if not account['closed'] and (search_term in account['account_number'] or
                                          search_term in account['customer_name']):
                print(f"Account Number: {account['account_number']}")
                print(f"Customer Name: {account['customer_name']}")
                print(f"Opening Date: {account['opening_date']}")
                if 'closing_date' in account:
                    print(f"Closing Date: {account['closing_date']}")
                    print(f"Closed By: {account['closed_by']}")
                print("===")

    def change_password(self):
        user_id = input("Enter your user ID: ")
        current_password = getpass.getpass("Enter your current password: ")
        if user_id in self.customers and self.customers[user_id] == current_password:
            new_password = getpass.getpass("Enter your new password: ")
            self.customers[user_id] = new_password
            print("Password changed successfully.")
        else:
            print("Invalid user ID or password. Password change aborted.")

    def check_transactions(self):
        account_number = input("Enter account number to check transactions: ")
        for account in self.accounts:
            if account['account_number'] == account_number and not account['closed']:
                for transaction in account['transactions']:
                    print(
                        f"Type: {transaction['type']}, Amount: {transaction['amount']}, Time: {transaction['timestamp']}")
                return
        print(f"Account {account_number} not found or closed.")

    def login(self):
        user_id = input("Enter your user ID: ")
        password = getpass.getpass("Enter your password: ")
        if user_id in self.customers and self.customers[user_id] == password:
            self.logged_in_user = user_id
            print(f"Welcome, {user_id}!")
            print(f"Last Login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        elif self.is_bank_official():
            self.logged_in_user = user_id
            print(f"Welcome, {user_id}!")
            print(f"Last Login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Invalid user ID or password. Login failed.")

    def run(self):
        self.load_data()
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.close_account()
            elif choice == '3':
                self.deposit_money()
            elif choice == '4':
                self.search_accounts()
            elif choice == '5':
                self.change_password()
            elif choice == '6':
                self.check_transactions()
            elif choice == '7':
                self.save_data()
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bear_bank = BearBank()
    bear_bank.run()
