#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-14
Purpose: Translate a DNA or RNA sequence into amino acid sequence 
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'STR', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    codons = args.codons
    outfile = args.outfile
    string = args.STR.upper()

    if not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))

    codon_dict = {}
    for n in open(codons):
        pair = n.split()        
        codon_dict[pair[0]] = pair[1]

    k = 3
    n = len(string) - k + 1
    protein = []
    for i in range(0, n, k):
        if codon_dict.get(string[i:i+k]) == None:
            protein.append('-')
        else:
            protein.append(codon_dict.get(string[i:i+k]))

    out_fh = open(outfile, 'wt')
    out_fh.write(str(''.join(protein)))

    print('Output written to "{}"'.format(outfile))
# --------------------------------------------------
if __name__ == '__main__':
    main()
