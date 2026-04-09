#!/usr/bin/env python

# Define a fucntion that, given a string, returns True is that string
# is a palindrom, Falose otherwise., e.g., 'radar' is a palindrome,
# 'boxer' is not.

def is_palindrome(word):
    return False

if __name__ == '__main__':
    words = ['radar', 'boxer', '', 'a', 'QQ', 'acracadacarca']
    expected_results = [True, False, True, True, True, True]
    for word, expected_result in zip(words, expected_results):
        if is_palindrome(word) == expected_result:
            print('okay for', word)
        else:
            print('not okay for', word)
