#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n"""
    if n <= 0:
        return []

    pascalT = [[1]]
    while len(pascalT) != n:
        tri = pascalT[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pascalT.append(tmp)
    return pascalT
