#!/usr/bin/env python

# Define a function that given a number of seconds, returns a 3-tuple
# consisting of the number of hours, minutes and seconds, e.g.,
# 7325 -> (2, 2, 5)
# Hint: look at the modulo operator, and the integer division
# operator.  Keep in mind that things changed from Python 2 to
# Python 3.
#
# Define a function that given a number of hours, minutes and
# seconds, returns a string representation in the format HH:MM:SS,
# e.g., (2, 2, 5) -> '02:02:05'
# Hint: look at the documentation of the str method format.
#
# Define a function that given a string in the format HH:MM:SS,
# returns a 3-tuple of integers that represent the hours, minutes,
# and seconds, e.g., '02:02:05' -> (2, 2, 5)
# Hint: look at the documentation of the str method split.
#
# Define a function that given hours, minutes, and seconds returns
# the total number of seconds, e.g., (2, 2, 5) -> 7325

def seconds2hms(seconds):
    return -1, -1, -1

def hms2str(hh, mm, ss):
    return 'nonsense'

def str2hms(hms_str):
    parts = hms_str.split(':')
    return -1, -1, -1

def hms2seconds(hh, mm, ss):
    return -1

if __name__ == '__main__':
    seconds = [7325, 714, 3517]
    hmss = [(2, 2, 5), (0, 11, 54), (0, 58, 37)]
    hms_strs = ['02:02:05', '00:11:54', '00:58:37']
    for second, hms in zip(seconds, hmss):
        if seconds2hms(second) == hms:
            print('okay for', second)
        else:
            print('not okay for', second)
    for hms, hms_str in zip(hmss, hms_strs):
        if hms2str(*hms) == hms_str:
            print('okay for', hms)
        else:
            print('not okay for', hms)
    for hms_str, hms in zip(hms_strs, hmss):
        if str2hms(hms_str) == hms:
            print('okay for', hms_str)
        else:
            print('not okay for', hms_str)
    for hms, second in zip(hmss, seconds):
        if hms2seconds(*hms) == second:
            print('okay for', hms)
        else:
            print('not okay for', hms)
