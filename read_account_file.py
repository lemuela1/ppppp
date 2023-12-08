myFile = open('account_file.txt', 'r')
try:
    myFile.seek(0)
    for each in range(34):
        myFile.readline()
    x_err = myFile.readline()
    y_err = myFile.tell()
    print(y_err)
    print(x_err[4::])


finally:
    myFile.close()
