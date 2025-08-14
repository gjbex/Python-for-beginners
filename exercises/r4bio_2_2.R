#!/usr/bin/env Rscript

library(stringr)

dna <- 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

tmp <- str_replace_all(dna, 'A', 't')
tmp <- str_replace_all(tmp, 'C', 'g')
tmp <- str_replace_all(tmp, 'G', 'c')
tmp <- str_replace_all(tmp, 'T', 'a')
cat(dna, sep = '\n')
cat(str_to_upper(tmp))
