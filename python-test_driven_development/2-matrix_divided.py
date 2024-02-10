#!/usr/bin/python3
"""define mtrix divid """


def matrix_divided(matrix, div):
    """ function who return divi"""
    a = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(a)

    if not isinstance(div, int) and float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = matrix[:]

    return [[round(element / div, 2)for element in row]for row in new_matrix]
