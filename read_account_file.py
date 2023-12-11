import decryption


def raw_password_listing():
    myFile = open('account_file.txt', 'r')
    try:
        Password_list = []
        myFile.seek(0)
        for each in range(2):
            x = myFile.readline()
            if x == 'EoF':
                break
        account_password = myFile.readline()
        Password_list.append(account_password[17:-1])

        Time_to_break = 0

        while True:
            for each in range(10):
                x = myFile.readline()
                if x == 'EoF':
                    Time_to_break = 1
                    break
            account_password = myFile.readline()
            Password_list.append(account_password[17:-1])
            if Time_to_break == 1:
                break
        Password_list.pop()

    finally:
        myFile.close()

    return Password_list


def Name_listing():
    myFile = open('account_file.txt', 'r')
    try:
        name_list = []
        myFile.seek(0)

        NAME = myFile.readline()
        name_list.append(decryption.Decryption(NAME[5:-1], is_special=True))

        Time_to_break = 0

        while True:
            for each in range(10):
                x = myFile.readline()
                if x == 'EoF':
                    Time_to_break = 1
                    break
            NAME = myFile.readline()
            if NAME == 'EoF':
                Time_to_break =1
                break

            name_list.append(decryption.Decryption(NAME[5:-1], is_special=True))
            if Time_to_break == 1:
                break
    finally:
        myFile.close()

    return name_list


def Account_Loading():
    myFile = open('account_file.txt', 'r')
    try:
        Account_list = []
        myFile.seek(0)
        for each in range(1):
            x = myFile.readline()
            if x == 'EoF':
                break
        Account_number = myFile.readline()
        Account_list.append(decryption.Decryption(Account_number[15:-1], is_special=True))

        Time_to_break = 0

        while True:
            for each in range(10):
                x = myFile.readline()
                if x == 'EoF':
                    Time_to_break = 1
                    break
            Account_number = myFile.readline()
            Account_list.append(decryption.Decryption(Account_number[15:-1], is_special=True))
            if Time_to_break == 1:
                break
        Account_list.pop()

    finally:
        myFile.close()

    return Account_list


def ID_Loading(need_decryption=False):
    myFile = open('account_file.txt', 'r')
    try:
        id_list = []
        myFile.seek(0)
        for each in range(5):
            x = myFile.readline()
            if x == 'EoF':
                break
        ID = myFile.readline()
        id_list.append(ID[4:-1])

        Time_to_break = 0

        while True:
            for each in range(10):
                x = myFile.readline()
                if x == 'EoF':
                    Time_to_break = 1
                    break
            ID = myFile.readline()
            id_list.append(ID[4:-1])
            if Time_to_break == 1:
                break
        id_list.pop()

    finally:
        myFile.close()

    if need_decryption:
        new_id_list = []
        for STR in id_list:
            new_id_list.append(decryption.Decryption(STR, is_ID=True))
        return new_id_list

    return id_list


def match_password_in_file(account_number: str):
    account_list = Account_Loading()
    Index_number = account_list.index(account_number)
    Line = Index_number * 11 + 2
    myFile = open('account_file.txt', 'r')
    try:
        for each in range(Line):
            myFile.readline()
        Password = myFile.readline()

    finally:
        myFile.close()

    return decryption.Decryption(Password[17:-1], decryption.Decryption(ID_Loading()[Index_number], is_ID=True))


def Account_level(account_number: str):
    status = []
    account_list = Account_Loading()
    Index_number = account_list.index(account_number)
    Line = Index_number * 11 + 6
    myFile = open('account_file.txt', 'r')
    try:
        for each in range(Line):
            myFile.readline()
        admin = myFile.readline()[-2]
        official = myFile.readline()[-2]
        status.append(decryption.Decryption(admin, decryption.Decryption(ID_Loading()[Index_number], is_ID=True)))
        status.append(decryption.Decryption(official, decryption.Decryption(ID_Loading()[Index_number], is_ID=True)))

    finally:
        myFile.close()

    return status


### get account information ###
### The order will be name, address, phone number, balance, enable status. ###
def account_information_get(account_number: str):
    information_list = []
    account_list = Account_Loading()
    Index_number = account_list.index(account_number)
    Line = Index_number * 11
    myFile = open('account_file.txt', 'r')
    Dict = decryption.Decryption(ID_Loading()[Index_number], is_ID=True)

    try:
        for each in range(Line):
            myFile.readline()
        information_list.append(decryption.Decryption(myFile.readline()[5:-1], is_special=True))
        myFile.readline()
        myFile.readline()
        information_list.append(decryption.Decryption(myFile.readline()[8:-1], Dict))
        information_list.append(decryption.Decryption(myFile.readline()[13:-1], is_special=True))
        myFile.readline()
        myFile.readline()
        myFile.readline()
        information_list.append(decryption.Decryption(myFile.readline()[8:-1], Dict))
        information_list.append(decryption.Decryption(myFile.readline()[7:-1], Dict))

    finally:
        myFile.close()

    return information_list


def ID_get(account_number: str):
    account_list = Account_Loading()
    Index_number = account_list.index(account_number)
    Dict = decryption.Decryption(ID_Loading()[Index_number], is_ID=True)

    return Dict


def account_status_get(account_number: str):
    account_list = Account_Loading()
    Index_number = account_list.index(account_number)
    Line = Index_number * 11 + 9
    myFile = open('account_file.txt', 'r')
    Dict = decryption.Decryption(ID_Loading()[Index_number], is_ID=True)
    try:
        for each in range(Line):
            myFile.readline()
        status = decryption.Decryption(myFile.readline()[7:-1], Dict)
    finally:
        myFile.close()

    return status


def Name_get(account_number: str, inverse=False):
    account_list = Account_Loading()
    name_list = Name_listing()
    if inverse:
        return account_list[name_list.index(account_number)]
    return name_list[account_list.index(account_number)]


def password_get(account_number: str):
    account_list = Account_Loading()
    password_list = raw_password_listing()
    Dict = ID_get(account_number)
    return decryption.Decryption(password_list[account_list.index(account_number)], Dict)




if __name__ == '__main__':
    # print(Account_Loading())
    # print(account_information_get('228813976'))
    # print(Name_listing())
    # print(Name_get('228813976'))
    # print(raw_password_listing())
    print(password_get('228813976'))


