#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:58:53 2016

@author: Geert Jan Bex
"""

import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        selection = sys.argv[1]
    else:
        selection = 'organism'
    if selection == 'at':
        from select_at import is_selected
    elif selection == 'organism':
        from select_organism import is_selected
    else:
        print('error: selection mode "{0}" is not implemented'.format(selection),
              file=sys.stderr)
        sys.exit(1)
    with open('data_6.csv', 'r') as data_file:
        for line in data_file:
            organism, dna_seq, gen_name, expr_level = line.split(',')
            expr_level = int(expr_level)
            if is_selected(organism, dna_seq, gen_name, expr_level):
                print(gen_name)
