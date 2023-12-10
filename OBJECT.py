import decryption
import encryption
import read_account_file
import main


class account_holder:
    Admin = 0
    Official = 0
    accounts = []

    def __init__(self, name, phone_number, address, account_number, account_password, DICT, balance, status):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.account_number = account_number
        self.account_password = account_password
        self.balance = balance
        self.status = status
        self.DICT = DICT

    def deposit_money(self):

        deposit_amount = input("How much you want to deposit?:\n")
        account_number = self.account_number
        Index_num = self.accounts.index(account_number)
        Line = Index_num * 11 + 8
        Keyfile = open('account_file.txt', 'r')
        ignore_content = ''
        try:
            initial_content = Keyfile.read()
            Keyfile.seek(0)
            for each in range(Line):
                ignore_content += Keyfile.readline()
        finally:
            Keyfile.close()
        initial_balance = read_account_file.account_information_get(account_number)[3]
        content = initial_content.replace(ignore_content, '')
        mod_content = content.replace(
            f'{encryption.Encryption(initial_balance, self.DICT)}',
            f'{encryption.Encryption(str(int(initial_balance) + int(deposit_amount)), self.DICT)}',
            1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

    def withdraw_money(self):

        deposit_amount = input("How much you want to withdraw?:\n")
        account_number = self.account_number
        Index_num = self.accounts.index(account_number)
        Line = Index_num * 11 + 8
        Keyfile = open('account_file.txt', 'r')
        ignore_content = ''
        try:
            initial_content = Keyfile.read()
            Keyfile.seek(0)
            for each in range(Line):
                ignore_content += Keyfile.readline()
        finally:
            Keyfile.close()
        initial_balance = read_account_file.account_information_get(account_number)[3]
        if int(initial_balance) - int(deposit_amount) < 0:
            print("\nYou don't have enough money.\n")
            return
        content = initial_content.replace(ignore_content, '')
        mod_content = content.replace(
            f'{encryption.Encryption(initial_balance, self.DICT)}',
            f'{encryption.Encryption(str(int(initial_balance) - int(deposit_amount)), self.DICT)}',
            1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

    def check_balance(self):
        balance = read_account_file.account_information_get(self.account_number)[3]
        print(balance)

    def change_password(self):
        Old_password = input("please enter your previous password:\n")
        if Old_password != self.account_password:
            print('password incorrect, please try again.\n')
            return

        New_password = input("please enter your new password:")
        account_number = self.account_number
        Index_num = self.accounts.index(account_number)
        Line = Index_num * 11 + 2
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
        mod_content = content.replace(
            f'{encryption.Encryption(Old_password, self.DICT)}',
            f'{encryption.Encryption(New_password, self.DICT)}',
            1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

    def menu(self):
        instruction = int(input(
            "What can I help you today?\n"
            "1, deposit money\n"
            "2, withdraw money\n"
            '3, check balance\n'
            '4, change password\n'
            "5, Quit\n"
        ))

        if instruction == 1:
            self.deposit_money()
        elif instruction == 2:
            self.withdraw_money()
        elif instruction == 3:
            self.check_balance()
        elif instruction == 4:
            self.change_password()
        elif instruction == 5:
            return 'Quit'
        else:
            print('Please enter valid instruction.')
            return


class Bank_official(account_holder):
    Official = 1

    def open_account(self):  # Fin
        if self.Official != '1':
            print('Please stop hacking!')
        main.Sign_up()

    def close_account(self):  # Fin, need test
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
        mod_content = content.replace(
                encryption.Encryption('Y', read_account_file.ID_get(account_number)),
                encryption.Encryption('N', read_account_file.ID_get(account_number)),
                1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

    def reopen_account(self):  # Fin, need test
        account_number = input("Enter account number to reopen: ")
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
        mod_content = content.replace(
            encryption.Encryption('N', read_account_file.ID_get(account_number)),
            encryption.Encryption('Y', read_account_file.ID_get(account_number)),
            1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

    def check_total_deposit(self):
        pass

    def Check_exist_account(self):
        pass

    def Search_account(self):
        pass

    def check_bank_account_info(self):
        instruction = input(
            "What do you want to check?\n\n"
            "1, Check total deposit in our bank\n"
            "2, Check all exist account and status\n"
            "3, Search account\n"
            "4, back\n"
        )
        if instruction == 1:
            self.check_total_deposit()
        elif instruction == 2:
            self.Check_exist_account()
        elif instruction == 3:
            self.Search_account()
        elif instruction == 4:
            self.menu()
        else:
            print('Please enter valid instruction.')
            self.check_bank_account_info()

    def menu(self):

        instruction = int(input(
            "What can I help you today?\n"
            "1, open_account\n"
            "2, close_account\n"
            '3, reopen_account\n'
            '4, change password\n'
            '5, check_bank_account_info\n'
            "6, Quit\n"
        ))
        x = None
        if instruction == 1:
            self.open_account()
        elif instruction == 2:
            self.close_account()
        elif instruction == 3:
            self.reopen_account()
        elif instruction == 4:
            self.change_password()
        elif instruction == 5:
            self.check_bank_account_info()
        elif instruction == 6:
            return 'Quit'
        else:
            print('Please enter valid instruction.')
            self.menu()


class System_administrator(account_holder):
    Admin = 1


import getpass


class BearBank:
    def __init__(self):
        self.accounts = []

    def load_data(self):  # FINISHED
        self.accounts.extend(read_account_file.Account_Loading())

    def login(self):  # FINISH COMBINATION
        print('Welcome to BearBank!\nPlease login.\n')
        user_id = input("Please enter your user ID: ")
        password = getpass.getpass("Please enter your password: ")
        user_status = read_account_file.Account_level(user_id)
        if not read_account_file.account_status_get(user_id) == 'Y':
            print('Your account has been lock by bank official,\n'
                  'Please Contact with Bank official.\n')
            return

        if user_id in self.accounts and read_account_file.match_password_in_file(user_id) == password:
            print(f"Welcome, {user_id}!")
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

        current_user.accounts = self.accounts

    def run(self):
        self.load_data()
        self.login()


if __name__ == "__main__":
    bear_bank = BearBank()
    bear_bank.run()
