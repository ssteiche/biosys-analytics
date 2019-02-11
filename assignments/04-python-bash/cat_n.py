#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-10
Purpose: Replicate 'cat' bash command function in python
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    infile = args[0]

    if not os.path.isfile(infile):
        print('{} is not a file'.format(infile))
        sys.exit(1)

    i = 0
    for line in open(infile):
        i += 1
        print("{:3}: {}".format(i, line), end='')
# --------------------------------------------------
main()
