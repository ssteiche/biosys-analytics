#!/usr/bin/env python3
"""
Author : ssteiche
Date   : 2019-01-31
Purpose: To warmly greet provided names.
"""

import os
import sys


# --------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME2 ...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(names) == 1:
        print('Hello to the 1 of you: ' + names[0] + '!')
        #print('Hello to the 1 of you: {}!'.format(names[0]))
    elif len(names) == 2:
        print('Hello to the 2 of you: {}!'.format(' and '.join(names)))
    elif len(names) > 2:
        num = len(names)
        lastname = names.pop()
        print('Hello to the {} of you: {}, and {}!'.format(num, ', '.join(names), lastname))
# --------------------------------------------------
main()
