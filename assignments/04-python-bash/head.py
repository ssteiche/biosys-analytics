#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-10
Purpose: Replicate head bach command functionality in python
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    infile = args[0]
    num_lines = 3

    if len(args) > 1:
        num_lines = int(args[1])

    if not os.path.isfile(infile):
        print('{} is not a file'.format(infile))
        sys.exit(1)

    if not num_lines > 0:
        print('lines ({}) must be a positive number'.format(num_lines))
        sys.exit(1)

    i = 0
    for line in open(infile):
        i += 1
        if i > num_lines:
            break
        print(line, end='')
# --------------------------------------------------
main()
