#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-15
Purpose: Graph through sequences 
"""

import argparse
import sys
from Bio import SeqIO
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='str', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='K size of overlap',
        metavar='int',
        type=int,
        default=3)

    return parser.parse_args()

# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def find_kmers(seq, kmer):
    """Return kmers"""
    kmers = []
    n = len(seq) - kmer + 1
    for i in range(0, n):
        kmers.append(seq[i:i+kmer])

    return(kmers)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    fasta = args.fasta
    over = args.overlap

    if over <= 0:
        die('-k "{}" must be a positive integer'.format(over))

    if not os.path.isfile(fasta):
        die('"{}" is not a file'.format(fasta))

    begin = {}
    end = {}

    for record in SeqIO.parse(fasta, 'fasta'):
        kmers = find_kmers(str(record.seq), over)
        begin[record.id] = kmers[0]
        end[record.id] = kmers[-1]
    
    for id_end, mer_end in end.items():
        for id_beg, mer_beg in begin.items():
            if mer_end == mer_beg:
                if id_end == id_beg:
                    continue
                else:
                    print(id_end, id_beg)

# --------------------------------------------------
if __name__ == '__main__':
    main()
