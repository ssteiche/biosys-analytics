#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-19
Purpose: Process a Swissprot file 
"""

import argparse
import sys
import os
from Bio import SeqIO
from xml.etree.ElementTree import ElementTree

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'uniprot', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
        '--output',
        help='A named integer argument',
        metavar='FILE',
        type=str,
        default='out.fa')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs='+',
        default='')

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
    uniprot = args.uniprot
    key = args.keyword.lower()
    output = args.output
    skip = set(map(str.lower, args.skip))

    if not os.path.isfile(uniprot):
        die('"{}" is not a file'.format(uniprot))

    skip_set = set(skip)

    print('Processing "{}"'.format(uniprot))

    num_skipped = 0
    num_taken = 0

    with open(output, 'w') as out_fh:
        for record in SeqIO.parse(uniprot, 'swiss'):
            annot = record.annotations
            if skip and 'taxonomy' in annot:
                taxa = set(map(str.lower, annot['taxonomy']))
                if skip.intersection(taxa):
                    num_skipped += 1
                    continue

            if 'keywords' in annot:
                kw = set(map(str.lower, annot['keywords']))

                if key in kw:
                    num_taken += 1
                    SeqIO.write(record, out_fh, 'fasta')
                else:
                    num_skipped += 1

    print('Done, skipped {} and took {}. See output in "{}".'.format(num_skipped, num_taken, output))

# --------------------------------------------------
if __name__ == '__main__':
    main()
