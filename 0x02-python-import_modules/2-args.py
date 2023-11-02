#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    num_arguments = len(arguments)
    if num_arguments == 1:
        print("0 arguments.")
    else:
        if num_arguments == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(num_arguments - 1))
        for i in range(1, num_arguments):
            print("{}: {}".format(i, sys.argv[i]))
