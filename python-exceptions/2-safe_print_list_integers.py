#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            p += 1
        except (ValueError, TypeError):
            continue
    print("")
    return p
