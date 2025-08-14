# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:32:07 2016

@author: Geert Jan Bex
"""

from at_content import at_content

def is_selected(organism, dna_seq, gen_name, expr_level):
    at_contents = at_content(dna_seq)
    return 0.45 <= at_contents and at_contents <= 0.65
