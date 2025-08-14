# UseModules
A small illustrations of using functions in modules.

## What is it?
1. `at_content.py`: script that computes the AT content of a fixed
    sequence, using a function it defines.
1. `select.py`: select data from a file, based on selection criterium
    that is passed on the command line.  It uses the `select_at` or
    `select_organism` modules' implementation of the selection function.
1. `select_at.py`: defines selection function based on the AT content of
    the sequence.  Uses the `at_content` module.
1. `select_organism.py`: defines selection function based on the name of
    the organism the sequence was sampled from.
1. `data_6.csv`: data file to use.
