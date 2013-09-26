from random import randint,seed
from Bio import SeqIO

def generate_substring(sequence, length=100):
  '''Given an input string, return a random substring of length length (default 100)'''
  start_idx = randint(0,len(sequence))
  end_idx = start_idx + length
  return get_substring_from_circular(sequence, start_idx, end_idx)

def get_substring_from_circular(sequence, start_idx, end_idx):
  '''Gets a substring from sequence while allowing the sequence to be circular. i.e. the two ends come together and end_idx can be < start_idx
  >>> get_substring_from_circular('ACGTGA', start_idx=0, end_idx=3)
  'ACG'
  >>> get_substring_from_circular('ACGTGA', start_idx=0, end_idx=1)
  'A'
  >>> get_substring_from_circular('ACGTGA', start_idx=4, end_idx=2)
  'GAAC'
  '''
  return sequence[start_idx:end_idx]

def read_simulator(sequence, n, out_fasta_filename):
	# Call generate_substring() n number of times
	substring = generate_substring(sequence, 100000)
	# write substring to out_fasta_filename
	# generate fastaID for each sequence and add ">"
	pass

# call read_simulator() for each of the Mu and Wt sequences

def enumerate_kmers_in_sequence(sequence, k):
    ''' returns a dictionary of k-mer counts '''
    # Pre-compute number of k-mers from a sequence
    step=1 # this could be changed 
    dKMers={}
    numOfKmers = ((len(sequence)-k)/step)+1
    # Get the kmers
    for i in range(0,numOfKmers*step,step):
        kMer=sequence[i:i+k]
        # now generate the dictionary
        if kMer in dKMers:
            dKMers[kMer]+= 1
        else:
            dKMers[kMer]=1
    return dKMers

def enumerate_kmers_in_fasta_file(k_mer_counts):
  # call enumerate_kmers_in_sequence() for each fasta sequence
  
  pass

# ----Main part of the program:
# open fasta file and iterate through the sequence 
#
from Bio import SeqIO   # move this to the top !!!!

# This needs to be adapted because first we open the wt sequence then the mu sequence files

wtFastaFile = open(</FASTAfilename>)
for i in SeqIO.parse(fastaFile,'fasta')
    # print i.id; print i.seq
    # obtain k-mer count for each sequence and build up dictionary by calling the functions above
    # !!! my_wt_dict = enumerate_kmers_in_fasta_file(wt_reads)   
wtfastaFile.close()

# obtain k-mer count for each sequence and build up dictionary by calling the functions above

# my_mu_dict = enumerate_kmers_in_fasta_file(mu_reads)

# find differences between my_wt_dict and my_mu_dict
#mu_only = set(my_mu_dict.keys()) - set(my_wt_dict.keys())
#wt_only = set(my_wt_dict.keys()) - set(my_mu_dict.keys())

if __name__ == '__main__':
  # this runs the doctests when the file is executed by python
  # but doesn't run them when the file is included
  import doctest
  doctest.testmod()

