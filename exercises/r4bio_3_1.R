#!/usr/bin/env Rscript

library(stringr)

filename <- 'genomic_dna_3.txt'
coding_filename <- 'genomic_dna_3_coding.txt'
noncoding_filename <- 'genomic_dna_3_noncoding.txt'

dna_file <- file(filename, open='r')
dna <- readLines(dna_file)
close(dna_file)

exon1 <- str_sub(dna, end = 63)
intron <- str_sub(dna, start = 64, end = 90)
exon2 <- str_sub(dna, start = 91)
coding_file <- file(coding_filename, open = 'w')
cat(exon1, exon2, sep = '', file = coding_file)
close(coding_file)
noncoding_file <- file(noncoding_filename, open = 'w')
cat(intron, sep = '', file = noncoding_file)
close(noncoding_file)
