#!/usr/bin/env Rscript

library(stringr)

headers <- c('ABC123', 'DEF456', 'HIJ789')
seqs <- c(
    'ATCGTACGATCGATCGATCGCTAGACGTATCG',
    'actgatcgacgatcgatcgatcacgact',
    'ACTGAC-ACTGT--ACTGTA----CATGTG'
)

for (i in seq(length(seqs))) {
    fasta_filename <- paste(headers[i], '.fasta', sep='')
    fasta_file <- file(fasta_filename, open='w')
    seq <- seqs[i]
    seq = str_replace_all(seq, '-', '')
    seq = str_to_upper(seq)
    cat('>', headers[i], '\n', sep = '', file = fasta_file)
    cat(seq, '\n', sep = '', file = fasta_file)
    close(fasta_file)
}
