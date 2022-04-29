#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1

    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print(f"{num} arguments:")
    for i in range(num):
        print(f"{i + 1}: {sys.argv[i + 1]}")
