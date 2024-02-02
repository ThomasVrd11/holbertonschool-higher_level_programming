#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            p += 1
    except IndexError:
        pass
    print()
    return p
