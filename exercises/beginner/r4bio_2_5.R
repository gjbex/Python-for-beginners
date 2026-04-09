#!/usr/bin/env Rscript

library(stringr)

dna <- paste(
    'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGAT',
    'CGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT',
    sep=''
)

exon1 <- str_sub(dna, end = 63)
exon2 <- str_sub(dna, start = 91)
cat(format((str_length(exon1) + str_length(exon2))/str_length(dna),
           digits = 4))
