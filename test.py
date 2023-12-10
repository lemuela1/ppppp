import decryption
import encryption
import OBJECT
import main

if __name__ == '__main__':
    myfile = open('account_file.txt', 'r')
    try:
        print(myfile.readlines(3))
        print(myfile.readlines(3))
        print(myfile.readlines(3))
    finally:
        myfile.close()
