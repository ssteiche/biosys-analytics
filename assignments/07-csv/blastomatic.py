#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-10
Purpose: Combine taxanomic assignments with BLAST percent ID result 
"""

import argparse
import sys
import os
import csv
from collections import defaultdict

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'BLAST', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annot',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
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
    outfile = args.outfile
    annot = args.annot
    blast = args.BLAST

    if not os.path.isfile(blast):
        die('"{}" is not a file'.format(blast))
        
    if not os.path.isfile(annot):
        die('"{}" is not a file'.format(annot))

    genus = {} 
    with open(annot) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['genus'] == '':
                genus[row['centroid']] = row['genus']
            else:
                genus[row['centroid']] = 'NA'

    species = {} 
    with open(annot) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['species'] == '':
                species[row['centroid']] = row['species']
            else:
                species[row['centroid']] = 'NA'

    blast_results = {}
    with open(blast) as tabfile:
        reader = csv.DictReader(tabfile, delimiter='\t', fieldnames=['0','1','2','3','4','5'])
        for row in reader:
            blast_results[row['1']] = row['2']

    for seqid in blast_results:
        if not seqid in genus.keys():
            warn('Cannot find seq "{}" in lookup'.format(seqid))
        else:
            print('{}\t{}\t{}\t{}'.format(seqid, blast_results.get(seqid), genus.get(seqid), species.get(seqid)))

    #print('outfile = "{}"'.format(outfile))
    #print('annot = "{}"'.format(annot))
    #print('blast = "{}"'.format(blast))

# --------------------------------------------------
if __name__ == '__main__':
    main()
