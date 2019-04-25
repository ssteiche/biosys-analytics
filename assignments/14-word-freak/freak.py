#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-24
Purpose: Count the occurances of words in files 
"""

import argparse
import sys
from collections import defaultdict
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print word frequencies',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files', metavar='FILE', help='A positional argument', nargs='+',
        type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
def freqs(infiles):
    """build a dictionary with word frequency counts"""
    counts = defaultdict(int)
    for infile in infiles:
        for line in infile:
            for word in line.rstrip().split():
                if re.sub('[^a-zA-Z0-9]', '', word).lower() == '':
                    continue
                counts[re.sub('[^a-zA-Z0-9]', '', word).lower()] += 1

    return counts

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.files
    sort = args.sort
    minc = args.min

    outc = freqs(files)
    if sort == 'word':
        for entry in sorted(outc.keys()):
            if outc[entry] >= minc:
                print('{:20} {}'.format(entry, outc[entry]))
    elif sort == 'frequency':
        pairs = sorted([(x[1], x[0]) for x in outc.items()])
        for num, word in pairs:
            if num >= minc:
                print('{:20} {}'.format(word, num))

    #print(outc.keys())
# --------------------------------------------------
if __name__ == '__main__':
    main()
