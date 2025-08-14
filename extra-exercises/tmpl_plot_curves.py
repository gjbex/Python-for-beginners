#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# Note: this exercise can only be done after create_curves.py was completed.
# Define a function that given a file name and a number, creates a plot
# shows the column of the data file with that number, versus the first
# column in the file.  Use 0-based indexing.  The function has an optional
# third argument, representing the label of the y-axis

def plot_curves(file_name, col_nr, ylabel=r'$f(t)$'):
    pass

if __name__ == '__main__':
    file_name = 'data.txt'
    plot_curves(file_name, 1, r'$\sin(2\pi t)$')
    plot_curves(file_name, 2, r'$\cos(2\pi t)$')
