import decryption
import encryption
import read_account_file
import main
import getpass
import datetime


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
        if not deposit_amount.isalnum():
            print("please enter valid input!")
            return
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

        # record transaction history
        myfile = open('Transaction history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

            NUM = initial_content[initial_content.rindex('total:') + 6:-1]
        total_change = initial_content.replace(
            NUM,
            str(int(NUM) + int(deposit_amount))
        )
        add_content = f'User:{self.name} deposited {deposit_amount} in bank. ({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})\n'
        mod_content = add_content + total_change

        myfile = open('Transaction history.txt', 'w')
        try:
            myfile.write(mod_content)
        finally:
            myfile.close()

    def withdraw_money(self):

        Withdraw_amount = input("How much you want to withdraw?:\n")
        if not Withdraw_amount.isalnum():
            print("please enter valid input!")
            return
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
        if int(initial_balance) - int(Withdraw_amount) < 0:
            print("\nYou don't have enough money.\n")
            return
        content = initial_content.replace(ignore_content, '')
        mod_content = content.replace(
            f'{encryption.Encryption(initial_balance, self.DICT)}',
            f'{encryption.Encryption(str(int(initial_balance) - int(Withdraw_amount)), self.DICT)}',
            1
        )
        mod_data = ignore_content + mod_content

        Keyfile = open('account_file.txt', 'w')
        try:
            Keyfile.write(mod_data)
        finally:
            Keyfile.close()

        # record transaction history
        myfile = open('Transaction history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

            NUM = initial_content[initial_content.rindex('total:') + 6:-1]
        total_change = initial_content.replace(
            NUM,
            str(int(NUM) - int(Withdraw_amount))
        )
        add_content = f'User:{self.name} withdraw {Withdraw_amount} from bank. ({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})\n'
        mod_content = add_content + total_change

        myfile = open('Transaction history.txt', 'w')
        try:
            myfile.write(mod_content)
        finally:
            myfile.close()

    def check_balance(self):
        balance = read_account_file.account_information_get(self.account_number)[3]
        print(f'Your balance is {balance}.\n')

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

    def check_transaction_history(self):

        return_str = ''
        myfile = open('Transaction history.txt', 'r')
        try:
            while True:
                reading = myfile.readline()
                if reading[5:len(self.account_number) + 5] == self.account_number:
                    return_str += reading
                if reading[:5] == 'total':
                    break
        finally:
            myfile.close()

        print(return_str)

    def menu(self):
        instruction = int(input(
            "What can I help you today?\n"
            "1, deposit money\n"
            "2, withdraw money\n"
            '3, check balance\n'
            '4, change password\n'
            '5, see transaction history\n'
            "6, Quit\n"
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
            self.check_transaction_history()
        elif instruction == 6:
            return 'Quit'
        else:
            print('Please enter valid instruction.')
            return


class Bank_official(account_holder):
    Official = 1

    def open_account(self):  # Fin
        if self.Official != 1:
            print('Please stop hacking!')
        account_number = main.Sign_up()

        #### record opening history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'Bank_official {self.name} has opened a user account O.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def close_account(self):  # Fin, need test
        try:
            account_number = input("Enter account number to close: ")
        except ValueError:
            print('Please enter valid input.')
            return
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

        #### record closing history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'Bank_official {self.name} has closed a user account C.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def reopen_account(self):
        account_number = 0
        try:
            account_number = input("Enter account number to reopen: ")
        except ValueError:
            print("Please enter valid input.")
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

        #### record reopening history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'Bank_official {self.name} has reopened a user account R.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def check_total_deposit(self):
        myfile = open('Transaction history.txt', 'r')
        try:
            text = myfile.read()
            print(text[text[:-1].rindex('\n') + 1:])
        finally:
            myfile.close()

    def Check_exist_account(self):
        existing_account = []
        closed_account = []

        myfile = open('account_open_history.txt', 'r')
        try:
            y = 1
            status = ''
            while True:
                x = myfile.readline()
                if x == 'EoF':
                    break

                elif y == 1:
                    status = x[-3]
                    y += 1
                elif y == 2:
                    account_number = x[:-1]
                    if status == 'O':
                        existing_account.append(account_number)
                        status = ''
                    elif status == 'C':
                        existing_account.remove(account_number)
                        closed_account.append(account_number)
                        status = ''
                    elif status == 'R':
                        existing_account.append(account_number)
                        closed_account.remove(account_number)
                        status = ''
                elif y == 3:
                    y = 1

        finally:
            myfile.close()
        print(
            f"Existing_account:\n{existing_account}\n\n"
            f"Closed_account:\n{closed_account}\n\n"
        )

    def Search_account(self):
        Line = 0
        BREAK = 0
        SEARCH = 0
        A_Line = 0
        Return_str = ''
        try:
            METHOD = int(input(
                "Please choose the way you want to search_account:\n"
                "1, by account number.\n"
                "2, by customer name.\n"
                "3, by phone number\n"
            ))
        except ValueError:
            print('\nPlease enter a number\n')
            return

        if METHOD == 1:
            INDEX = encryption.Special_Encryption(input("Please enter the account number:\n"))
            Line = 1
            SEARCH = 15

        elif METHOD == 2:
            INDEX = encryption.Special_Encryption(input("Please enter the customer name:\n"))
            Line = 0
            SEARCH = 5

        elif METHOD == 3:
            INDEX = encryption.Special_Encryption(input("Please enter the phone number:\n"))
            Line = 4
            SEARCH = 13

        else:
            print("Please enter a valid number.")
            return

        myfile = open('account_file.txt', 'r')
        try:
            for each in range(Line):
                x = myfile.readline()

            while True:
                content_index = myfile.readline()
                if content_index == 'EoF':
                    break

                elif content_index[SEARCH:-1] == INDEX:
                    break

                for each in range(10):
                    x = myfile.readline()
                    if x == 'EoF':
                        print('Account can not be found.')
                        BREAK = 1
                        break

                A_Line += 1

                if BREAK == 1:
                    break

            myfile.seek(0)
            for each in range(A_Line * 11):
                x = myfile.readline()

            # Forming info text #
            Return_str += f'Name:{decryption.Decryption(myfile.readline()[5:-1], is_special=True)}\n'
            Account = decryption.Decryption(myfile.readline()[15:-1], is_special=True)
            Dict = read_account_file.ID_get(Account)
            Return_str += f'Account Number:{Account}\n'
            myfile.readline()
            Return_str += f'Address:{decryption.Decryption(myfile.readline()[8:-1], Dict)}\n'
            Return_str += f'Phone Number:{decryption.Decryption(myfile.readline()[13:-1], is_special=True)}\n'
            for each in range(3):
                myfile.readline()
            Return_str += f'Balance:{decryption.Decryption(myfile.readline()[8:-1], Dict)}$\n'

            print(Return_str)

        finally:
            myfile.close()

    def check_all_transaction(self):
        myfile = open('Transaction history.txt', 'r')
        try:
            text = myfile.read()
            print(text)
        finally:
            myfile.close()

    def check_bank_account_info(self):
        try:
            instruction = int(input(
                "What do you want to check?\n\n"
                "1, Check total deposit in our bank\n"
                "2, Check all exist account and status\n"
                "3, Search account\n"
                "4, Check whole transaction history\n"
                "5, back\n"
            ))
        except ValueError:
            print('\nPlease enter a number\n')
            return

        if instruction == 1:
            self.check_total_deposit()
        elif instruction == 2:
            self.Check_exist_account()
        elif instruction == 3:
            self.Search_account()
        elif instruction == 4:
            self.check_all_transaction()
        elif instruction == 5:
            self.menu()
        else:
            print('Please enter valid instruction.')
            self.check_bank_account_info()

    def menu(self):
        instruction = 0
        try:
            instruction = int(input(
                "What can I help you today?\n"
                "1, open_account\n"
                "2, close_account\n"
                '3, reopen_account\n'
                '4, change a user\'s password\n'
                '5, check_bank_account_info\n'
                "6, Quit\n"
            ))
        except ValueError:
            print('\nPlease enter a number\n')

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
    Official = 0

    def open_account(self):  # Fin
        if self.Admin != 1:
            print('Please stop hacking!')
        account_number = main.Sign_up(2)

        #### record opening history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'System administrator {self.name} has opened a Bank official account O.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def close_account(self):  # Fin, need test
        try:
            account_number = input("Enter account number to close: ")
        except ValueError:
            print('Please enter valid input.')
            return
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

        #### record closing history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'System Administrator {self.name} has disable a account C.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def reopen_account(self):
        account_number = 0
        try:
            account_number = input("Enter account number to reopen: ")
        except ValueError:
            print("Please enter valid input.")
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

        #### record reopening history ###
        myfile = open('account_open_history.txt', 'r')
        try:
            initial_content = myfile.read()
        finally:
            myfile.close()

        add_content = f'System administrator {self.name} has reopened a account R.\n{account_number}\n\n'
        new_content = initial_content.replace(initial_content[-3:], '') + add_content + 'EoF'

        myfile = open('account_open_history.txt', 'w')
        try:
            myfile.write(new_content)
        finally:
            myfile.close()

    def Change_user_password(self):
        user_name = ''
        try:
            user_name = input('Please enter user\'s name:')
        except ValueError:
            print('Please enter valid input')

        New_password = input("please enter your new password:")
        account_number = read_account_file.Name_get(user_name, inverse=True)
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
            f'{encryption.Encryption(read_account_file.password_get(account_number), self.DICT)}',
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
        instruction = 0

        print("1. Create Bank Official")
        print("2. Disable Bank Official Login")
        print("3. Enable Bank Official Login")
        print("4. Change User Password")
        print("5. Go Back to Home")

        try:
            instruction = int(input("What would you like to do? Choose a number(1-5): "))
        except ValueError:
            print('\nPlease enter a number\n')

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
            return 'Quit'
        else:
            print('Please enter valid instruction.')
            self.menu()


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
