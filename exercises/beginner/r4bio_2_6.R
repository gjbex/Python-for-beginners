#!/usr/bin/env Rscript

library(stringr)

dna <- paste(
    'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGAT',
    'CGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT',
    sep=''
)

exon1 <- str_sub(dna, end = 63)
intron <- str_sub(dna, start = 64, end = 90)
exon2 <- str_sub(dna, start = 91)
cat(str_to_upper(exon1), str_to_lower(intron), str_to_upper(exon2), sep='')
