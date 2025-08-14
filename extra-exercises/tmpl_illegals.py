#!/usr/bin/env python

# Define a function that given a string, counts the number of charactes
# that do not represent nucleotides in DNA.
# If you get it right, the script will print 'okay' for all test cases.

def count_illegal_chars(dna):
    return -1

if __name__ == '__main__':
    dnas = ['ACGTTAGC', 'ACewla', 'acccgv']
    expected_illegals_counts = [0, 3, 1]
    for dna, expected_illegals_count in zip(dnas, expected_illegals_counts):
        if count_illegal_chars(dna) == expected_illegals_count:
            print('okay for', dna)
        else:
            print('not okay for', dna)
