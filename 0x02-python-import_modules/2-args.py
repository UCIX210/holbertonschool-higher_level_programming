#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print(f"{num_arguments} arguments:")

    num_arguments = 0
    for arg in sys.argv:
        if num_arguments != 0:
            print(f"{num_arguments}: {arg}")
        num_arguments += 1
