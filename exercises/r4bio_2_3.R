#!/usr/bin/env Rscript

library(stringr)

dna <- 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
motif <- 'GAATTC'

cut_index <- str_locate(dna, motif)
seq1 <- str_sub(dna, end = cut_index[1])
seq2 <- str_sub(dna, start = cut_index[1] + 1)
cat(seq1, '*', seq2, '\n', sep='')
cat(str_length(seq1), str_length(seq2))
