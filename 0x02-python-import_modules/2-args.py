#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv) -1

    char_s = ""
    if num_arguments > 1:
        char_s = "s"
    elif num_arguments == 0:
        char_s = "s."

    print(f"{num_arguments} argument{char_s}")

    if num_arguments > 0:
        for argument in range(1, num_arguments + 1):
            print(f"{argument}: {sys.argv[argument]}")
