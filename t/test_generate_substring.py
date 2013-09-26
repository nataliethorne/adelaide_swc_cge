import sys
sys.path.insert(0,'/home/swc_trainee/adelaide_swc_cge')

import generate_substring

Tests = [
  ['ACGTGA', 2, 4, 'GT'],
  ['ACGTGA', 4, 6, 'GA'],
  ['ACGTGT', 6, 1, 'TA'],
]

passes = 0
for (i, (sequence, start_idx, end_idx, expected)) in enumerate(Tests):
  if generate_substring.get_substring_from_circular(sequence, start_idx, end_idx) == expected:
    passes += 1
  else:
    print('test %d failed' % i)

print('%d/%d tests passed' % (passes, len(Tests)))

#print generate_substring.enumerate_kmers_in_sequence('ACGTGA', k=2)
#print generate_substring.enumerate_kmers_in_sequence('ACGTGAACGTGA', k=2)
