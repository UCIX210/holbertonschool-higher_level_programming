#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if 97 <= char <= 122:
            char = char - 32
        print(chr(char), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")