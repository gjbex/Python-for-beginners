#!/usr/bin/env python

# Define a function that given a DNA sequence, and a subsequence,
# determines the maximum number of consecutive repetitions of that
# subsequence in the given sequence.  Repetitions do not overlap.
# Hint: look at the documentation of the string method find.

def find_max_repetitions(dna, subseq):
    return -1

if __name__ == '__main__':
    inputs = [
        ('AGTGTAGTGTGTAGTGTA', 'GT'),
        ('AAAATAATAAA', 'AA'),
        ('AATAAAATAAAAAAA', 'AA'),
    ]
    expected_results = [3, 2, 3]
    for input, expected_result in zip(inputs, expected_results):
        if find_max_repetitions(input[0], input[1]) == expected_result:
            print('okay for', inputs)
        else:
            print('not okay for', inputs)
