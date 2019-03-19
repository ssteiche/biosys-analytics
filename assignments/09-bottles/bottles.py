#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-03-19
Purpose: Sing a jaunty tune 
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default=10)

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
    num = args.num_bottles

    if num < 1:
        die('N ({}) must be a positive integer'.format(num))

    for i in list(reversed(range(1,num+1))):
        if i == 1:
            print('{} bottle of beer on the wall,\n{} bottle of beer,'.format(i, i))
            print('Take one down, pass it around,\n{} bottles of beer on the wall!'.format(i-1))
        elif i == 2:
            print('{} bottles of beer on the wall,\n{} bottles of beer,'.format(i, i))
            print('Take one down, pass it around,\n{} bottle of beer on the wall!\n'.format(i-1))
        else:    
            print('{} bottles of beer on the wall,\n{} bottles of beer,'.format(i, i))
            print('Take one down, pass it around,\n{} bottles of beer on the wall!\n'.format(i-1))

# --------------------------------------------------
if __name__ == '__main__':
    main()
