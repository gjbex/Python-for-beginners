#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:23:17 2016

@author: Geert Jan Bex
"""

def at_content(dna_seq):
    dna_seq = dna_seq.upper()
    a_content = dna_seq.count('A')
    t_content = dna_seq.count('T')
    seq_length = len(dna_seq)
    return (a_content + t_content)/seq_length
    
if __name__ == '__main__':
    dna_seq = 'ATTTACCGGAATTTTAAA'
    print(at_content(dna_seq))
