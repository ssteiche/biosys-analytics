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
        default=None)

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
    key = args.keyword
    output = args.output
    skip = args.skip

    if key == None:
        die('error: the following arguments are required: -k/--keyword')
    
    if not os.path.isfile(uniprot):
        die('"{}" is not a file'.format(uniprot))

    key_set = set(key)
    skip_set = set(skip)

    tree = ElementTree()
    root = tree.parse(file)

    print('str_arg = "{}"'.format(str_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
