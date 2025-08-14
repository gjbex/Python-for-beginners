#!/usr/bin/env Rscript

library(stringr)

dna <- 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

at_content <- (str_count(dna, 'A') + str_count(dna, 'T'))/str_length(dna)
cat(format(100*at_content, digits=5), '%')
