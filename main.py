import encryption
import decryption
import File_storage


class account_holder:
    Admin = 0
    Official = 0

    def __init__(self, name, phone_number, address, account_number, account_password, DICT):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.account_number = account_number
        self.account_password = account_password
        self.DICT = DICT


class administrator(account_holder):
    Admin = 1


class bank_official(account_holder):
    Official = 1


def Sign_up():
    classification = int(input(
        "Are you bank official or system administrator?\n"
        "Type 1 if you are bank official\n"
        "Type 2 if you are system administrator.\n"
        "Type 0 if you are account holder.\n"
        "\n"
        "please enter your instruction:"
    ))

    account_class, DICT = encryption.Encryption(str(classification))

    if classification == 1:
        Sign_up_2(DICT, 0, 1)

    elif classification == 2:
        Sign_up_2(DICT, 1, 0)

    elif classification == 0:
        Sign_up_2(DICT, 0, 0)

    else:
        print("please enter a valid instruction")
        Sign_up()


def Sign_up_2(DICT, Admin, official):
    account_number_setup = encryption.Encryption(input("Please enter your account number:"), DICT)
    account_password_setup = encryption.Encryption(input("Please enter your account password:"), DICT)
    account_name_setup = encryption.Encryption(input("Please enter your account name:"), DICT)
    account_address_setup = encryption.Encryption(input("Please enter your address:"), DICT)
    account_phone_setup = encryption.Encryption(input("Please enter your phone number:"), DICT)
    File_storage.Storage_account_data(
        account_name_setup, account_number_setup, account_password_setup, account_address_setup, account_phone_setup,
        DICT, encryption.Encryption(str(Admin), DICT), encryption.Encryption(str(official), DICT)
    )


def Sign_in():
    pass


def instruction_1():
    x = int(input(
        "Welcome to online Bear Bank!\n"
        "Please place your instruction:\n\n"
        "1. Sign in your account.\n"
        "2. Sign up your account.\n\n"
        "enter 1 or 2 to select your instruction:\n"
    ))

    if x == 1:
        Sign_in()

    elif x == 2:
        Sign_up()

    else:
        print("Please enter a valid instruction.")
        instruction_1()


def main():
    while True:
        instruction_1()
        pass


if __name__ == '__main__':
    main()
