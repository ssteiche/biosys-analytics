#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-25
Purpose: Segregate FASTA sequences by GC content
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
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FASTA', nargs='+', help='Input FASTA file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
    fasta_arg = args.fasta
    out_arg = args.outdir
    pcgc_arg = args.pct_gc

    if not 1 <= pcgc_arg <= 100:
        die('--pct_gc "{}" must be between 0 and 100'.format(pcgc_arg))

    if not os.path.isdir(out_arg):
        os.mkdir(out_arg)

    num_written = 0
    
    for fas in fasta_arg:
        if not os.path.isfile(fas):
            warn('"{}" is not a file'.format(fas))
        else: 

            #print(fas)
            basename = os.path.basename(fas)
            out_file_high = os.path.join(out_arg, os.path.splitext(basename)[0]+'_high'+os.path.splitext(basename)[1])
            out_fh_high = open(out_file_high, 'wt')
            out_file_low = os.path.join(out_arg, os.path.splitext(basename)[0]+'_low'+os.path.splitext(basename)[1])
            out_fh_low = open(out_file_low, 'wt')

            for record in SeqIO.parse(fas, 'fasta'):
                num_written += 1
                seq_len = len(record.seq)
                nucs = Counter(record.seq)
                gc = nucs.get('G', 0) + nucs.get('C', 0)
                #print(record.seq)
                gc_num = int(gc/seq_len*100)
                #print(gc_num)
                if gc_num >= pcgc_arg:
                    SeqIO.write(record, out_fh_high, 'fasta') 
                else:
                    SeqIO.write(record, out_fh_low, 'fasta')

    print('Done, wrote {} sequences to out dir "{}"'.format(num_written, out_arg))
#    print('fasta_arg = "{}"'.format(','.join(fasta_arg)))
#    print('out_arg = "{}"'.format(out_arg))
#    print('pcgc_arg = "{}"'.format(pcgc_arg))

# --------------------------------------------------
if __name__ == '__main__':
    main()
