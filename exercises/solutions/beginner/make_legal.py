#!/usr/bin/env python

# Define a function that given a string that represents DNA, creates a new
# string that only contains the character 'A', 'C', 'G', 'T'.  If the
# original string contains lower case letters 'a', 'c', 'g', 't', replace
# those with upper case.  All other characters are left out.
# If you get it right, the script will print 'okay' for all test
# cases.

def make_legal(dna):
    new_dna = ''
    for symbol in dna:
        symbol = symbol.upper()
        if symbol in ['A', 'C', 'G', 'T']:
            new_dna += symbol
    return new_dna

if __name__ == '__main__':
    dnas = ['ACGTTAGC', 'ACewla', 'acccgv', '', 'fkjrk']
    expected_legals = ['ACGTTAGC', 'ACA', 'ACCCG', '', '']
    for dna, expected_legal in zip(dnas, expected_legals):
        if make_legal(dna) == expected_legal:
            print("okay for '{0}'".format(dna))
        else:
            print("not okay for '{0}'".format(dna))
