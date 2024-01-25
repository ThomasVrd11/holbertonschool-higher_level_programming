#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (ord(letter) <= ord('z') and ord(letter) >= ord('a')):
            up = chr(ord(letter) - 32)
        else:
            up = letter
        print("{}".format(up), end='')
    print()
