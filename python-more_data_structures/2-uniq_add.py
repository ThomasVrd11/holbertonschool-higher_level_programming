#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_int = set(my_list)
    num = 0
    for int in unique_int:
        num += int
    return num