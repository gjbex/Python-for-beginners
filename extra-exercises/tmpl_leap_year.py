#!/usr/bin/env python

# Implement the function is_leap_year so that it returns True when the
# year is a leap year, False otherwise.  Check the Wikipedia article
# on leap years for the definition.
# Hint: the modulo operator in Python is %, it can be used to compute
#       the remainder of a division.
# If you get it right, the script will print 'okay' for all test
# cases.

def is_leap_year(year):
    return True

if __name__ == '__main__':
    years = [1971, 1972, 1980, 1990, 2000, 2004, 2100]
    expected_results = [False, True, True, False, True, True, False]
    for year, expected_result in zip(years, expected_results):
        if is_leap_year(year) == expected_result:
            print('okay for', year)
        else:
            print('not okay for', year)
