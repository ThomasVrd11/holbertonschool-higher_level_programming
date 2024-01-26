#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    if (num_args == 0):
        print("0 arguments.")
    elif (num_args == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, sys.argv[arg]))


if __name__ == "__main__":
    main()
