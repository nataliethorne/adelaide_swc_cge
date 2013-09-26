This function has been written to assess whether mutation can be identified from k-mer values obtained from genomic sequences when reference genomes are not available and the reads are not assembled de novo either. The function thus compares reads generated from a wild type strain with those generated from its related mutant. We assume that the reads have an even coverage, and the data do not include sequencing errors. Therefore we use fasta files as input.
To test this hypothesis we downloaded a random 10 000 bp sequence, duplicated it and manually made two single nucleotide mutations. The 
two sequences are then randomly split in 100 bp simulated-reads and two dictionaries based on k-mer of user-defined length are generated for the wild type and the mutant, respectively. The comparison of the two dictionaries will eventually detect the two single-nucleotide mutations that we introduced at the beginning.       


