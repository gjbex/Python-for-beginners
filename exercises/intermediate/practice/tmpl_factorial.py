#!/usr/bin/env python

# Define a function that given a positive integer, returns the factorial
# of that number.  The factorial is defined as:
# 0! = 1
# n! = n*(n-1)!
# Define two versions, one that is recursive (i.e., the function calls
# itself, the other iterative.
# If you get it right, the script will print 'okay' for all years.

def fac_rec(n):
    return -1


def fac_iter(n):
    return -1

if __name__ == '__main__':
    import math
    for i in range(10):
        if fac_rec(i) == math.factorial(i):
            print('recursive okay for {0}'.format(i))
        else:
            print('recursive not okay for {0}'.format(i))
    for i in range(10):
        if fac_iter(i) == math.factorial(i):
            print('iterative okay for {0}'.format(i))
        else:
            print('iterative not okay for {0}'.format(i))
