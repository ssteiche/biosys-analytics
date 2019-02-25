#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-25
Purpose: Print the first line of each file in a directory 
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print the first line of each file in a directory',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'dirs', metavar='DIR', help='Directory containing files to list first lines', nargs='+')

    parser.add_argument(
        '-w',
        '--width',
        help='Width of space to print',
        metavar='int',
        type=int,
        default='50')

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
    dirs = args.dirs
    width = args.width

    for d in dirs:
        if not os.path.isdir(d):
            warn('"{}" is not a directory'.format(d))
        else: 
            print('{}'.format(d))
            out_dict = {}
            for filename in os.listdir(d):
                i = 0
                for line in open(os.path.join(d, filename)):
                    i += 1
                    if i > 1:
                        break
                    out_dict[line] = filename    
            for l, n in sorted(out_dict.items()):
                dots = width - len(l.rstrip()+n)
                print('{}'.format(l.rstrip()), '.'*dots, '{}'.format(n))

# --------------------------------------------------
if __name__ == '__main__':
    main()
