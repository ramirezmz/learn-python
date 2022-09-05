import os

try:
    os.remove('./test.txt')
    print('File removed with success!')
except FileNotFoundError as erro:
    print('File not Found')
    print('Description:', erro)
