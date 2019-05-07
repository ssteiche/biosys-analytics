#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-05-07
Purpose: Split interleaved sequence reads into seperate files
"""

import argparse
import sys
import os
from Bio import SeqIO
from collections import Counter

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Takes a single fasta file and split interleaved reads into seperate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fastas', metavar='FILE', nargs='+', help='Input file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='split')

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
    fastas = args.fastas
    outdir = args.outdir

    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    
    file_num = 0
    for fas in fastas:
        if not os.path.isfile(fas):
            warn('"{}" is not a file'.format(fas))
            continue
        
        file_num += 1

        basename = os.path.basename(fas)
        fname = os.path.splitext(basename)
        out_file_1 = os.path.join(outdir, fname[0]+'_1'+fname[1])
        out_fh_1 = open(out_file_1, 'wt')
        out_file_2 = os.path.join(outdir, fname[0]+'_2'+fname[1])
        out_fh_2 = open(out_file_2, 'wt')
        
        seqs = 0
        for record in SeqIO.parse(fas, 'fasta'):
            seqs += 1
            if seqs % 2 == 1:
                SeqIO.write(record, out_fh_1, 'fasta')
            else:
                SeqIO.write(record, out_fh_2, 'fasta')

        print('{}: {}\n\tSplit {} sequences to dir "{}"'.format(file_num, basename, seqs, outdir))
# --------------------------------------------------
if __name__ == '__main__':
    main()
