#!/usr/bin/python3

def no_c(my_string):
    noCstring = my_string.translate({ord(i): None for i in 'cC'})
    return noCstring
