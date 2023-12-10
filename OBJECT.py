import decryption
import read_account_file
import main


class account_holder:
    Admin = 0
    Official = 0

    def __init__(self, name, phone_number, address, account_number, account_password, DICT, balance, status):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.account_number = account_number
        self.account_password = account_password
        self.balance = balance
        self.status = status
        self.DICT = DICT


class Bank_official(account_holder):
    Official = 1


class System_administrator(account_holder):
    Admin = 1

    def change_password(self, new_password):
        self.account_password = new_password

        Keyfile = open('account_file.txt', 'w+')
        try:
            pass

        finally:
            Keyfile.close()
        print("Password changed successfully.")


import json, getpass
from datetime import datetime


class BearBank:
    def __init__(self):
        self.accounts = []

    def load_data(self):  # FINISHED
        self.accounts.extend(read_account_file.Account_Loading())

    def save_data(self):
        data = {'accounts': self.accounts, 'customers': self.customers}
        with open('bear_bank_data.json', 'w') as file:
            json.dump(data, file, indent=2)

    def display_menu(self):  # FIN
        print("1. Open Account (Bank Official Only)")
        print("2. Close Account (Bank Official Only)")
        print("3. Deposit Money")
        print("4. Search Accounts(Bank Official Only)")
        print("5. Change Password")
        print("6. Check Transactions")
        print("7. Quit")

    def open_account(self):  # Fin
        if current_user.Official == 0:
            print("Only bank officials can open an account.")
            return

        main.Sign_up()
        # opening_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # opening_date removed because of issue of changing data.

    def close_account(self):  # Fin, need test
        if current_user.Official == 0:
            print("Only bank officials can close an account.")
            return
        account_number = input("Enter account number to close: ")
        Index_num = self.accounts.index(account_number)
        if account_number in self.accounts is False:
            print(f"Account {account_number} not found or already closed.")
            return

        Line = Index_num * 11 + 9
        Keyfile = open('account_file.txt', 'r')
        ignore_content = ''
        try:
            initial_content = Keyfile.read()
            Keyfile.seek(0)
            for each in range(Line):
                ignore_content += Keyfile.readline()
        finally:
            Keyfile.close()

        content = initial_content.replace(ignore_content, '')
        mod_content = content.replace('y', 'N', 1)
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

        # account['closing_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

    def login(self):  # FINISH COMBINATION
        print('Welcome to BearBank!\nPlease login.\n')
        user_id = input("Please enter your user ID: ")
        password = getpass.getpass("Please enter your password: ")
        user_status = read_account_file.Account_level(user_id)
        if not read_account_file.account_status_get(user_status) == 'Y':
            print('Your account has been lock by bank official,\n'
                  'Please Contact with Bank official.\n')
            return

        if user_id in self.accounts and read_account_file.match_password_in_file(user_id) == password:
            print(f"Welcome, {user_id}!")
            # print(f"Last Login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Invalid user ID or password. Login failed.")

        ### current_user log in ###
        global current_user
        if user_status == ['O', 'N']:
            info = read_account_file.account_information_get(user_id)
            current_user = account_holder(
                account_number=user_id,
                account_password=password,
                name=info[0],
                address=info[1],
                phone_number=info[2],
                balance=info[3],
                status=info[4],
                DICT=read_account_file.ID_get(user_id)
            )

        elif user_id == ['1', '0']:
            info = read_account_file.account_information_get(user_id)
            current_user = System_administrator(
                account_number=user_id,
                account_password=password,
                name=info[0],
                address=info[1],
                phone_number=info[2],
                balance=info[3],
                status=info[4],
                DICT=read_account_file.ID_get(user_id)
            )

        elif user_id == ['0', '1']:
            info = read_account_file.account_information_get(user_id)
            current_user = Bank_official(
                account_number=user_id,
                account_password=password,
                name=info[0],
                address=info[1],
                phone_number=info[2],
                balance=info[3],
                status=info[4],
                DICT=read_account_file.ID_get(user_id)
            )

    def run(self):
        self.load_data()
        self.login()
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
