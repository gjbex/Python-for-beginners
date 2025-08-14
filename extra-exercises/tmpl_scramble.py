#!/usr/bin/env python

# Define a function that given a string representing a text
# consisting of sentences in a natural language, and at random
# switches two consecutive characters in words.  Add an optional
# argument for the probability two exchange character in a word,
# defaults to 20 %. You can assume that the text contains only
# words and whitespace, no other characters.
# E.g.,  'This is an example' -> 'hTis is an exapmle'
# Hint: look at the documentation of the function random in the
# standard library module random and randint.

import random

def scramble_word(word, prob):
    return word


def scramble(sentence, prob=0.2):
    return sentence

def count_changes(orig_sentences, new_sentence):
    count = 0
    for orig_word, new_word in zip(orig_sentences.split(),
                                   new_sentence.split()):
        if orig_word != new_word:
            count += 1
    return count

if __name__ == '__main__':
    sentence = ('This is an example I think with a very long '
                'sentence that seems to keep going for ever since '
                'we need quite some words')
    nr_words = len([1 for word in sentence.split() if len(word) > 1])
    for prob in [0.0, 0.2, 0.5, 1.0]:
        new_sentence = scramble(sentence, prob)
        msg = 'probability = {0:.1%}, {1:.1%} words changed:'
        nr_words_changed =  count_changes(sentence, new_sentence)
        print(msg.format(prob, nr_words_changed/nr_words))
        print(new_sentence)
