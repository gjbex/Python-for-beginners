#!/usr/bin/env python

# Define a function that given a string that represents DNA, finds the
# longest sequence of identical nucleotides, e.g.,
# AACCCGACGGT -> CCC
# AAACCAAAA -> AAAA
# If there are multiple subsequences of the same length, return the first,
# e.g.,
# ACCCGTTTA -> CCC

def longest_identical(dna):
    if len(dna) == 0:
        return ''
    subseq = ''
    curr_seq = dna[0]
    for nucl in dna[1:]:
        if nucl == curr_seq[0]:
            curr_seq += nucl
        else:
            if len(curr_seq) > len(subseq):
                subseq = curr_seq
            curr_seq = nucl
    if len(curr_seq) > len(subseq):
        subseq = curr_seq
    return subseq

if __name__ == '__main__':
    dnas = ['AACCCGACCGGT', 'AAACGAAAAT', 'CAAGTTG', 'CAGT', '',
            'CAAGAAA', 'CCAAAGGTTTG']
    expected_subseqs = ['CCC', 'AAAA', 'AA', 'C', '', 'AAA', 'AAA']
    for dna, expected_subseq in zip(dnas, expected_subseqs):
        if longest_identical(dna) == expected_subseq:
            print("okay for '{0}'".format(dna))
        else:
            print("not okay for '{0}'".format(dna))
