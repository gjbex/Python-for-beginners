#!/usr/bin/env python

# Define a function that given two DNA sequences returns True if the
# first sequence is the complement of the second, False otherwise.  You can
# assume that the DNA strings only contain A, C, G, and T.
# Hint: define a function that returns the complement of a given nucleotide.

def complement(nucl):
    if nucl == 'A':
        return 'T'
    elif nucl == 'C':
        return 'G'
    elif nucl == 'G':
        return 'C'
    elif nucl == 'T':
        return 'A'
    else:
        return None


def is_complement(dna1, dna2):
    if len(dna1) != len(dna2):
        return False
    for i in range(len(dna1)):
        if dna1[i] != complement(dna2[i]):
            return False
    return True

if __name__ == '__main__':
    dna_tuples = [('ACCGT', 'TGGCA'), ('GA', 'CT'), ('ACG', 'CGC')]
    expected_results = [True, True, False]
    for dna_tuple, expected_result in zip(dna_tuples, expected_results):
        if is_complement(dna_tuple[0], dna_tuple[1]) == expected_result:
            print('okay for', dna_tuple)
        else:
            print('not okay for', dna_tuple)
