#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-04-07
Purpose: Check alternate passwords 
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Check alternate passwords',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'password', metavar='PASSWORD', help='Users password')
    
    parser.add_argument(
        'alt', metavar='ALT', help='Alternative password')

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
    password = args.password
    alt = args.alt

    if alt.isupper():
        alt = alt.lower()

    if re.match('.?'+password+'.?', alt) or re.match(alt[0].lower()+alt[1:], password):
        print('ok')
    else:
        print('nah')

# --------------------------------------------------
if __name__ == '__main__':
    main()
