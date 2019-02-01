#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-01-31
Purpose: Count vowels, check that subject and verd number agrees, and proper use of plurals 
"""

import os
import sys


# --------------------------------------------------
def main():
    STRING = sys.argv[1:]

    if len(STRING) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    print('String is "{}"'.format(STRING))


# --------------------------------------------------
main()
