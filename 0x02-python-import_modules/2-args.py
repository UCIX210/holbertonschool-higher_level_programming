#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print(f"{num_arguments} arguments.")
    elif num_arguments == 1:
        print(f"{num_arguments} argument:")
    else:
        print(f"{num_arguments} arguments:")

    if num_arguments >= 1:
        num_arguments = 0
        for arg in sys.argv:
            if num_arguments != 0:
                print(f"{num_arguments}: {arg}")
            num_arguments += 1
