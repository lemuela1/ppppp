import decryption


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
        Account_list.append(Account_number[15:-1])

        Time_to_break = 0

        while True:
            for each in range(10):
                x = myFile.readline()
                if x == 'EoF':
                    Time_to_break = 1
                    break
            Account_number = myFile.readline()
            Account_list.append(Account_number[15:-1])
            if Time_to_break == 1:
                break
        Account_list.pop()

    finally:
        myFile.close()

    return Account_list


def ID_Loading():
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
        information_list.append(decryption.Decryption(myFile.readline()[5:-1], Dict))
        myFile.readline()
        myFile.readline()
        information_list.append(decryption.Decryption(myFile.readline()[8:-1], Dict))
        information_list.append(decryption.Decryption(myFile.readline()[13:-1], Dict))
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
    ID_list = ID_Loading()
    index_num = account_list.index(account_number)
    return ID_list[index_num:-1]


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


if __name__ == '__main__':
    print(account_status_get('1059115847'))
