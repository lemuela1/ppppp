### This is a function for decryption. ###
### x is the string that you wanna decryption, y decryption code dict. ###


def Decryption(encrypted_data: str, decrypted_user_id: dict = None, is_ID: bool = False) -> str or dict:
    code_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
        '+', '=', '-', 'Q', 'W', 'E', 'R', 'Y', 'U', 'I', 'O', 'P', '{', '[', ']', '}', '\\', '|', '\'', '\"', ':',
        ';', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '<', '>',
        '/', '?', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ' '
    ]

    if not is_ID:
        copy_list = []

        for each in code_list:
            copy_list += decrypted_user_id.get(each)

        DIC_decryption = {}

        for each in range(len(code_list)):
            DIC_decryption.update({copy_list[each]: code_list[each]})

        RETURN = ''

        for each in encrypted_data:
            RETURN += DIC_decryption.get(each)

        ### if the encrypted information is user_ID and DICT ###
        ### The return will be a dict ###

    elif is_ID:
        RETURN = {}
        for each in range(len(encrypted_data)):
            RETURN.update({encrypted_data[each]: code_list[each]})

    return RETURN


def Main():
    ID = """YF>!D,C+kf[ePhgUmHcL5?p#{:zGS*$RW)_aIw46xdu8JMV](s 0/lNoZ^73'bAq9=1ry%@.-|&\\"v2Ej}OQt;in<BXK"""
    print(Decryption(ID, is_ID=True))


if __name__ == "__main__":
    Main()
