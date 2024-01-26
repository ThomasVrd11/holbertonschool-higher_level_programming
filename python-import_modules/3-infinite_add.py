#!/usr/bin/python3
import sys


def main():
    result = 0
    for arg in range(1, len(sys.argv)):
        result += int(sys.argv[arg])
    print("{}".format(result))


if __name__ == "__main__":
    main()
