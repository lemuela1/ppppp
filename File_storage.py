import main
import encryption
import decryption


def Sign_in_account_data(name, account_number, account_password, address, phone_number, Dict: dict, admin, official):
    match_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
        '+', '=', '-', 'Q', 'W', 'E', 'R', 'Y', 'U', 'I', 'O', 'P', '{', '[', ']', '}', '\\', '|', '\'', '\"', ':',
        ';', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '<', '>',
        '/', '?', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ' '
    ]

    DICT = ''

    for each in match_list:
        DICT += Dict.get(each)

    account_file = open("account_file.txt", "r")
    try:
        file_data = account_file.read()
    finally:
        account_file.close()
    initial_balance = 0
    initial_Enable = 'Y'
    file_data = file_data.rstrip('EoF')
    file_data += (
        f"Name:{name}\n"
        f"Account_number:{account_number}\n"
        f"Account_password:{account_password}\n"
        f"Address:{address}\n"
        f"Phone number:{phone_number}\n"
        f"ID: {DICT}\n"
        f"Admin:{admin}\n"
        f"Bank Official:{official}\n"
        f'Balance:{encryption.Encryption(str(initial_balance), Dict)}\n'
        f'Enable:{encryption.Encryption(initial_Enable, Dict)}\n'
        f"\n"
        f"EoF"
    )

    account_file = open('account_file.txt', 'w')
    try:
        account_file.write(file_data)

    finally:
        account_file.close()