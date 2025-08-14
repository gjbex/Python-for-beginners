#!/usr/bin/env python

import numpy as np

# Define a function that given a file name and a number crates a file
# that contains 3 columns, and the given number of rows.  The first 
#cojumn represents time t, starting from 0.0, ending at 1.0.  The second and
# third column list the values of the functions sin(2pi t) and cos(2pi t)
# respectively.
# Hint: check the documentation for the functions linspace, sin, cos, and
# savetxt in the numpy module.

def create_curves(file_name, nr_rows):
    data = np.empty((nr_rows, 3))
    data[:, 0] = np.linspace(0.0, 1.0, nr_rows)
    data[:, 1] = np.sin(2*np.pi*data[:, 0])
    data[:, 2] = np.cos(2*np.pi*data[:, 0])
    np.savetxt(file_name, data)

if __name__ == '__main__':
    file_name = 'data.txt'
    expected_file_name = 'expected_data.txt'
    create_curves(file_name, 51)
    data = np.loadtxt(file_name)
    expected_data = np.loadtxt(expected_file_name)       
    if (data.shape == expected_data.shape and
        np.all(np.abs(data - expected_data) < 1e-5)):
        print('okay')
    else:
        print('not okay')
