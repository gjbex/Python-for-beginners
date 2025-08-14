#!/usr/bin/env python

import numpy as np

# Define a function that, given a file name, reads the data in the file,
# and computes the sum of the columns in that file.
# The file contains the elements of a 2D array, each row on a line, the
# elements separated by spaces.
# write a second function that copmutes the row sum, rather than the column
# sum.
# Hint: look at the documentation of the loadtxt and sum functions
# from the numpy library.

def compute_col_sum(file_name):
    A = np.loadtxt(file_name)
    return A.sum(axis=0)


def compute_row_sum(file_name):
    A = np.loadtxt(file_name)
    return A.sum(axis=1)

if __name__ == '__main__':
    file_names = ['matrix1.txt', 'matrix2.txt']
    expected_col_sums = [np.array([3, 5, 7]), np.array([5, 2])]
    expected_row_sums = [np.array([17, -3, 1]), np.array([6, 1])]
    for file_name, expected_sum in zip(file_names, expected_col_sums):
        if np.all(compute_col_sum(file_name) == expected_sum):
            print("column okay for '{0}'".format(file_name))
        else:
            print("column not okay for '{0}'".format(file_name))
    for file_name, expected_sum in zip(file_names, expected_row_sums):
        if np.all(compute_row_sum(file_name) == expected_sum):
            print("row okay for '{0}'".format(file_name))
        else:
            print("row not okay for '{0}'".format(file_name))
