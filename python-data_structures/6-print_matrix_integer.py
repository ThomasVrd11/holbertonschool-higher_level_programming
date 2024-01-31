#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for R in matrix:
        for i in range(len(R)):
            print("{:d}".format(R[i]), end=' ' if i != len(R) - 1 else '')
        print()
