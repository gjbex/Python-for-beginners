#!/usr/bin/env python

# Write a function, that given a string, returns the number of upper case
# characters in that string.
# Hint: check the documentation on strings in Python for a method to check
#       whether a string consists entirely of upper case letters.
# If you get it right, the script will print 'okay' for all test cases.

def count_upper(s):
    return -1

if __name__ == '__main__':
    str_examples = ['', 'Abc', 'ABc', '99485', 'A5b', 'ABCD']
    expected_counts = [0, 1, 2, 0, 1, 4]
    for str_example, expected_count in zip(str_examples, expected_counts):
        if count_upper(str_example) == expected_count:
            print("okay for '{0}'".format(str_example))
        else:
            print("not okay for '{0}'".format(str_example))
