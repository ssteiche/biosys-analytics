#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-08
Purpose: Write unclustered proteins to file 
"""

import argparse
import sys
import re
import os
from Bio import SeqIO
import csv

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find unclustered proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True)
    
    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

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
def main():
    """Make a jazz noise here"""
    args = get_args()
    cdhit = args.cdhit
    proteins = args.proteins
    outfile = args.outfile
    
    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))

    if not os.path.isfile(cdhit):
        die('--cdhit "{}" is not a file'.format(cdhit))
    
    cdhit_re = re.compile('>gi\|(?P<id>\d*)')
    clustered = set()
    for line in open(cdhit):
        if cdhit_re.search(line) == None:
            continue
        pid = cdhit_re.search(line)
        clustered.add(pid.group('id'))

    num_unclustered = 0
    num_total = 0

    with open(outfile, 'w') as out_fh:
        for record in SeqIO.parse(proteins, 'fasta'):
            num_total += 1
            if not re.sub('[|].*', '', record.id) in clustered:
                num_unclustered += 1
                SeqIO.write(record, out_fh, 'fasta')

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(num_unclustered, num_total, outfile))

# --------------------------------------------------
if __name__ == '__main__':
    main()
