#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-02-04
Purpose: Create square grid of a given length 
"""

import os
import sys


# --------------------------------------------------
def main():
    num = sys.argv[1:]

    if len(num) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    num = int(num[0])
    if num < 2 or num > 9:
        print('NUM ({}) must be between 1 and 9'.format(num))
        sys.exit(1)

    for i in range(1, num ** 2 + 1):
        if i % num == 0:
           print('{:3}\n'.format(i), end='')
        else:
           print('{:3}'.format(i), end='')
# --------------------------------------------------
main()
