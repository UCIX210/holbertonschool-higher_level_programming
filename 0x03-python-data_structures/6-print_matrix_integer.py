#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for index in matrix:
        for x in index:
            print(" ".join("{:d}".format(x)))
