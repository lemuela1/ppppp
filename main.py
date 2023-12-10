import encryption
import decryption
import File_storage
import OBJECT


def Sign_up(classification=0):

    if classification == 1:
        Admin = 1
        official = 0
    elif classification == 2:
        official = 1
        Admin = 0
    elif classification == 0:
        Admin = 'O'
        official = 'N'

    account_number_setup = input("Please enter your account number:")
    account_password_setup, DICT = encryption.Encryption(input("Please enter your account password:"))
    account_name_setup = encryption.Encryption(input("Please enter your account name:"), DICT)
    account_address_setup = encryption.Encryption(input("Please enter your address:"), DICT)
    account_phone_setup = encryption.Encryption(input("Please enter your phone number:"), DICT)
    File_storage.Sign_in_account_data(
        account_name_setup, account_number_setup, account_password_setup, account_address_setup, account_phone_setup,
        DICT, encryption.Encryption(str(Admin), DICT), encryption.Encryption(str(official), DICT)
    )


def main():
    Bear_bank = OBJECT.BearBank
    Bear_bank.run()


if __name__ == '__main__':
    main()
