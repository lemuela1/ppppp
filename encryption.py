### Password check dictionary generator. ###
### x is the string that you wanna encryption, y encryption code dic. ###
### If there isn't a y dict, it will generate and return a dict. ###
import read_account_file
import random


def Encryption(x: str, y: dict = None) -> str and dict:
    Str_return = ''
    if type(y) is dict:
        for each in x:
            Str_return += y.get(each)
        return Str_return

    elif y is None:

        # random ID generate
        while True:
            code_list = [
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                '+', '=', '-', 'Q', 'W', 'E', 'R', 'Y', 'U', 'I', 'O', 'P', '{', '[', ']', '}', '\\', '|', '\'', '\"',
                ':',
                ';', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '<', '>',
                '/', '?', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                'z', 'x', 'c', 'v', 'b', 'n', 'm', ' '
            ]

            Original_list = code_list.copy()

            random.shuffle(code_list)

            DIC = {}
            for each in range(len(code_list)):
                DIC.update({code_list[each]: Original_list[each]})

            # prevent ID redundant
            if DIC not in read_account_file.ID_Loading():
                break

        Str_return = ''
        for each in x:
            Str_return += DIC.get(each)

        return Str_return, DIC


def Special_Encryption(data: str):
    Str_return = ''
    DIC = {'1': 'U', '2': '[', '3': '@', '4': 'W', '5': 'V', '6': '6', '7': 'f', '8': 'I', '9': '1', '0': 'b', '!': 'G',
           '@': '%', '#': 'e', '$': '7', '%': 'w', '^': 'C', '&': '$', '*': '/', '(': ';', ')': 'm', '_': '8', '+': 'p',
           '=': '"', '-': 'S', 'Q': 'k', 'W': 'z', 'E': '&', 'R': '3', 'Y': '-', 'U': '5', 'I': '{', 'O': '<', 'P': 'O',
           '{': 'F', '[': 'D', ']': 'Y', '}': '>', '\\': 'B', '|': 'g', "'": ',', '"': ':', ':': 'o', ';': 'v',
           'A': 'n', 'S': 't', 'D': 'R', 'F': 'd', 'G': 'M', 'H': 'y', 'J': 'Z', 'K': 's', 'L': '.', 'Z': '#', 'X': '}',
           'C': '*', 'V': 'q', 'B': '4', 'N': 'J', 'M': 'H', ',': '+', '.': 'L', '<': 'E', '>': ')', '/': 'Q', '?': 'h',
           'q': 'x', 'w': '(', 'e': '!', 'r': 'P', 't': 'u', 'y': 'r', 'u': '2', 'i': 'i', 'o': 'j', 'p': 'A',
           'a': '\\', 's': '?', 'd': 'K', 'f': "'", 'g': 'N', 'h': '9', 'j': ' ', 'k': 'X', 'l': ']', 'z': 'a',
           'x': '_', 'c': '^', 'v': '0', 'b': '=', 'n': 'l', 'm': '|', ' ': 'c'}
    for each in data:
        Str_return += DIC.get(each)

    return Str_return


def Main():
    print(Encryption(input(), {'s': '1', '<': '2', 'R': '3', 'B': '4', 'P': '5', 'G': '6', 'n': '7', 'N': '8', 'u': '9',
                               '2': '0', 'S': '!', 'd': '@', 'F': '#', 'l': '$', 'm': '%', '[': '^', 'j': '&', 'f': '*',
                               'i': '(', 'M': ')', 'x': '_', 'c': '+', '8': '=', '?': '-', 'k': 'Q', ',': 'W', '*': 'E',
                               'H': 'R', '+': 'Y', '(': 'U', '$': 'I', '7': 'O', 'L': 'P', 'Y': '{', '|': '[', 'g': ']',
                               'O': '}', '\\': '\\', 'X': '|', '_': "'", 'q': '"', '^': ':', 'y': ';', '%': 'A',
                               'I': 'S', ';': 'D', 'v': 'F', 'a': 'G', '-': 'H', 'Q': 'J', '@': 'K', "'": 'L', '9': 'Z',
                               '{': 'X', 'r': 'C', 'z': 'V', 'U': 'B', '!': 'N', 'o': 'M', ' ': ',', '"': '.', 'C': '<',
                               ':': '>', 'J': '/', 'p': '?', '}': 'q', '.': 'w', '>': 'e', 'b': 'r', ')': 't', 'K': 'y',
                               '#': 'u', 'e': 'i', '/': 'o', 'D': 'p', 't': 'a', '0': 's', 'E': 'd', 'V': 'f', 'w': 'g',
                               '&': 'h', '3': 'j', '1': 'k', 'h': 'l', '=': 'z', '6': 'x', 'Z': 'c', '5': 'v', 'W': 'b',
                               '4': 'n', ']': 'm', 'A': ' '}))
    print(Encryption('asdfasdf'))
    print(isinstance(Encryption('asdfasdf'), tuple))


if __name__ == "__main__":
    Main()
