#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-13
Purpose: Calculate Hamming distances
"""

import argparse
import sys
import logging
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='File inputs', nargs=2)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true', default=False)

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
def dist(s1, s2):
    """Calculate Hamming distance"""
    edits = abs(len(s1)-len(s2))
    for l1, l2 in list(zip(s1, s2)):
        if l1 != l2:
            edits += 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, edits))
    return edits

# --------------------------------------------------
def main():
    """Execute dist function and log"""
    args = get_args()
    files = args.files

    for inp in files:
        if not os.path.isfile(inp):
            die('"{}" is not a file'.format(inp))

    prg = sys.argv[0]
    prg_name, _ = os.path.splitext(os.path.basename(prg))
    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    logging.debug('file1 = {}, file2 = {}'.format(files[0], files[1]))
    
    hamm = 0
    f1 = open(files[0]).read().split()
    f2 = open(files[1]).read().split()
    ftot = list(zip(f1, f2))
    for s1, s2 in ftot:
        hamm += dist(s1, s2)
    
    print(hamm)

# --------------------------------------------------
if __name__ == '__main__':
    main()
