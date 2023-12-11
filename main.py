import decryption
import encryption
import File_storage
import OBJECT
import read_account_file
import sys


class BearBank:
    def __init__(self):
        self.accounts = []

    def load_data(self):  # FINISHED
        self.accounts.extend(read_account_file.Account_Loading())

    def login(self):  # FINISH COMBINATION
        print('Welcome to BearBank!\nPlease login.\n')
        while True:
            user_id = input("Please enter your user ID: ")
            if user_id in self.accounts:
                break
            print('User id does not exist.')

        password = input("Please enter your password: ")
        user_status = read_account_file.Account_level(user_id)
        if not read_account_file.account_status_get(user_id) == 'Y':
            print('Your account has been lock by bank official,\n'
                  'Please Contact with Bank official.\n')
            sys.exit()

        while True:
            if read_account_file.match_password_in_file(user_id) == password:
                print(f"\nWelcome, {read_account_file.account_information_get(user_id)[0]}!\n")
                break
            else:
                print("Wrong password. try it again.")
                password = input("Please enter your password: ")

        ### current_user log in ###
        global current_user

        if user_status == ['O', 'N']:
            info = read_account_file.account_information_get(user_id)
            current_user = OBJECT.account_holder(
                account_number=user_id,
                account_password=password,
                name=info[0],
                address=info[1],
                phone_number=info[2],
                balance=info[3],
                status=info[4],
                DICT=read_account_file.ID_get(user_id)
            )

        elif user_status == ['1', '0']:
            info = read_account_file.account_information_get(user_id)
            current_user = OBJECT.System_administrator(
                account_number=user_id,
                account_password=password,
                name=info[0],
                address=info[1],
                phone_number=info[2],
                balance=info[3],
                status=info[4],
                DICT=read_account_file.ID_get(user_id)
            )

        elif user_status == ['0', '1']:
            info = read_account_file.account_information_get(user_id)
            current_user = OBJECT.Bank_official(
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


def Sign_up(classification=0):
    Admin = 'O'
    official = 'N'
    if classification == 1:
        Admin = 1
        official = 0
    elif classification == 2:
        official = 1
        Admin = 0
    while True:
        account_number = encryption.Special_Encryption(input("Please enter your account number:"))
        if account_number in read_account_file.Account_Loading():
            print("This account_name already exist, please try other names.")
        else:
            account_number_setup = account_number
            break
    account_password_setup, DICT = encryption.Encryption(input("Please enter your account password:"))
    account_name_setup = encryption.Special_Encryption(input("Please enter your account name:"))
    account_address_setup = encryption.Encryption(input("Please enter your address:"), DICT)
    account_phone_setup = encryption.Special_Encryption(input("Please enter your phone number:"))
    File_storage.Sign_in_account_data(
        account_name_setup, account_number_setup, account_password_setup, account_address_setup, account_phone_setup,
        DICT, encryption.Encryption(str(Admin), DICT), encryption.Encryption(str(official), DICT)
    )
    return decryption.Decryption(account_number, is_special=True)


def main():
    bear_bank = BearBank()
    bear_bank.run()
    while True:
        Q = current_user.menu()
        if Q == 'Quit':
            print(
                'Thank you for using Bear bank,\n'
                'We wish you have a good day!'
            )

            break


if __name__ == '__main__':
    main()
